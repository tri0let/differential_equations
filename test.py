from phase_portrait import phase_portrait_interactive

def f(x, y, t):
    # return (-2 * x - x**3 - x * y**2, -3 * y + x**2 * y + y**3)
    return (-x, -2 * y)

phase_portrait_interactive(f, yrange=(-2,2), xrange=(-2,2), num_steps=3000, clear=True)