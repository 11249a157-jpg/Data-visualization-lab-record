# Experiment No. 8: Data Visualizations – Charts, Graphs and Data Mapping
Aim
To create and display different data visualizations, including bar charts, pie charts, and line charts, using Python, Pandas, and Matplotlib to analyze sales data.

Algorithm
Start the program.

Import the Pandas library and Matplotlib's Pyplot module.

Load the sales_data.csv dataset using pd.read_csv().

Group the data by Category and calculate the total sales for each category.

Create a bar chart to compare sales across categories.

Group the data by Region and calculate the total sales for each region.

Create a pie chart to represent the percentage distribution of sales across regions.

Plot Quantity against Sales using a line chart.

Add suitable titles and axis labels to each visualization.

Adjust the layout and display each chart using plt.show().

Stop the program.

Description
Data visualization is the graphical representation of data using charts, graphs, and maps. It helps users understand patterns, compare values, and identify relationships within datasets.

In this experiment, Python libraries Pandas and Matplotlib are used to analyze and visualize sales data.

Bar Chart: Compares total sales across product categories.

Pie Chart: Displays the percentage contribution of each region to total sales.

Line Chart: Shows the relationship between quantity and sales values.

Pandas is used for loading, grouping, and aggregating the dataset, while Matplotlib is used to create and display the visualizations.

Program
# Experiment No. 8: Data Visualizations - Charts, Graphs and Data Mapping

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("sales_data.csv")

# Bar chart: sales by category
data.groupby("Category")["Sales"].sum().plot(kind="bar")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()

# Pie chart: sales by region
data.groupby("Region")["Sales"].sum().plot(
    kind="pie", autopct="%1.1f%%"
)
plt.title("Sales by Region")
plt.ylabel("")
plt.tight_layout()
plt.show()

# Line chart: sales versus quantity
plt.plot(data["Quantity"], data["Sales"], marker="o")
plt.title("Sales vs Quantity")
plt.xlabel("Quantity")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()
Explanation
1. Importing Libraries
pandas is used to load and manipulate sales data.

matplotlib.pyplot is used to create charts and graphs.

2. Loading the Dataset
pd.read_csv("sales_data.csv") loads the sales dataset into a DataFrame named data.

3. Bar Chart: Sales by Category
groupby("Category") groups the records by product category.

["Sales"].sum() calculates total sales for each category.

plot(kind="bar") creates a bar chart.

plt.title(), plt.xlabel(), and plt.ylabel() add the chart title and axis labels.

4. Pie Chart: Sales by Region
groupby("Region")["Sales"].sum() calculates total sales for each region.

plot(kind="pie") creates a pie chart.

autopct="%1.1f%%" displays each region's percentage contribution.

plt.ylabel("") removes the default vertical-axis label.

5. Line Chart: Sales Versus Quantity
plt.plot(data["Quantity"], data["Sales"], marker="o") plots Quantity on the X-axis and Sales on the Y-axis.

marker="o" displays circular markers for individual data points.

The title and axis labels make the visualization easier to interpret.

6. Adjusting the Layout
plt.tight_layout() adjusts the spacing of chart elements to prevent labels and titles from overlapping.

7. Displaying the Charts
plt.show() displays each chart in a separate plotting window.

Sample Output
The program generates the following three visualizations:

Sales by Category: A bar chart comparing total sales for Electronics and Furniture.

Sales by Region: A pie chart showing the percentage contribution of each region to total sales.

Sales vs Quantity: A line chart plotting sales against quantity for each row in the dataset.

Result
Thus, bar, pie, and line charts were successfully created using Python, Pandas, and Matplotlib to visualize and analyze sales data by category, region, and quantity.

Applications
Comparing sales across product categories.

Analyzing regional sales contributions.

Examining the relationship between quantity and sales.

Identifying sales trends and patterns.

Presenting business data through graphical reports.

