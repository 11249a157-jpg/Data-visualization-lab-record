EXPERIMENT 3: BAR PLOT .R

AIM:
To create a bar plot in R to represent and compare categorical data using rectangular bars.

DESCRIPTION:
A bar plot is a graphical representation of categorical data using rectangular bars. The height of each bar represents the value of a category. Bar plots are useful for comparing different categories. In R, the barplot() function is used to create a bar plot.

APPLICATIONS:
1. To compare the sales of different products.
2. To represent the number of students in different courses.
3. To compare the performance of different categories.
4. To display survey results.
5. To visualize categorical data.

ALGORITHM:
1. Start the program.
2. Create a vector containing numerical values.
3. Create a vector containing category names.
4. Use the barplot() function to create the graph.
5. Add the title and axis labels.
6. Set the color of the bars.
7. Display the bar plot.
8. Stop the program.

PROGRAM:

# Create a vector containing student numbers
students <- c(40, 30, 25, 20, 35)

# Create a vector containing programming languages
languages <- c("Python", "Java", "C", "C++", "JavaScript")

# Create the bar plot
barplot(students,
        names.arg = languages,
        col = "skyblue",
        main = "Programming Languages Preferred by Students",
        xlab = "Programming Languages",
        ylab = "Number of Students")

PROGRAM EXPLANATION:
1. students <- c(40, 30, 25, 20, 35): Creates a vector containing the number of students.
2. languages <- c("Python", "Java", "C", "C++", "JavaScript"): Stores the programming language names.
3. barplot(students): Creates a bar plot using the student values.
4. names.arg = languages: Displays the language names below the bars.
5. col = "skyblue": Sets the color of the bars to sky blue.
6. main: Adds the title to the graph.
7. xlab: Labels the X-axis.
8. ylab: Labels the Y-axis.

SAMPLE OUTPUT:
A bar plot appears with five sky-blue bars representing Python, Java, C, C++, and JavaScript. The respective values are 40, 30, 25, 20, and 35 students. The graph displays the title "Programming Languages Preferred by Students."

RESULT:
Thus, a bar plot was successfully created in R using the barplot() function to compare the number of students who prefer different programming languages.
