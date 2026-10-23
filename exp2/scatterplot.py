EXPERIMENT NAME: Scatter Plot

AIM:
To represent the relationship between two numerical variables using a scatter plot in Python.

DESCRIPTION:
A scatter plot is a type of graph that displays the relationship between two numerical variables using individual points. Each point represents one pair of values. The X-axis represents one variable, and the Y-axis represents another variable. A scatter plot helps identify patterns, trends, and relationships between the variables.

APPLICATIONS:
1. To analyze the relationship between study hours and examination marks.
2. To identify patterns and trends in data.
3. To compare two numerical variables.
4. To detect unusual values or outliers.
5. To support data analysis and decision-making.

ALGORITHM:
1. Start the program.
2. Import the Matplotlib library.
3. Define the X-axis and Y-axis data.
4. Create a scatter plot using the scatter() function.
5. Add a title and labels to both axes.
6. Display the grid.
7. Display the graph using show().
8. Stop the program.

PROGRAM:

import matplotlib.pyplot as plt

hours = [1, 2, 3, 4, 5, 6, 7, 8]
marks = [35, 40, 50, 55, 65, 70, 80, 90]

plt.scatter(hours, marks, color='blue', marker='o')

plt.title('Study Hours vs Examination Marks')
plt.xlabel('Study Hours')
plt.ylabel('Examination Marks')

plt.grid(True)
plt.show()

PROGRAM EXPLANATION:
1. import matplotlib.pyplot as plt: Imports the Matplotlib library for creating graphs.
2. hours: Stores the number of hours spent studying.
3. marks: Stores the corresponding examination marks.
4. plt.scatter(): Creates a scatter plot using the given values.
5. color='blue': Sets the points to blue.
6. marker='o': Displays the data points as circles.
7. plt.title(): Adds a title to the graph.
8. plt.xlabel(): Labels the X-axis as Study Hours.
9. plt.ylabel(): Labels the Y-axis as Examination Marks.
10. plt.grid(True): Displays grid lines for easier reading.
11. plt.show(): Displays the scatter plot.

SAMPLE OUTPUT:
A scatter plot titled "Study Hours vs Examination Marks" is displayed. The X-axis represents study hours, and the Y-axis represents examination marks. The plotted points show a generally positive relationship, meaning that marks tend to increase as study hours increase.

RESULT:
Thus, the scatter plot was successfully created using Python and Matplotlib to visualize the relationship between study hours and examination marks.
