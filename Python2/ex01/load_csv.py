import pandas as pd

def load(path: str):
    """
    Load a CSV file and return its dimensions.
    
    Parameters:
    path (str): The file path to the CSV file.
    
    Returns:
        data from the csv file
    """
    try:
        data = pd.read_csv(path)
        dimensions = data.shape

        print(f"Loading dataset of dimensions {dimensions}")
        print(data.head())  # This will print the first 5 rows by default
        
        return data
    
    except FileNotFoundError:
        print(f"Error: The file at path '{path}' was not found.")
    except pd.errors.EmptyDataError:
        print(f"Error: The file at path '{path}' is empty.")
    except pd.errors.ParserError:
        print(f"Error: The file at path '{path}' is not a valid CSV file or is malformed.")
    except Exception as e:
        print(f"Error: {e}")
    return None
