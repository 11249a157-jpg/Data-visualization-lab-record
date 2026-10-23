EXPERIMENT 7: SCATTER PLOT IN R

AIM:
To create a scatter plot in R to visualize the relationship between two numerical variables.

DESCRIPTION:
A scatter plot is a graphical representation of two numerical variables using individual points. Each point represents a pair of values, one on the X-axis and the other on the Y-axis. It helps identify relationships, patterns, trends, and unusual values in a dataset. In R, the plot() function is used to create a scatter plot.

APPLICATIONS:
1. To analyze the relationship between study hours and examination marks.
2. To identify positive and negative relationships between variables.
3. To detect unusual values or outliers.
4. To study relationships between sales and advertising expenses.
5. To visualize numerical data for statistical analysis.

ALGORITHM:
1. Start the program.
2. Create a vector containing the X-axis values.
3. Create a vector containing the Y-axis values.
4. Use the plot() function to create a scatter plot.
5. Specify the plotting symbol and color.
6. Add a title and labels to both axes.
7. Display the scatter plot.
8. Stop the program.

PROGRAM:

# Create a vector containing study hours
hours <- c(1, 2, 3, 4, 5, 6, 7, 8)

# Create a vector containing examination marks
marks <- c(35, 40, 50, 55, 65, 70, 80, 90)

# Create the scatter plot
plot(hours, marks,
     main = "Study Hours vs Examination Marks",
     xlab = "Study Hours",
     ylab = "Examination Marks",
     col = "blue",
     pch = 16)

PROGRAM EXPLANATION:
1. hours <- c(1, 2, 3, 4, 5, 6, 7, 8): Creates a vector containing study hours.
2. marks <- c(35, 40, 50, 55, 65, 70, 80, 90): Stores the corresponding examination marks.
3. plot(hours, marks): Creates a scatter plot using study hours and marks.
4. main: Adds the title "Study Hours vs Examination Marks".
5. xlab = "Study Hours": Labels the X-axis.
6. ylab = "Examination Marks": Labels the Y-axis.
7. col = "blue": Sets the points to blue.
8. pch = 16: Displays solid circular points.

SAMPLE OUTPUT:
A scatter plot titled "Study Hours vs Examination Marks" appears with blue points. The X-axis represents study hours, and the Y-axis represents examination marks. The points show a generally positive relationship, as examination marks tend to increase with study hours.

RESULT:
Thus, a scatter plot was successfully created in R using the plot() function to visualize the relationship between study hours and examination marks.
