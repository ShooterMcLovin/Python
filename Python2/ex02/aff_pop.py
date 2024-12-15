from load_csv import load
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def convert_population(pop):
    """Converts population values from 'k' and 'M' format to numeric."""
    if type(pop) == str:  # Check if the value is a string
        if pop[-1] == 'k':  # For populations in 'k' (thousands)
            return float(pop[:-1]) * 1000
        elif pop[-1] == 'M':  # For populations in 'M' (millions)
            return float(pop[:-1]) * 1000000
    return float(pop)  # If it's already a number, return it as is

def main():
    try:
        path = '../population_total.csv'  # Path to your CSV file
        csv_data = load(path)  # Load the dataset
        country = 'Canada'
        country2 = 'France'
        
        # Filter the row for the specified countries
        country_row = csv_data[csv_data['country'] == country]
        country_row2 = csv_data[csv_data['country'] == country2]
        
        if not country_row.empty and not country_row2.empty:
            print(f"Data for {country}:")
            print(country_row)
            print(f"Data for {country2}:")
            print(country_row2)
        else:
            print(f"Country '{country}' or '{country2}' not found in the dataset.")
            return

        # Extract years (x) and population data (y)
        x = np.array(csv_data.columns[1:])  # Skip the 'country' column
        y = country_row.iloc[0, 1:].values  # Population values for Canada
        y2 = country_row2.iloc[0, 1:].values  # Population values for France

        # Convert population data from 'k' and 'M' to numeric
        y_converted = [convert_population(pop) for pop in y]
        y_converted2 = [convert_population(pop) for pop in y2]

        # Ensure all population values are numeric
        print(f"Converted population values for {country}: {y_converted}")
        print(f"Converted population values for {country2}: {y_converted2}")

        # Plotting the data
        plt.title(f"Population Comparison: {country} vs {country2} (1800-2100)") 
        plt.xlabel("Year") 
        plt.ylabel("Population (in millions)") 
        
        # Plot the data for both countries
        plt.plot(x, np.array(y_converted) / 1e6, color="green", label=country)  # Convert to millions
        plt.plot(x, np.array(y_converted2) / 1e6, color="blue", label=country2)  # Convert to millions

        # Adjust the x-ticks (show every 40th year)
        xticks = x[::40]
        plt.xticks(xticks, rotation=45)

        # Adjust the y-ticks based on population data range (in billions)
        # yticks = np.linspace(min(np.array(y_converted) / 1e6), max(np.array(y_converted2) / 1e6), 20)  # Dynamic range for y-ticks in millions
        min_y = min(np.array(y_converted) / 1e6)  # Minimum population in millions
        max_y = max(np.array(y_converted2) / 1e6)  # Maximum population in millions
        yticks = np.arange(min_y // 20 * 20, max_y + 20, 20)  # Step by 20M
        # yticks = yticks[::2]

        plt.yticks(yticks, rotation=45)
        
        # Add grid for better readability
        plt.grid(True)

        # Add the legend to differentiate countries
        plt.legend()

        # Show the plot
        plt.tight_layout()
        plt.show()

    except FileNotFoundError:
        print(f"Error: The file at path '{path}' was not found.")
    except pd.errors.EmptyDataError:
        print(f"Error: The file at path '{path}' is empty.")
    except pd.errors.ParserError:
        print(f"Error: The file at path '{path}' is not a valid CSV file or is malformed.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
