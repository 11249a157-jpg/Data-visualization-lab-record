Experiment No. 3: Basic Visualization in R
Aim
To create and display different types of data visualizations, including line graphs, bar charts, pie charts, scatter plots, and histograms using the R programming language.

Algorithm
Start the program.

Define the data required for each visualization using the c() function.

Create a line graph using the plot() function with type="o" to display points connected by lines.

Create a bar chart using the barplot() function to compare marks across different subjects.

Create a pie chart using the pie() function to represent the distribution of values.

Create a scatter plot using the plot() function with pch=19 to show the relationship between study hours and marks.

Create a histogram using the hist() function to display the frequency distribution of marks.

Add suitable titles and axis labels to the visualizations.

Display the graphs in the R graphics window.

Stop the program.

Description
Data visualization is the process of presenting data graphically to make it easier to understand and analyze. R is a programming language widely used for statistical computing, data analysis, and visualization.

R provides built-in functions for creating different types of graphs without requiring additional visualization packages.

Line Graph: Displays changes in values and helps identify trends.

Bar Chart: Compares numerical values across different categories.

Pie Chart: Represents the proportion of each category as a part of the whole.

Scatter Plot: Shows the relationship between two numerical variables.

Histogram: Displays the frequency distribution of numerical data grouped into intervals.

These visualizations help users interpret data, identify patterns, and communicate findings effectively.

Program
# Experiment No. 3: Basic Visualization in R
# Aim: Create line, bar, pie, scatter and histogram visualizations.

# Line graph
x <- c(1, 2, 3, 4, 5)
y <- c(10, 20, 15, 25, 30)
plot(x, y, type="o", main="Line Graph",
     xlab="X Values", ylab="Y Values")

# Bar chart
marks <- c(85, 75, 80, 90)
subjects <- c("Python", "Java", "R", "Tableau")
barplot(marks, names.arg=subjects,
        main="Marks by Subject",
        xlab="Subject", ylab="Marks")

# Pie chart
pie(marks, labels=subjects, main="Technology Usage")

# Scatter plot
hours <- c(1, 2, 3, 4, 5, 6)
student_marks <- c(45, 50, 58, 65, 72, 80)
plot(hours, student_marks,
     main="Study Hours vs Marks",
     xlab="Study Hours", ylab="Marks", pch=19)

# Histogram
all_marks <- c(45, 50, 52, 55, 58, 60, 62, 65, 68,
               70, 72, 75, 78, 80, 82, 85, 88, 90)
hist(all_marks, breaks=5,
     main="Distribution of Marks",
     xlab="Marks", ylab="Frequency")
Explanation
1. Line Graph
x and y store the numerical values for the graph.

plot() creates the graph.

type="o" displays points connected by lines.

main specifies the title, while xlab and ylab specify the axis labels.

2. Bar Chart
marks stores the marks for four subjects.

subjects stores the corresponding subject names.

barplot() creates the bar chart.

names.arg=subjects displays the subject names below the bars.

3. Pie Chart
pie() creates a circular chart representing the values.

labels=subjects assigns subject names to the slices.

main="Technology Usage" sets the chart title.

4. Scatter Plot
hours stores the number of study hours.

student_marks stores the corresponding student marks.

plot() displays the relationship between the two variables.

pch=19 represents data points using solid circles.

5. Histogram
all_marks stores a collection of student marks.

hist() groups the numerical values into intervals and displays their frequencies.

breaks=5 suggests five intervals; R may adjust the actual number of bins.

The X-axis represents marks, and the Y-axis represents frequency.

Output
The program generates five visualizations in the R graphics window:

A line graph showing changes in the given values.

A bar chart comparing marks across Python, Java, R, and Tableau.

A pie chart showing the distribution of the four values.

A scatter plot illustrating the relationship between study hours and marks.

A histogram showing the frequency distribution of student marks.

Result
Thus, line graphs, bar charts, pie charts, scatter plots, and histograms were successfully created using the built-in graphical functions of the R programming language.

Applications
Analyzing trends and patterns in data.

Comparing marks across different subjects.

Representing proportions and percentage distributions.

Studying relationships between numerical variables.

Understanding the frequency distribution of numerical data.

