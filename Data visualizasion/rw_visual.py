import matplotlib.pyplot as plt
import pygal

from random_walk import RandomWalk

# Make a random walk, and plot the points.
rw = RandomWalk(5000)
rw.fill_walk()

# Set the size of the plotting window.
plt.figure(figsize=(10,6))

point_numbers = list(range(rw.num_points))
plt.scatter(rw.x_values, rw.y_values, c=point_numbers,
            cmap=plt.cm.Blues, edgecolor='none', s=1)

# Emphasize the first and last points.
plt.scatter(0, 0, c='green', edgecolors='none', s=100)
plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

# Remove the axes.
plt.axis('off')

plt.show()
# PYGAL section
x_steps = [rw.get_step() for _ in range(5001)]
y_steps = [rw.get_step() for _ in range(5001)]
abs_x = [abs(x) for x in x_steps]
abs_y = [abs(y) for y in y_steps]
x_plus = [x for x in x_steps if x > 0]
y_plus = [y for y in y_steps if y > 0]
x_minus = [x for x in x_steps if x < 0]
y_minus = [y for y in y_steps if y < 0]

frequencies = [(abs_x + abs_y).count(value) for value in range(0, 5)]
for list in [x_plus, x_minus, y_plus, y_minus]:
    frequencies.append(len(list))
hist = pygal.Bar()
hist._title = "Results of a random walk with 5000 steps"
hist.x_labels = ['0', '1', '2', '3', '4', 'x+', 'x-', 'y+', 'y-']
hist._x_title = "Distance and Directions"
hist._y_title = "Frequency"

hist.add('Random walk', frequencies)
hist.render_to_file('rw_visual.svg')
