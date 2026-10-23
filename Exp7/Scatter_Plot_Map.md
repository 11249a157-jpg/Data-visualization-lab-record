# Experiment No. 7: Creating Scatter Plot Maps in Tableau

## Aim
To create a scatter plot map in Tableau Public using geographic sales data containing latitude, longitude, category, region, and sales information.

## Algorithm
1. Start the program.
2. Import the Pandas library.
3. Create a dataset containing geographic coordinates, product categories, regions, and sales values.
4. Save the dataset as `sales_map_data.csv`.
5. Open Tableau Public and connect to the generated CSV file.
6. Drag Longitude to Columns and Latitude to Rows.
7. Set the mark type to Circle, if required.
8. Drag Category or Region to Color on the Marks Card.
9. Drag Sales to Size on the Marks Card.
10. Review the scatter plot map and save the workbook.
11. Stop the experiment.

## Description
Tableau Public is a data visualization tool used to create interactive charts, maps, and dashboards.

A scatter plot map displays geographic locations using latitude and longitude coordinates. In this experiment, a Python program generates sample sales data containing geographic coordinates. The CSV file is then imported into Tableau to create a map.

The visualization uses:
- **Latitude:** Represents the north–south position.
- **Longitude:** Represents the east–west position.
- **Category or Region:** Distinguishes locations using colors.
- **Sales:** Represents sales values using different-sized circles.

## Program

Save the following Python code as `experiment7.py`.

```python
# Experiment No. 7: Creating Scatter Plot Maps in Tableau
# Aim: Generate geographic sales data for Tableau visualization.

import pandas as pd

# Create geographic sales dataset
data = {
    "Location": ["Chennai", "Bengaluru", "Hyderabad",
                 "Mumbai", "Delhi"],
    "Latitude": [13.0827, 12.9716, 17.3850,
                 19.0760, 28.6139],
    "Longitude": [80.2707, 77.5946, 78.4867,
                  72.8777, 77.2090],
    "Category": ["Electronics", "Furniture",
                 "Electronics", "Furniture",
                 "Electronics"],
    "Region": ["South", "South", "South",
               "West", "North"],
    "Sales": [55000, 25000, 40000, 35000, 60000]
}

# Convert dictionary into a DataFrame
df = pd.DataFrame(data)

# Save dataset as CSV
df.to_csv("sales_map_data.csv", index=False)

# Display the dataset
print("Geographic Sales Dataset:")
print(df)

print("\nDataset saved successfully as sales_map_data.csv")
```

## Explanation

1. **Import Pandas:** The Pandas library is used to create and manage tabular data.
2. **Create the dataset:** A dictionary stores location names, latitude, longitude, category, region, and sales values.
3. **Create a DataFrame:** `pd.DataFrame(data)` converts the dictionary into a table.
4. **Save the CSV file:** `df.to_csv()` saves the dataset as `sales_map_data.csv`.
5. **Display the dataset:** `print(df)` displays the generated records.

## Procedure in Tableau
1. Run `experiment7.py` to generate `sales_map_data.csv`.
2. Open Tableau Public.
3. Under Connect, select **Text File** and open `sales_map_data.csv`.
4. Open a new worksheet.
5. Drag `Longitude` to Columns and `Latitude` to Rows.
6. Choose **Circle** in the Marks Card, if necessary.
7. Drag `Category` or `Region` to **Color**.
8. Drag `Sales` to **Size**.
9. Optionally, drag `Location` to **Detail** or **Label** to identify each point.
10. Review the map and save or publish the workbook.

## Sample Output

```text
Geographic Sales Dataset:
    Location  Latitude  Longitude      Category Region  Sales
0    Chennai   13.0827    80.2707   Electronics  South  55000
1  Bengaluru   12.9716    77.5946     Furniture  South  25000
2  Hyderabad   17.3850    78.4867   Electronics  South  40000
3     Mumbai   19.0760    72.8777     Furniture   West  35000
4      Delhi   28.6139    77.2090   Electronics  North  60000

Dataset saved successfully as sales_map_data.csv
```

**Tableau output:** A geographic visualization showing five locations in India. The colors distinguish product categories or regions, and the circle sizes represent sales values.

## Result
Thus, a geographic sales dataset was generated using Python and imported into Tableau Public to create a scatter plot map based on latitude, longitude, category, region, and sales values.

## Applications
- Geographic sales analysis.
- Regional business performance comparison.
- Location-based data visualization.
- Identification of high-sales locations.
- Preparation of interactive business dashboards.

