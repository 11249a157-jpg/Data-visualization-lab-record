# Experiment No. 5: Connecting to Data and Preparing Data for Visualization

## Aim
To load, inspect, clean, and save a CSV dataset using Python and the Pandas library in preparation for data visualization.

## Algorithm
1. Start the program.
2. Import the Pandas library.
3. Load the `sales_data.csv` file using the `pd.read_csv()` function.
4. Display the first five rows of the dataset using `data.head()`.
5. Identify and display missing values in each column using `data.isnull().sum()`.
6. Remove duplicate rows using `data.drop_duplicates()`.
7. Convert the `Sales` column into a numeric data type using `pd.to_numeric()` with `errors="coerce"`.
8. Remove rows containing missing or invalid values in the `Sales` column using `data.dropna()`.
9. Save the cleaned dataset as `cleaned_sales_data.csv` using `data.to_csv()`.
10. Display a success message.
11. Stop the program.

## Description
Data preparation is an important step in data analysis and visualization. It involves loading data, examining its structure, identifying missing values, removing duplicate records, correcting data types, and saving the cleaned dataset.

The Pandas library provides functions for handling tabular data efficiently.

- **CSV Loading:** Reads data from a comma-separated values file.
- **Data Inspection:** Displays the first five rows to understand the structure of the dataset.
- **Missing Value Detection:** Identifies empty or missing values in each column.
- **Duplicate Removal:** Eliminates duplicate rows to improve data quality.
- **Data Type Conversion:** Converts the Sales column into numeric values.
- **Missing Value Removal:** Removes rows where the Sales value is missing or invalid.
- **Data Export:** Saves the cleaned dataset to a new CSV file for further analysis and visualization.

The cleaned dataset can subsequently be imported into tools such as Tableau or Orange.

## Program

```python
# Experiment No. 5: Connecting to Data and Preparing Data for Visualization
# Aim: Load, inspect, clean and save a CSV dataset.

import pandas as pd

data = pd.read_csv("sales_data.csv")

print("First five rows:")
print(data.head())

print("\nMissing values:")
print(data.isnull().sum())

data = data.drop_duplicates()
data["Sales"] = pd.to_numeric(data["Sales"], errors="coerce")
data = data.dropna(subset=["Sales"])

data.to_csv("cleaned_sales_data.csv", index=False)

print("\nData prepared successfully.")
```

## Explanation

### 1. Importing Pandas
`import pandas as pd` imports the Pandas library and assigns it the alias `pd`.

### 2. Loading the Dataset
`pd.read_csv("sales_data.csv")` reads the sales dataset and stores it in a DataFrame named `data`.

### 3. Displaying the First Five Rows
`data.head()` displays the first five rows of the dataset, helping us understand its contents.

### 4. Checking Missing Values
`data.isnull().sum()` counts the missing values in each column and displays the results.

### 5. Removing Duplicate Records
`data.drop_duplicates()` removes duplicate rows from the dataset.

### 6. Converting Sales into Numeric Values
`pd.to_numeric(data["Sales"], errors="coerce")` converts valid Sales values into numbers and replaces invalid values with missing values.

### 7. Removing Missing Sales Values
`data.dropna(subset=["Sales"])` removes rows where the Sales column contains missing or invalid values.

### 8. Saving the Cleaned Dataset
`data.to_csv("cleaned_sales_data.csv", index=False)` saves the cleaned data to a new CSV file without including the DataFrame index as an extra column.

### 9. Displaying the Success Message
`print("\nData prepared successfully.")` displays a message indicating that the script has completed its processing steps.

## Sample Output

```text
First five rows:
       Product Region  OrderID     Category  Sales  Quantity
0       Laptop  South      101  Electronics  55000         2
1       Mobile  North      102  Electronics  20000         3
2        Chair   West      103    Furniture   5000         5
3        Table   East      104    Furniture   7000         2
4   Headphones  South      105  Electronics   3000         4

Missing values:
Product     0
Region      0
OrderID     0
Category    0
Sales       0
Quantity    0
dtype: int64

Data prepared successfully.
```

**Note:** This sample output assumes the six-row sales dataset has the columns shown above and contains no missing or duplicate values. Your actual output depends on your CSV file.

## Result
Thus, the sales dataset was successfully loaded, inspected, cleaned by removing duplicate rows and invalid Sales values, and saved as `cleaned_sales_data.csv` for further data visualization.

## Applications
- Preparing datasets for visualization.
- Improving data quality and consistency.
- Detecting missing and invalid values.
- Removing duplicate records.
- Preparing CSV files for Tableau, Orange, and other data analysis tools.

