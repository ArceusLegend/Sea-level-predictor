import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('numpy_pandas\data\epa-sea-level.csv')

    # Extract the year portion from the 'Year' column
    # Will make the x axis of our plot cleaner as it won't be as cluttered
    df['Year'] = pd.to_datetime(df['Year']).dt.year

    # Create a single figure
    plt.figure(figsize=(12, 6)) 

    # Create scatter plot

    # 'Year' is the x axis, 'CSIRO Adjusted Sea Level' is the y axis
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], s=10, c='blue', alpha=0.5, label='Sea Level Data')

    # First line of best fit (1880-2050)

    # Calculate linear regression
    slope, intercept, r, p, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Make line range go to 2050
    years = range(1880, 2050)

    # Plot the line of best fit
    plt.plot(years, slope * years + intercept, '-',
              color='red', label='First prediction (1880-2050)')
    
    # Second line of best fit (2000-2050)

    # Pass all data from 2000- to a new dataframe and repeat the same steps as the first line
    df_2 = df.loc[df['Year'] >= 2000].reset_index().drop('index', axis=1)

    # Calculate linear regression
    slope2, intrcpt2, r2, p2, std_err2 = linregress(df_2['Year'], df_2['CSIRO Adjusted Sea Level'])

    # Extend second line to 2050
    range2 = range(2000, 2050)

    # Plot the second line
    plt.plot(range2, slope2 * range2 + intrcpt2, 'y--', label='Second prediction (2000-2050)')

    # Add title and labels
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')

    # Add legend and grid to the plot
    plt.legend()  
    plt.grid()

    # Show the plot
    plt.show()


draw_plot()