# Experiment No. 9: Basic Dashboards
Aim
To create basic data visualizations using Python and understand how to combine multiple worksheets into an interactive dashboard in Tableau.

Algorithm
Start the program.

Import the Pandas library and Matplotlib's Pyplot module.

Load the sales_data.csv dataset using pd.read_csv().

Group the data by Category and calculate the total sales for each category.

Create and display a bar chart representing sales by category.

Group the data by Region and calculate the total sales for each region.

Create and display a pie chart representing sales by region.

Plot Quantity against Sales using a line chart.

Add suitable titles and labels to the charts and display them.

Open Tableau and connect to the sales dataset.

Create worksheets for Sales by Category, Sales by Region, and Sales vs Quantity.

Create a new Dashboard and add the three worksheets.

Arrange the visualizations as required and save the workbook.

Stop the program.

Description
A dashboard is a visual representation of important information displayed together on a single screen. It combines multiple charts, graphs, and other visual elements to help users understand data and make decisions.

Python libraries such as Pandas and Matplotlib can be used to create individual visualizations. Tableau allows users to combine multiple worksheets into a single interactive dashboard.

In this experiment, three sales visualizations are created:

Sales by Category: A bar chart comparing total sales across product categories.

Sales by Region: A pie chart showing the percentage contribution of each region to total sales.

Sales vs Quantity: A line chart showing the relationship between quantity and sales.

These visualizations can be recreated as worksheets in Tableau and combined into a dashboard for a consolidated view of sales performance.

Program
# Experiment No. 9: Basic Dashboards
# The following charts are examples of views that can be combined in a Tableau dashboard.

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("sales_data.csv")

# Bar chart: Sales by Category
data.groupby("Category")["Sales"].sum().plot(kind="bar")
plt.title("Sales by Category")
plt.tight_layout()
plt.show()

# Pie chart: Sales by Region
data.groupby("Region")["Sales"].sum().plot(
    kind="pie", autopct="%1.1f%%"
)
plt.title("Sales by Region")
plt.ylabel("")
plt.tight_layout()
plt.show()

# Line chart: Sales vs Quantity
plt.plot(data["Quantity"], data["Sales"], marker="o")
plt.title("Sales vs Quantity")
plt.xlabel("Quantity")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()

# In Tableau, add the worksheets to a Dashboard and arrange them as required.
Explanation
1. Importing Libraries
pandas is used to load and process the sales dataset.

matplotlib.pyplot is used to create the visualizations.

2. Loading the Dataset
pd.read_csv("sales_data.csv") reads the CSV file and stores the data in a DataFrame.

3. Sales by Category
data.groupby("Category")["Sales"].sum() calculates total sales for each category. The plot(kind="bar") method displays the results as a bar chart.

4. Sales by Region
data.groupby("Region")["Sales"].sum() calculates total sales for each region. The pie chart displays each region's percentage contribution using autopct="%1.1f%%".

5. Sales vs Quantity
plt.plot(data["Quantity"], data["Sales"], marker="o") creates a line chart with Quantity on the X-axis and Sales on the Y-axis.

6. Creating a Tableau Dashboard
Open Tableau Public and connect to sales_data.csv.

Create a worksheet for Sales by Category.

Create another worksheet for Sales by Region.

Create a third worksheet for Sales vs Quantity.

Click New Dashboard.

Drag the three worksheets onto the dashboard.

Arrange and resize the charts to fit the dashboard.

Save or publish the workbook as required.

Output
The Python program displays three separate visualizations:

A bar chart showing sales by category.

A pie chart showing sales by region.

A line chart showing sales versus quantity.

In Tableau, these visualizations can be combined into a single dashboard displaying sales information in one place.

Result
Thus, basic sales visualizations were successfully created using Python, and the procedure for combining worksheets into a dashboard in Tableau was studied.

Applications
Monitoring sales performance.

Comparing product category performance.

Analyzing regional sales contributions.

Presenting multiple visualizations in one place.

Supporting business reporting and decision-making.

