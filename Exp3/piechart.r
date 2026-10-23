EXPERIMENT 6: PIE CHART IN R

AIM:
To create a pie chart in R to represent the proportions of different categories in a dataset.

DESCRIPTION:
A pie chart is a circular graph divided into sectors, where each sector represents a category's proportion of the total. The size of each sector depends on its numerical value. In R, the pie() function is used to create a pie chart. It is useful for displaying percentages and comparing parts of a whole.

APPLICATIONS:
1. To represent monthly expenses.
2. To display market share of different companies.
3. To show the percentage of students in different courses.
4. To represent survey results.
5. To compare the proportions of different categories.

ALGORITHM:
1. Start the program.
2. Create a vector containing the values for each category.
3. Create a vector containing the category names.
4. Use the pie() function to create the pie chart.
5. Add labels and percentage values.
6. Add a title to the chart.
7. Display the pie chart.
8. Stop the program.

PROGRAM:

# Create a vector containing monthly expenses
expenses <- c(30, 35, 10, 15, 10)

# Create category names
categories <- c("Food", "Rent", "Transport", "Education", "Savings")

# Calculate percentages
percentages <- round(expenses / sum(expenses) * 100)

# Create labels with category names and percentages
labels <- paste(categories, percentages, "%")

# Create the pie chart
pie(expenses,
    labels = labels,
    col = rainbow(length(expenses)),
    main = "Monthly Expense Distribution",
    clockwise = TRUE)

PROGRAM EXPLANATION:
1. expenses <- c(30, 35, 10, 15, 10): Stores the values for five expense categories.
2. categories <- c(...): Stores the names of the expense categories.
3. sum(expenses): Calculates the total of all expense values.
4. expenses / sum(expenses) * 100: Calculates the percentage of each category.
5. round(...): Rounds the percentages to whole numbers.
6. paste(categories, percentages, "%"): Combines category names and percentages to create labels.
7. pie(): Creates the pie
