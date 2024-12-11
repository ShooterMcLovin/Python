import pandas as pd

def load(path: str):
    """
    Load a CSV file and return its dimensions.
    
    Parameters:
    path (str): The file path to the CSV file.
    
    Returns:
    tuple or None: The dimensions of the dataset as a tuple (rows, columns),
                   or None if there's an error in loading the file.
    """
    try:
        data = pd.read_csv(path)
        
        # Get the dimensions (rows, columns)
        dimensions = data.shape
        
        # Print the dataset shape (dimensions)
        print(f"Loading dataset of dimensions {dimensions}")
        
        # Optionally display the first few rows of the dataset for preview
        print(data.head())  # This will print the first 5 rows by default
        
        # Return the dimensions
        return data
    
    except FileNotFoundError:
        print(f"Error: The file at path '{path}' was not found.")
    except pd.errors.EmptyDataError:
        print(f"Error: The file at path '{path}' is empty.")
    except pd.errors.ParserError:
        print(f"Error: The file at path '{path}' is not a valid CSV file or is malformed.")
    except Exception as e:
        print(f"Error: {e}")
    
    # Return None if there's any error
    return None

