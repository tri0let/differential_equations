import numpy as np
from phase_portrait import phase_portrait_interactive, vector_field, phase_portrait
import matplotlib.pyplot as plt

#============ Define some functions ===========

def f(x, y, t):
    # return (-y * x - x**3 - x * y**2, -3 * y + x**2 * y + y**3)
    return ((1) * x + (-0.5) * y, (0.5) * x + (1) * y)

def g(x, y):
    return (np.sin(x + y), np.cos(x - y))

def h(x, y, t):
    return (np.cos(t * x), -np.sin(t**2 * x))

#=========== Make an interactive phase portrait of f ==========

phase_portrait_interactive(f, yrange=(-2,2), xrange=(-2,2), num_steps=3000, clear=True)

#=========== Plot a vector field of g ============

vector_args = vector_field(g, xrange=(-1, 1), yrange=(-1,1))

fig1, ax1 = plt.subplots()
ax1.quiver(*vector_args)
plt.show()

#=========== Approximate a solution to g ===========

solution_args, neg_solution_args = phase_portrait(h, x0=2, y0=2, t0=0, reverse=True)

fig2, ax2 = plt.subplots()
ax2.plot(*solution_args, color='blue', linestyle='-', label='Positive-time solution')
ax2.plot(*neg_solution_args, color='red', linestyle='--', label='Negative-time solution')
ax2.legend()
plt.show()