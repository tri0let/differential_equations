import numpy as np
import matplotlib.pyplot as plt

#Define a function f: R^2 -> R^2. The differential equation will be taken as
#   (x', y') = f(x, y)

def phase_portrait(
        f, xrange: tuple[float, float]=(-1.0, 1.0), yrange: tuple[float, float]=(-1.0, 1.0),
        vector_spacing_x: float | None=None, vector_spacing_y: float | None=None,
        num_steps: int=5000, step_size: float=0.001,
        reverse: bool=False, clear: bool=True
                   ):
    

    f = np.vectorize(f)

    xmin0, xmax0 = xrange
    ymin0, ymax0 = yrange

    if vector_spacing_x is None:
        vector_spacing_x = (xmax0 - xmin0) / 35
    if vector_spacing_y is None:
        vector_spacing_y = (ymax0 - ymin0) / 35

    X, Y = np.meshgrid(np.arange(xmin0, xmax0, vector_spacing_x), np.arange(ymin0, ymax0, vector_spacing_y))

    xmargin = 0.05 * (np.max(X) - np.min(X))
    ymargin = 0.05 * (np.max(Y) - np.min(Y))

    xmin = xmin0 + xmargin
    xmax = xmax0 - xmargin
    ymin = ymin0 + ymargin
    ymax = ymax0 - ymargin

    norm = np.sqrt(f(X, Y)[0]**2 + f(X, Y)[1]**2)
    norm[norm==0] += 0.01
    U = f(X, Y)[0]/norm
    V = f(X, Y)[1]/norm

    def pos_picker(self, mouseevent):
        props = dict(pickx=mouseevent.xdata, picky=mouseevent.ydata)
        return True, props

    fig, ax = plt.subplots(picker=pos_picker)

    def onpick(event):
        global line
        if reverse:
            global rline

        if event.pickx is None or event.picky is None:
            return None

        x0 = event.pickx
        y0 = event.picky
        lx, ly = [x0], [y0]
        rlx, rly = [x0], [y0]

        i = 0
        x, y = x0, y0

        while i < num_steps and 2 * xmin < x < 2 * xmax and 2 * ymin < y < 2 * ymax:
            x += step_size * f(x, y)[0]
            y += step_size * f(x, y)[1]
            lx.append(x)
            ly.append(y)
            i += 1

        if reverse:

            i = 0
            x, y = x0, y0
        
            while i > - num_steps and 2 * xmin < x < 2 * xmax and 2 * ymin < y < 2 * ymax:
                x -= step_size * f(x, y)[0]
                y -= step_size * f(x, y)[1]
                rlx.append(x)
                rly.append(y)
                i -= 1

        if clear:
            if reverse:
                try:
                    ax.lines[0].remove()
                    ax.lines[0].remove()
                except:
                    pass
            else:
                try:
                    ax.lines[0].remove()
                except:
                    pass
        
        line = ax.plot(lx, ly, color='red')

        if reverse:
            rline = ax.plot(rlx, rly, color='red', linestyle='--')
        plt.show()

    fig.canvas.mpl_connect('pick_event', onpick)
    ax.quiver(X, Y, U, V, norm)
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)


    x0 = []
    y0 = []
    for t in np.linspace(-2, 5, 50):
        x0.append(np.exp(-t))
        y0.append(np.exp(-2*t))
    ax.plot(x0,y0)



    plt.show()
