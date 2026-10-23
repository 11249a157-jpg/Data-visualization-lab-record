Experiment No. 2C: Histogram

Aim:
To create a histogram using Python's Matplotlib library to represent the frequency distribution of numerical data.

Description:
A histogram is a graphical representation of numerical data that displays the frequency distribution of values using adjacent bars. It groups numerical data into intervals called bins.

Histograms help us understand the distribution, spread, and frequency of data. They are commonly used in statistics, data analysis, research, and business applications.

Applications:
1. Understanding the distribution of numerical data.
2. Analyzing students' examination marks.
3. Studying age distributions.
4. Analyzing sales and customer data.
5. Identifying patterns and variations in datasets.

Algorithm:
1. Start the program.
2. Import the pyplot module from Matplotlib.
3. Define a list of numerical values.
4. Create a histogram using the hist() function.
5. Add a title and labels to the axes.
6. Display the histogram using show().
7. Stop the program.

Program:

import matplotlib.pyplot as plt

marks = [45, 50, 55, 60, 62, 65, 67, 70, 72, 75,
         78, 80, 82, 85, 88, 90, 92, 95, 60, 70]

plt.hist(marks, bins=5, color='skyblue', edgecolor='black')

plt.title('Distribution of Students Marks')
plt.xlabel('Marks')
plt.ylabel('Frequency')

plt.show()

Program Explanation:
1. import matplotlib.pyplot as plt imports the plotting module from Matplotlib.
2. marks stores the numerical marks of students.
3. plt.hist() creates a histogram using the numerical values.
4. bins=5 divides the data range into five intervals.
5. color='skyblue' sets the color of the bars.
6. edgecolor='black' adds black outlines to the bars.
7. plt.title() adds a title to the histogram.
8. plt.xlabel() labels the horizontal axis.
9. plt.ylabel() labels the vertical axis.
10. plt.show() displays the histogram.

Sample Output:
A histogram titled "Distribution of Students Marks" is displayed.

The X-axis represents marks grouped into intervals, and the Y-axis represents the frequency of students in each interval. The adjacent bars show how the marks are distributed across the intervals.

Result:
A histogram was created using Python's Matplotlib library to represent the frequency distribution of students' marks. The experiment demonstrates how histograms help visualize the distribution of numerical data.
