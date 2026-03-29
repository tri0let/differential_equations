# Differential equation numeric solver + visualizer

This is an initial draft of a project I wanted to make to help with visualizations for MATH 325 this semester. Feel free to fork it and make your own contributions, I'll try to keep up to date with pull requests. 

The dependencies are numpy and matplotlib (see uv.lock for more details).

## Tools currently available

- vector_field: a way to convert a 2-D vector-valued function $f: \mathbb{R^2} \rightarrow \mathbb{R^2}$ into an array of vectors and magnitudes that is compatible with the Quiver and Barbs vector field plotting tools in matplotlib
- phase_portrait: returns x and y values of an approximation to a (potentially non-autonomous) 2D system $(x'(t), y'(t)) = f(x, y, t)$ of differential equations, given an initial condition $t_0, x_0, y_0$. Returns the positive-time ($t>t_0$) and negative-time ($t<t_0$) portions of the solutions as two separate lists so that they can be plotted separately.
- interactive_phase_portrait: plots the (static) vector field for a given differential equation. Click on the plot to make a solution appear.

See `examples.py` for more details and examples of how the functions are used. See `phase_portrait.py` for function definitions.

## To do / wishlist: 

- Add sliders for various parameters to make the plot more interactive
- Add functionality for plotting other things over the interactive plot (right now it only exists within the function)
- Functionality for matrices
- Add 3D!
- Fix bug in `phase_portrait` where the method for calculating backwards trajectories results in a kink at the initial condition