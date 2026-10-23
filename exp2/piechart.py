# Experiment No. 2E: Pie Chart

# Aim:
# To create a pie chart using Python's Matplotlib library to represent
# data as proportions of a whole.

# Algorithm:
# 1. Import Matplotlib.
# 2. Define categories and their values.
# 3. Create a pie chart using the pie() function.
# 4. Display category labels and percentages.
# 5. Add a title and display the chart.
# 6. Stop the program.

# Program:

import matplotlib.pyplot as plt

categories = ['Food', 'Rent', 'Transport', 'Education', 'Savings']
expenses = [30, 35, 10, 15, 10]

plt.pie(
    expenses,
    labels=categories,
    autopct='%1.1f%%',
    startangle=90
)

plt.title('Monthly Expense Distribution')
plt.axis('equal')
plt.show()

# Program Explanation:
# categories stores the names of expense categories.
# expenses stores the corresponding expense values.
# plt.pie() creates the pie chart.
# labels displays the category names.
# autopct displays percentages on the slices.
# startangle=90 sets the starting angle of the chart.
# plt.title() adds the chart title.
# plt.axis('equal') ensures the pie chart is circular.
# plt.show() displays the chart.

# Sample Output:
# A pie chart titled "Monthly Expense Distribution" is displayed.
# Food: 30%
# Rent: 35%
# Transport: 10%
# Education: 15%
# Savings: 10%

# Result:
# A pie chart was created successfully using Matplotlib to represent
# the distribution of monthly expenses.
