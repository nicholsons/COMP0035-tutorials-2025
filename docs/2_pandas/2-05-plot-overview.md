# 5. Introduction to charts with pandas.DataFrame.plot()

The aim during the data exploration phase is to get a better understanding of the data to decide if what you have is
largely free from data quality issues and that it suits the needs of your project.

These are charts for your own use, not for others, so you don't need to focus on visual aesthetics.

## Pandas plot

Pandas has a builtin plotting method, [.plot()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html)
that can be applied to a DataFrame to generate visualisations. These visualisations are also referred to as "charts", "
graphs" or "plots".

By default, pandas `.plot()` uses `matplotlib` as the engine that renders (draws) the
plot. [Matplotlib](https://matplotlib.org) is a Python visualisation library that has more functions than are used by
pandas. You won't be learning matplotlib directly in this tutorial, only the `pandas.plot()` interface.

As pandas is built on matplotlib then you will see common terminology used.

- Data (dataframe): The data to be used in the plot.
- Figure: The overall window that the visualisation is drawn on. This can contain multiple plots or 'axes'.
- Axes: The individual plots within a Figure. Each can have its own labels, titles, ticks, etc. Where there are several
  plots in one figure, these plot are created as 'subplots'.

The typical steps to create a pandas plot are:

- Define the data to be plotted in a dataframe
- Create a figure and axes
- Plot the data on the axes
- Optionally, customise the plot e.g. styling, titles, ticks, labels etc.
- Show the plot

For example:

```Python
import pandas as pd
import matplotlib.pyplot as plt

# Sample DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B': [4, 3, 2, 1]
})

# Using pandas.plot directly creates the figure, axes and allows for some customisation
# matplotlib examples typically split this into separate commands defining fig and ax then adding customisation
ax = df.plot(title='Sample Plot', xlabel='X-axis Label', ylabel='Y-axis Label')

# Save plot (may prefer this to showing the plot)
plt.savefig('sample_plot.png')

# Show the plot
plt.show()
```

You can run this example in `starter/example_plot.py` in your own IDE.

In VS Code the chart usually displays in a separate pop-out window. You need to close this window before running the
code again.

In PyCharm it displays in the Plots pane within the interface.

Note that once the chart is displayed, the code stops executing so you may need to close the chart window before running
further code. You may prefer to save the chart as an image file instead.

## Styling

During the data exploration phase you are not creating a polished chart intended for a particular audience.

You don't need to spend time formatting these charts, however some formatting may be needed beyond the examples included
in the activities.

The [pandas visualisation documentation](https://pandas.pydata.org/docs/user_guide/visualization.html#plot-formatting)
gives you plot formatting guidance and examples. This includes:

- [x and y labels](https://pandas.pydata.org/docs/user_guide/visualization.html#controlling-the-labels)
- [displaying the legend](https://pandas.pydata.org/docs/user_guide/visualization.html#controlling-the-legend)
- [subplots](https://pandas.pydata.org/docs/user_guide/visualization.html#plot-formatting)
- [custom formatters for timeseries plots](https://pandas.pydata.org/docs/user_guide/visualization.html#custom-formatters-for-timeseries-plots)

[Next activity](2-06-plot-distribution)