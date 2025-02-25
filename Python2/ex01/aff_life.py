from load_csv import load
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    try:
        path = '../life_expectancy_years.csv'
        csv_data = load(path)
        country = 'Canada'
        country_row = csv_data[csv_data['country'] == country]
    
        if not country_row.empty:
            print(country_row)
        else:
            print(f"Country '{country}' not found in the dataset.")

        x = np.array(csv_data.columns[1:])
        y = country_row.iloc[0, 1:].values

        plt.title(f"Life Expectancy in {country} (1800-2100)") 
        plt.xlabel("Year") 
        plt.ylabel("Life Expectancy (years)") 
        plt.plot(x, y, color="green", label=country) 
        xticks = x[::40]
        plt.xticks(xticks, rotation=45)  
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