# Experiment No. 1: Introduction to Various Data Visualization Tools

## Aim
To display the installed versions of commonly used Python data visualization and data analysis libraries, such as Matplotlib, Seaborn, Plotly, and Pandas.

## Algorithm
1. Start the program.
2. Import the Matplotlib, Seaborn, Plotly, and Pandas libraries.
3. Access the `__version__` attribute of each library.
4. Display the installed version of each library using the `print()` function.
5. Stop the program.

## Description
Data visualization is the process of representing data in graphical formats such as charts, graphs, and plots. Python provides several libraries for data visualization and analysis.

- **Matplotlib:** Used to create graphs, charts, and plots.
- **Seaborn:** Used to create attractive statistical visualizations.
- **Plotly:** Used to create interactive charts and graphs.
- **Pandas:** Used for data manipulation, analysis, and handling tabular data.

Checking the installed versions of these libraries helps verify the Python environment and identify which versions are available for use.

## Program

```python
# Experiment No. 1: Introduction to Various Data Visualization Tools
# Aim: Display installed versions of commonly used Python visualization libraries.

import matplotlib
import seaborn
import plotly
import pandas

print("Matplotlib:", matplotlib.__version__)
print("Seaborn:", seaborn.__version__)
print("Plotly:", plotly.__version__)
print("Pandas:", pandas.__version__)
```

## Explanation
1. `import matplotlib`: Imports the Matplotlib library.
2. `import seaborn`: Imports the Seaborn library.
3. `import plotly`: Imports the Plotly library.
4. `import pandas`: Imports the Pandas library.
5. `__version__`: Returns the installed version of the respective library.
6. `print()`: Displays the library name and its installed version on the screen.

## Sample Output

```text
Matplotlib: 3.x.x
Seaborn: 0.x.x
Plotly: 5.x.x
Pandas: 2.x.x
```



## Result
Thus, the installed versions of the commonly used Python libraries Matplotlib, Seaborn, Plotly, and Pandas were successfully displayed.

