from phase_portrait import phase_portrait

def f(x, y):
    # return (-2 * x - x**3 - x * y**2, -3 * y + x**2 * y + y**3)
    return (-x, -2 * y)

phase_portrait(f, yrange=(-2,2), xrange=(-2,2), reverse=True)