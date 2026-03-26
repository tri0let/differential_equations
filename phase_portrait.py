import numpy as np
import matplotlib.pyplot as plt

#Define a function f: R^2 -> R^2. The differential equation will be taken as
#   (x', y') = f(x, y)

def vector_field(
        f, xrange: tuple[float, float]=(-1.0, 1.0), yrange: tuple[float, float]=(-1.0, 1.0),
        vector_spacing_x: float | None=None, vector_spacing_y: float | None=None
                 ):
    
    f = np.vectorize(f)

    xmin0, xmax0 = xrange
    ymin0, ymax0 = yrange

    if vector_spacing_x is None:
        vector_spacing_x = (xmax0 - xmin0) / 35
    if vector_spacing_y is None:
        vector_spacing_y = (ymax0 - ymin0) / 35

    X, Y = np.meshgrid(np.arange(xmin0, xmax0, vector_spacing_x), np.arange(ymin0, ymax0, vector_spacing_y))

    norm = np.sqrt(f(X, Y)[0]**2 + f(X, Y)[1]**2)
    norm[norm == 0] += min(norm[norm > 0])
    U = f(X, Y)[0]/norm
    V = f(X, Y)[1]/norm

    return X, Y, U, V, norm

def phase_portrait(
        f, x0: float=0.0, y0: float=0.0, t0: float=0.0,
        xrange: tuple[float, float]=(-100.0, 100.0), yrange: tuple[float, float]=(-100.0, 100.0),
        num_steps: int=5000, step_size: float=0.001,
        reverse: bool=True
                    ):
    
    f = np.vectorize(f)

    xmin, xmax = xrange
    ymin, ymax = yrange

    if x0 < xmin or x0 > xmax or y0 < ymin or y0 > ymax:
        raise ValueError(f'Initial condition outside specified range: x between {xmin} and {xmax}, y between {ymin} and {ymax}.')
    
    lx, ly = [x0], [y0]
    rlx, rly = [x0], [y0]

    i = 0
    x, y = x0, y0
    t = t0

    while i < num_steps and 2 * xmin < x < 2 * xmax and 2 * ymin < y < 2 * ymax:
        x += step_size * f(x, y, t)[0]
        y += step_size * f(x, y, t)[1]
        t += step_size
        lx.append(x)
        ly.append(y)
        i += 1

    if reverse:

        i = 0
        x, y = x0, y0
        t = t0
    
        while i > -num_steps and 2 * xmin < x < 2 * xmax and 2 * ymin < y < 2 * ymax:
            x -= step_size * f(x, y, t)[0]
            y -= step_size * f(x, y, t)[1]
            t -= step_size
            rlx.append(x)
            rly.append(y)
            i -= 1
    
    return [lx, ly],[rlx, rly]


def phase_portrait_interactive(
        f, xrange: tuple[float, float]=(-1.0, 1.0), yrange: tuple[float, float]=(-1.0, 1.0),
        vector_spacing_x: float | None=None, vector_spacing_y: float | None=None,
        num_steps: int=5000, step_size: float=0.001,
        reverse: bool=True, clear: bool=True
                   ):
    
    def g(x, y):
        return f(x, y, t=0)
    
    vector_args = vector_field(g, xrange, yrange, vector_spacing_x, vector_spacing_y)


    xmin0, xmax0 = xrange
    ymin0, ymax0 = yrange

    xmargin = 0.05 * (xmax0 - xmin0)
    ymargin = 0.05 * (ymax0 - ymin0)

    xmin = xmin0 + xmargin
    xmax = xmax0 - xmargin
    ymin = ymin0 + ymargin
    ymax = ymax0 - ymargin

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
        
        line_args = phase_portrait(f=f, x0=x0, y0=y0, t0=0, xrange=xrange, yrange=yrange, num_steps=num_steps, step_size=step_size, reverse=reverse)[0]
        rline_args = phase_portrait(f, x0, y0, t0=0, xrange=xrange, yrange=yrange, num_steps=num_steps, step_size=step_size, reverse=reverse)[1]

        line = ax.plot(*line_args, color='red')

        if reverse:
            rline = ax.plot(*rline_args, color='red', linestyle='--')
        
        plt.show()

    fig.canvas.mpl_connect('pick_event', onpick)
    ax.quiver(*vector_args)
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)
    ax.set_title('Click anywhere to set an initial condition')
    plt.show()
