Experiment No. 2: Bar Graph

Aim:
To create a bar graph using Python's Matplotlib library to represent and compare values across different categories.

Description:
A bar graph is a data visualization technique that uses rectangular bars to represent values for different categories. The height or length of each bar corresponds to the value it represents.

Bar graphs are widely used in education, business, research, and statistical analysis to compare quantities and present information clearly.

Applications of Bar Graphs:
1. Comparing values across different categories.
2. Representing students' preferences for programming languages.
3. Comparing sales of different products.
4. Displaying population figures across regions.
5. Presenting survey results.

Algorithm:
1. Start the program.
2. Import the pyplot module from Matplotlib.
3. Define the categories and their corresponding values.
4. Create a bar graph using the bar() function.
5. Add a title and label the X-axis and Y-axis.
6. Display the graph using show().
7. Stop the program.

Program:

import matplotlib.pyplot as plt

categories = ['Python', 'Java', 'C', 'C++', 'JavaScript']
students = [40, 30, 25, 20, 35]

plt.bar(categories, students, color='skyblue', edgecolor='black')

plt.title('Programming Languages Preferred by Students')
plt.xlabel('Programming Languages')
plt.ylabel('Number of Students')

plt.show()

Program Explanation:
1. import matplotlib.pyplot as plt: Imports the plotting module from Matplotlib.
2. categories: Stores the programming language names.
3. students: Stores the number of students for each category.
4. plt.bar(): Creates a vertical bar graph.
5. color='skyblue': Sets the color of the bars to sky blue.
6. edgecolor='black': Adds black outlines to the bars.
7. plt.title(): Sets the title of the graph.
8. plt.xlabel(): Labels the horizontal axis.
9. plt.ylabel(): Labels the vertical axis.
10. plt.show(): Displays the generated graph.

Sample Output:
A vertical bar graph is displayed with the title "Programming Languages Preferred by Students".

X-axis: Programming Languages
Y-axis: Number of Students

Python: 40 students
Java: 30 students
C: 25 students
C++: 20 students
JavaScript: 35 students

Python has the highest value of 40 students, while C++ has the lowest value of 20 students.

Result:
A bar graph was created using Python's Matplotlib library to compare the number of students associated with different programming languages. The experiment demonstrates how bar graphs help visualize categorical data effectively.
