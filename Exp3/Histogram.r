EXPERIMENT 4: HISTOGRAM IN R

AIM:
To create a histogram in R to represent the frequency distribution of numerical data.

DESCRIPTION:
A histogram is a graphical representation of the frequency distribution of continuous numerical data. It uses adjacent rectangular bars to show how data values are distributed across different intervals called bins. In R, the hist() function is used to create a histogram.

APPLICATIONS:
1. To analyze the distribution of students' marks.
2. To understand the distribution of numerical data.
3. To identify the most frequent range of values.
4. To study data variability and patterns.
5. To detect skewness and unusual distributions.

ALGORITHM:
1. Start the program.
2. Create a vector containing numerical data.
3. Use the hist() function to create a histogram.
4. Specify the color of the bars.
5. Add a title to the graph.
6. Label the X-axis and Y-axis.
7. Display the histogram.
8. Stop the program.

PROGRAM:

# Create a vector containing students' marks
marks <- c(45, 50, 55, 60, 62, 65, 67, 70, 72, 75,
           78, 80, 82, 85, 88, 90, 92, 95, 60, 70)

# Create the histogram
hist(marks,
     breaks = 5,
     col = "skyblue",
     main = "Distribution of Students' Marks",
     xlab = "Marks",
     ylab = "Frequency",
     border = "black")

PROGRAM EXPLANATION:
1. marks <- c(...): Creates a vector containing the marks of 20 students.
2. hist(marks): Creates a histogram using the marks data.
3. breaks = 5: Requests approximately five intervals (bins) for grouping the marks.
4. col = "skyblue": Sets the bars to sky blue.
5. main: Adds the title to the histogram.
6. xlab = "Marks": Labels the X-axis as Marks.
7. ylab = "Frequency": Labels the Y-axis as Frequency.
8. border = "black": Sets the borders of the bars to black.

SAMPLE OUTPUT:
A histogram titled "Distribution of Students' Marks" appears with sky-blue bars and black borders. The X-axis represents marks, and the Y-axis represents the frequency of students within each interval.

RESULT:
Thus, a histogram was successfully created in R using the hist() function to visualize the frequency distribution of students' marks.
