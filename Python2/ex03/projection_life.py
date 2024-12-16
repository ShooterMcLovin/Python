from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt

def main():
    # File paths for the data
    path1 = "../income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
    path2 = "../life_expectancy_years.csv"
    
    # Load the GDP per capita data (income data)
    try:
        data1 = load(path1)
        print(f"Loaded {path1} successfully.")
    except FileNotFoundError:
        print(f"Error: The file at path '{path1}' was not found.")
        return
    except pd.errors.EmptyDataError:
        print(f"Error: The file at path '{path1}' is empty.")
        return
    except pd.errors.ParserError:
        print(f"Error: The file at path '{path1}' is not a valid CSV file or is malformed.")
        return
    except Exception as e:
        print(f"Error: {e}")
        return
    
    # Load the life expectancy data
    try:
        data2 = load(path2)
        print(f"Loaded {path2} successfully.")
    except FileNotFoundError:
        print(f"Error: The file at path '{path2}' was not found.")
        return
    except pd.errors.EmptyDataError:
        print(f"Error: The file at path '{path2}' is empty.")
        return
    except pd.errors.ParserError:
        print(f"Error: The file at path '{path2}' is not a valid CSV file or is malformed.")
        return
    except Exception as e:
        print(f"Error: {e}")
        return
    
    # Extract data for the year 1900 from the life expectancy dataset
    try:
        life_expectancy_1900 = data2[['country', '1900']].dropna()
        life_expectancy_1900.columns = ['Country', 'Life_Expectancy']  # Rename columns for easier handling
    except KeyError as e:
        print(f"Error: Missing expected columns in the life expectancy data: {e}")
        return
    
    # Extract data for the year 1900 from the GDP dataset
    try:
        gdp_1900 = data1[['country', '1900']].dropna()
        gdp_1900.columns = ['Country', 'GDP_per_capita']  # Rename columns for easier handling
    except KeyError as e:
        print(f"Error: Missing expected columns in the GDP data: {e}")
        return
    
    # Merge the life expectancy and GDP data on 'Country'
    try:
        merged_data = pd.merge(life_expectancy_1900, gdp_1900, on='Country', how='inner')
    except KeyError as e:
        print(f"Error: Missing 'Country' column in one or both datasets: {e}")
        return
    
    # Check if merged data is empty
    if merged_data.empty:
        print("No matching countries found for the year 1900.")
        return
    
    # Plot the projection: Life Expectancy vs GDP per Capita for 1900
    plt.figure(figsize=(10, 6))
    plt.scatter(merged_data['GDP_per_capita'], merged_data['Life_Expectancy'], color='b', label='1900 Data')
    
    # Add titles and labels
    plt.title('Life Expectancy vs GDP per Capita in 1900')
    plt.xlabel('GDP per Capita (PPP, inflation adjusted)')
    plt.ylabel('Life Expectancy (Years)')
    
    # Add a legend
    plt.legend()
    
    # Show the plot
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
