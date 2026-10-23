EXPERIMENT 5: LINE PLOT IN R

AIM:
To create a line plot in R to represent changes in data over a period of time.

DESCRIPTION:
A line plot is a graphical representation of data points connected by straight lines. It is commonly used to show trends and changes in values over time. In R, the plot() function with the type = "o" or type = "l" argument can be used to create a line plot. The type = "o" option displays both points and connecting lines.

APPLICATIONS:
1. To represent monthly sales.
2. To analyze temperature changes over time.
3. To track business growth.
4. To compare performance trends.
5. To visualize changes in data over different time periods.

ALGORITHM:
1. Start the program.
2. Create a vector containing the months.
3. Create a vector containing the corresponding sales values.
4. Use the plot() function to create the line plot.
5. Set the line color and plotting type.
6. Add the graph title and axis labels.
7. Display the line plot.
8. Stop the program.

PROGRAM:

# Create a vector containing months
months <- c("Jan", "Feb", "Mar", "Apr", "May", "Jun")

# Create a vector containing monthly sales
sales <- c(120, 150, 100, 180, 200, 170)

# Create the line plot
plot(sales,
     type = "o",
     col = "blue",
     pch = 16,
     xaxt = "n",
     main = "Monthly Sales Report",
     xlab = "Month",
     ylab = "Sales")

# Display month names on the X-axis
axis(1, at = 1:6, labels = months)

PROGRAM EXPLANATION:
1. months <- c(...): Stores the names of the six months.
2. sales <- c(...): Stores the sales values for each month.
3. plot(sales): Creates a graph using the sales data.
4. type = "o": Displays points connected by lines.
5. col = "blue": Sets the line and points to blue.
6. pch = 16: Displays solid circular points.
7. xaxt = "n": Hides the default X-axis labels.
8. main: Adds the title "Monthly Sales Report".
9. xlab = "Month": Labels the X-axis as Month.
10. ylab = "Sales": Labels the Y-axis as Sales.
11. axis(1, at = 1:6, labels = months): Displays the month names along the X-axis.

SAMPLE OUTPUT:
A blue line plot titled "Monthly Sales Report" is displayed. The X-axis represents January to June, and the Y-axis represents sales. Sales increase and decrease across the months, reaching the highest value of 200 in May.

RESULT:
Thus, a line plot was successfully created in R using the plot() function to visualize monthly sales trends.
