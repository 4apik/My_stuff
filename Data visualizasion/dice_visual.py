import pygal
import matplotlib.pyplot as plt

from die import Die

# Create a D6 and a D10.
die_1 = Die()
die_2 = Die(10)

# Make some rolls, and store results in a list.
results = [(die_1.roll() + die_2.roll()) for _ in range(50000)]

# Analize the results.
max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result+1)]

possible_results = [f"{value}" for value in range(2, max_result+1)]

# Visualize the results.
hist = pygal.Bar()

hist._title = "Results of rolling a D6 and a D10 50000 times."
hist.x_labels = possible_results
hist._x_title = "Result"
hist._y_title = "Frequency of Result"

hist.add('D6 + D10', frequencies)
hist.render_to_file('dice_visual.svg')

# MATPLOTLIB section
plt.plot(possible_results, frequencies, linewidth=5)
plt.show()
