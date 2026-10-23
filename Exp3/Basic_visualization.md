# Experiment No. 3: Basic Visualization in R

## Aim
To implement fundamental data visualization techniques in R and examine how different graphical representations help in analyzing and interpreting data.

## Description
R is a programming language designed for statistical analysis, data manipulation, and graphical presentation. Its built-in graphics functions allow users to create visualizations without installing additional packages. For more advanced and customized graphics, R also provides packages such as `ggplot2`.

Graphs play an important role in exploratory data analysis because they help reveal important characteristics of a dataset before applying statistical methods. Different graphs are suitable for different purposes. Line graphs illustrate changes across ordered observations, bar charts compare categories, pie charts show proportions, scatter plots display relationships between numerical variables, and histograms summarize the frequency distribution of data.

In this experiment, five basic graphs are developed using base R functions. Each program demonstrates how data can be stored in vectors, passed to a plotting function, and presented with suitable titles and labels. These techniques form the foundation for visualizing larger datasets and developing more advanced analytical reports.

## Applications
- Exploring data before performing statistical analysis.
- Comparing values among different categories.
- Observing changes and trends in ordered data.
- Examining associations between numerical variables.
- Understanding the spread and frequency of observations.
- Communicating analytical findings through graphical displays.

## Algorithm
1. Start the R environment.
2. Define vectors containing the required sample data.
3. Choose a graph function based on the visualization objective.
4. Supply the data and any required category labels to the function.
5. Add a suitable chart title and axis labels wherever applicable.
6. Execute the program to generate the graph.
7. Examine the visualization and interpret the displayed information.

## Functions Used

| Function | Purpose |
|---|---|
| `plot()` | Creates line graphs and scatter plots, depending on the arguments supplied. |
| `barplot()` | Represents values using rectangular bars for category comparison. |
| `pie()` | Displays the relative proportions of values as circular sectors. |
| `hist()` | Groups numerical observations into intervals and displays their frequencies. |
| `c()` | Combines values into a vector for use in the plotting programs. |

These functions belong to the base R graphics system, so the five programs can be executed without installing external visualization packages.

## Result
The five fundamental visualizations—line graph, bar chart, pie chart, scatter plot, and histogram—were implemented using base R. The experiment demonstrates how graphical functions can be used to compare categories, identify trends, investigate relationships, and understand the distribution of numerical data.
