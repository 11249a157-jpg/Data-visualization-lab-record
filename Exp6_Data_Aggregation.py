# Experiment No. 6: Data Aggregation and Statistical Functions

## Aim
To calculate summary statistics and perform data aggregation on sales data using Python and the Pandas library.

## Algorithm
1. Start the program.
2. Import the Pandas library.
3. Load the `sales_data.csv` dataset using `pd.read_csv()`.
4. Calculate summary statistics for the `Sales` and `Quantity` columns using the `describe()` function.
5. Group the dataset by `Category` and calculate the total sales for each category using `groupby()` and `sum()`.
6. Group the dataset by `Region` and calculate the average sales for each region using `groupby()` and `mean()`.
7. Group the dataset by `Region` and calculate the total sales for each region using `groupby()` and `sum()`.
8. Display all the calculated statistics and aggregated results.
9. Stop the program.

## Description
Data aggregation is the process of grouping data and calculating summary values to understand patterns and trends. Statistical functions help summarize numerical data and support data-driven decision-making.

The Pandas library provides several functions for statistical analysis and aggregation.

- **`describe()`**: Calculates count, mean, standard deviation, minimum, maximum, and quartile values for numerical columns.
- **`groupby()`**: Groups rows based on a specified column, such as Category or Region.
- **`sum()`**: Calculates the total value of a numerical column.
- **`mean()`**: Calculates the average value of a numerical column.

In this experiment, sales data is analyzed to obtain summary statistics, total sales by category, average sales by region, and total sales by region.

## Program

```python id="w1z5ra"
# Experiment No. 6: Data Aggregation and Statistical Functions
# Aim: Calculate summary statistics and aggregate sales data.

import pandas as pd

data = pd.read_csv("sales_data.csv")

print("Summary statistics:")
print(data[["Sales", "Quantity"]].describe())

print("\nTotal sales by category:")
print(data.groupby("Category")["Sales"].sum())

print("\nAverage sales by region:")
print(data.groupby("Region")["Sales"].mean())

print("\nTotal sales by region:")
print(data.groupby("Region")["Sales"].sum())
```

## Explanation

### 1. Importing Pandas
`import pandas as pd` imports the Pandas library for data analysis and manipulation.

### 2. Loading the Dataset
`pd.read_csv("sales_data.csv")` loads the sales dataset into a DataFrame named `data`.

### 3. Calculating Summary Statistics
`data[["Sales", "Quantity"]].describe()` calculates statistical measures for the Sales and Quantity columns, including:
- Count
- Mean
- Standard deviation
- Minimum
- 25th percentile
- Median (50th percentile)
- 75th percentile
- Maximum

### 4. Total Sales by Category
`data.groupby("Category")["Sales"].sum()` groups the data by product category and calculates the total sales for each category.

### 5. Average Sales by Region
`data.groupby("Region")["Sales"].mean()` groups the data by region and calculates the average sales for each region.

### 6. Total Sales by Region
`data.groupby("Region")["Sales"].sum()` groups the data by region and calculates the total sales for each region.

### 7. Displaying the Results
The `print()` function displays the summary statistics and aggregation results on the screen.

## Sample Output

```text id="yq28z1"
Summary statistics:
              Sales   Quantity
count      6.000000   6.000000
mean   19166.666667   2.833333
std    20157.631140   1.471960
min     3000.000000   1.000000
25%     5500.000000   2.000000
50%    13500.000000   2.500000
75%    23750.000000   3.750000
max    55000.000000   5.000000

Total sales by category:
Category
Electronics    78000
Furniture      37000
Name: Sales, dtype: int64

Average sales by region:
Region
East      7000.0
North    22500.0
South    29000.0
West      5000.0
Name: Sales, dtype: float64

Total sales by region:
Region
East      7000
North    45000
South    58000
West      5000
Name: Sales, dtype: int64
```

**Note:** The sample output is based on the six-row `sales_data.csv` dataset used in the earlier experiment. Your output may differ if your dataset contains different records.

## Result
Thus, summary statistics were calculated, and sales data was successfully aggregated by category and region using Pandas statistical and grouping functions.

## Applications
- Analyzing total sales across product categories.
- Comparing sales performance across regions.
- Calculating average sales and quantities.
- Identifying high-performing categories and regions.
- Preparing summarized datasets for charts and dashboards.


