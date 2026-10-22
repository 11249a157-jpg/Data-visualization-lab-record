# Experiment No. 1: Introduction to Various Data Visualization Tools

## Aim
To explore commonly used data visualization tools and verify the installed versions of important Python libraries used for data analysis and graphical representation.

## Description
Data visualization is the process of representing data through visual formats such as charts, graphs, maps, and dashboards. It helps users understand complex information, compare values, identify patterns, and draw meaningful conclusions.

Data visualization is widely used in education, business, healthcare, research, and finance. Python provides several libraries for creating visualizations, while tools such as Tableau and Power BI are used to develop interactive dashboards and reports.

## Applications of Data Visualization
- Simplifies the interpretation of large datasets.
- Helps compare values across different categories.
- Identifies trends, patterns, and unusual observations.
- Presents analytical findings clearly.
- Supports informed decision-making.
- Helps monitor business and organizational performance.

## Algorithm
1. Start the Python program.
2. Import Matplotlib, Seaborn, Plotly, and Pandas.
3. Retrieve the version information of each library.
4. Display the library names and their installed versions.
5. Verify the displayed output.
6. Stop the program.

## Program

```python
import matplotlib
import seaborn
import plotly
import pandas

print("Matplotlib Version:", matplotlib.__version__)
print("Seaborn Version:", seaborn.__version__)
print("Plotly Version:", plotly.__version__)
print("Pandas Version:", pandas.__version__)
```

## Program Explanation

- **Matplotlib:** A Python library used to create line graphs, bar charts, histograms, and scatter plots.
- **Seaborn:** A statistical visualization library that provides attractive charts and convenient plotting functions.
- **Plotly:** A library used to create interactive graphs and charts.
- **Pandas:** A library used for loading, organizing, cleaning, and analyzing structured data.
- **`__version__`:** An attribute that returns the installed version of a Python library.

The program imports the four libraries and displays their installed version numbers. If all the libraries are installed correctly, their version details appear in the console.

## Common Python Visualization Libraries

| Library | Purpose |
|---|---|
| Matplotlib | Creates static charts and graphs. |
| Seaborn | Creates statistical visualizations. |
| Plotly | Develops interactive charts and graphs. |
| Pandas | Organizes and analyzes tabular data. |

## Introduction to Data Analytics Using Python

Data analytics is the process of examining data to discover useful information, identify problems, and support decision-making. Data can be collected from business transactions, educational institutions, healthcare systems, websites, and social media platforms.

The data analytics process generally includes data collection, data cleaning, data processing, analysis, visualization, and interpretation. Python is widely used for these activities because it provides libraries for data manipulation, statistical analysis, and visualization.

Organizations use data analytics to understand customer preferences, monitor performance, identify business opportunities, and improve operations.

### Types of Data Analytics

1. **Descriptive Analytics:** Explains what happened by summarizing historical data.
2. **Diagnostic Analytics:** Investigates why an event occurred.
3. **Predictive Analytics:** Uses historical data and analytical models to estimate future outcomes.
4. **Prescriptive Analytics:** Recommends possible actions to achieve desired results.

These types of analytics can be combined to understand past performance, identify causes of problems, predict future trends, and make better decisions.

## Data Measurement Scales

Data can be classified into four measurement scales:

- **Nominal Scale:** Classifies data into categories without a natural order, such as product type or region.
- **Ordinal Scale:** Represents categories with a meaningful order, such as low, medium, and high.
- **Interval Scale:** Has equal intervals between values but no absolute zero, such as temperature measured in Celsius.
- **Ratio Scale:** Has equal intervals and a meaningful zero, such as sales revenue, distance, and quantity.

Understanding measurement scales helps determine the appropriate methods for analyzing and visualizing data.

## Data Visualization Tools

Several tools are available for analyzing and presenting data:

- **Matplotlib:** A Python library for creating static charts and graphs.
- **Seaborn:** A Python library for statistical data visualization.
- **Plotly:** A library for creating interactive visualizations.
- **Tableau:** A visual analytics platform for creating dashboards and reports.
- **Power BI:** A business intelligence tool for analyzing and presenting information.
- **Google Looker Studio:** A tool for creating reports and dashboards.
- **Microsoft Excel:** A spreadsheet application that supports charts and data analysis.
- **Jupyter Notebook:** An interactive environment for writing Python code, documenting analysis, and displaying visualizations.

The choice of tool depends on the dataset, analysis requirements, level of interactivity, and intended audience.

## Major Areas of Data Analytics

Data analytics involves several related disciplines:

- **Statistics:** Summarizes data and studies relationships between variables.
- **Data Mining:** Identifies useful patterns in large datasets.
- **Business Intelligence:** Converts organizational data into reports and performance insights.
- **Data Visualization:** Presents information through charts, graphs, and dashboards.
- **Simulation:** Examines possible outcomes under different conditions.
- **Modelling and Optimization:** Represents problems mathematically and identifies effective solutions.
- **What-if Analysis:** Studies how changes in input values may affect outcomes.

### Basic Predictive Analytics Workflow

Historical Data → Predictive Algorithm → Trained Model

New Data → Trained Model → Predicted Outcome

A predictive model learns patterns from historical data and uses them to estimate outcomes for new data. Its performance should be evaluated to determine how reliable its predictions are.

## Role of Data Professionals

A **data analyst** collects, cleans, analyzes, and visualizes data to communicate useful findings. A **data scientist** may additionally develop statistical models and machine learning systems for advanced analysis and prediction.

Both roles require analytical thinking, programming skills, problem-solving abilities, and clear communication.

## Sample Output

```text
Matplotlib Version: [installed version]
Seaborn Version: [installed version]
Plotly Version: [installed version]
Pandas Version: [installed version]
```

Note: The actual version numbers depend on the libraries installed on the computer running the program.

## Result

The program was designed to import Matplotlib, Seaborn, Plotly, and Pandas and display their installed version numbers. The experiment also introduced common data visualization tools, the fundamentals of data analytics, measurement scales, and the major types of analytical methods.

Thus, Python libraries provide a useful foundation for preparing, analyzing, and visually presenting data.
