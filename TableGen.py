#calculates the rate of cooling for temperatures at an interval of 1 degrees
#reads csv file with 2 columns t and T
#stores the calculated rate with t and T columns as R column in a seperate file

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

#loading data from the csv fike from the file path in main

def load_data(file_path):
    data = pd.read_csv(file_path)
    # drops rows with NaN or inf values
    #drops rows without any value
    data = data.apply(pd.to_numeric, errors='coerce').dropna()
    x = data['t'].values
    y = data['T'].values
    return x, y

# Calculate slopes at intervals of 1 degree temperature
#returns the time, temperature and rate of the corresponding temperature

def calculate_slopes(x, y, interval=1):
    # Create an interpolation function
    f = interp1d(y, x, kind='linear', fill_value="extrapolate")
    y_new = np.arange(min(y), max(y) + interval, interval)
    x_new = f(y_new)
    
    slopes = np.gradient(x_new, y_new)
    
    return x_new, y_new, slopes

# Main function
def main(file_path, output_path):
    x, y = load_data(file_path)
    if len(x) == 0 or len(y) == 0:
        print("No valid data points to plot.")
        return
    
    # Calculate slopes
    x_new, y_new, slopes = calculate_slopes(x, y)
    
    # Create a DataFrame for the slopes
    slope_data = pd.DataFrame({
        't': x_new,
        'T': y_new,
        'R': slopes
    })
    
    # Save the DataFrame to a CSV file
    slope_data.to_csv(output_path, index=False)
    print(f"Rates saved to {output_path}")
    
    # Plotting the data and connecting the points with a line
    plt.plot(x, y, marker='.', linestyle='-', color='b', label='Cooling curve')
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Cooling Plot')
    plt.show()

# Example usage
if __name__ == "__main__":
    input_file_path = r"D:\1_Melita's official Works\Research\JM\Final works\Tables\5n.csv"  # Use raw string literal
    output_file_path = r"D:\1_Melita's official Works\Research\JM\Final works\newTables\5n.csv"  # Use raw string literal
    main(input_file_path, output_file_path)