JONNA LAHARI 11249A134
1:04 PM (0 minutes ago)
to 11249A212, me

# Experiment No. 6: Data Aggregation and Statistical Functions

## Aim
To calculate summary statistics and perform data aggregation on sales data using Python and the Pandas library.

## Algorithm
1. Start the program.
2. Import the Pandas library.
3. Load the `sales_data.csv` dataset using `pd.read_csv()`.
4. Calculate summary statistics for the `Sales` and `Quantity` columns using the `describe()` function.
5. Group the dataset by `Category` and calculate the total sales for each category using `groupby()` and `sum()`.
6. Group the dataset by `Region` and calculate the average sales for each region using `groupby()` and `mean()`.
7. Group the dataset by `Region` and calculate the total sales for each region using `groupby()` and `sum()`.
8. Display all the calculated statistics and aggregated results.
9. Stop the program.

## Description
Data aggregation is the process of grouping data and calculating summary values to understand patterns and trends. Statistical functions help summarize numerical data and support data-driven decision-making.

The Pandas library provides several functions for statistical analysis and aggregation.

- **`describe()`**: Calculates count, mean, standard deviation, minimum, maximum, and quartile values for numerical columns.
- **`groupby()`**: Groups rows based on a specified column, such as Category or Region.
- **`sum()`**: Calculates the total value of a numerical column.
- **`mean()`**: Calculates the average value of a numerical column.

In this experiment, sales data is analyzed to obtain summary statistics, total sales by category, average sales by region, and total sales by region.

## Program

```python id="w1z5ra"
# Experiment No. 6: Data Aggregation and Statistical Functions
# Aim: Calculate summary statistics and aggregate sales data.

import pandas as pd

data = pd.read_csv("sales_data.csv")

print("Summary statistics:")
print(data[["Sales", "Quantity"]].describe())

print("\nTotal sales by category:")
print(data.groupby("Category")["Sales"].sum())

print("\nAverage sales by region:")
print(data.groupby("Region")["Sales"].mean())

print("\nTotal sales by region:")
print(data.groupby("Region")["Sales"].sum())
```

## Explanation

### 1. Importing Pandas
`import pandas as pd` imports the Pandas library for data analysis and manipulation.

### 2. Loading the Dataset
`pd.read_csv("sales_data.csv")` loads the sales dataset into a DataFrame named `data`.

### 3. Calculating Summary Statistics
`data[["Sales", "Quantity"]].describe()` calculates statistical measures for the Sales and Quantity columns, including:
- Count
- Mean
- Standard deviation
- Minimum
- 25th percentile
- Median (50th percentile)
- 75th percentile
- Maximum

### 4. Total Sales by Category
`data.groupby("Category")["Sales"].sum()` groups the data by product category and calculates the total sales for each category.

### 5. Average Sales by Region
`data.groupby("Region")["Sales"].mean()` groups the data by region and calculates the average sales for each region.

### 6. Total Sales by Region
`data.groupby("Region")["Sales"].sum()` groups the data by region and calculates the total sales for each region.

### 7. Displaying the Results
The `print()` function displays the summary statistics and aggregation results on the screen.

## Sample Output

```text id="yq28z1"
Summary statistics:
              Sales   Quantity
count      6.000000   6.000000
mean   19166.666667   2.833333
std    20157.631140   1.471960
min     3000.000000   1.000000
25%     5500.000000   2.000000
50%    13500.000000   2.500000
75%    23750.000000   3.750000
max    55000.000000   5.000000

Total sales by category:
Category
Electronics    78000
Furniture      37000
Name: Sales, dtype: int64

Average sales by region:
Region
East      7000.0
North    22500.0
South    29000.0
West      5000.0
Name: Sales, dtype: float64

Total sales by region:
Region
East      7000
North    45000
South    58000
West      5000
Name: Sales, dtype: int64
```

**Note:** The sample output is based on the six-row `sales_data.csv` dataset used in the earlier experiment. Your output may differ if your dataset contains different records.

## Result
Thus, summary statistics were calculated, and sales data was successfully aggregated by category and region using Pandas statistical and grouping functions.

## Applications
- Analyzing total sales across product categories.
- Comparing sales performance across regions.
- Calculating average sales and quantities.
- Identifying high-performing categories and regions.
- Preparing summarized datasets for charts and dashboards.

