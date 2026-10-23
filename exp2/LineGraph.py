# Experiment No. 2D: Line Graph

# Aim:
# To create a line graph using Python's Matplotlib library to represent changes in data over time.

# Description:
# A line graph represents data using points connected by straight lines.
# It is used to identify trends, increases, and decreases in data over time.

# Algorithm:
# 1. Start the program.
# 2. Import Matplotlib.
# 3. Define the months and sales values.
# 4. Create a line graph using the plot() function.
# 5. Add a title and axis labels.
# 6. Display the graph.
# 7. Stop the program.

# Program:

import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [120, 150, 100, 180, 200, 170]

plt.plot(months, sales, marker='o', color='blue', linestyle='-')

plt.title('Monthly Sales Report')
plt.xlabel('Month')
plt.ylabel('Sales')

plt.show()

# Program Explanation:
# 1. import matplotlib.pyplot as plt imports the plotting module.
# 2. months contains the month names.
# 3. sales contains the corresponding sales values.
# 4. plt.plot() creates the line graph.
# 5. marker='o' displays circular markers at each point.
# 6. plt.title() adds the graph title.
# 7. plt.xlabel() labels the X-axis.
# 8. plt.ylabel() labels the Y-axis.
# 9. plt.show() displays the graph.

# Sample Output:
# A line graph titled "Monthly Sales Report" is displayed.
# The X-axis represents the months from January to June.
# The Y-axis represents the sales values.
# Sales increase from January to February, decrease in March,
# rise to the highest value in May, and decrease in June.

# Result:
# A line graph was created using Python's Matplotlib library to represent monthly sales data and visualize trends over time.
