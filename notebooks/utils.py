import pandas as pd
import requests
import io

def download_and_save_df(url, file_path, extention=".csv"):
    """
    Download a file from a URL and save it locally.
    
    Parameters:
    -----------
    url : str
        URL to download the file from
    file_path : str
        Local file path where the file will be saved
    extention : str, default ".csv"
        File extension (.csv, .parquet, or .xlsx)
    
    Returns:
    --------
    pd.DataFrame
        The loaded dataframe
    """
    # Normalize extension (ensure it starts with a dot and is lowercase)
    if not extention.startswith("."):
        extention = "." + extention
    extention = extention.lower()
    
    # Download the file
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad status codes
    
    # Read based on file extension
    if extention == ".csv":
        df = pd.read_csv(io.StringIO(response.text))
    elif extention == ".parquet":
        df = pd.read_parquet(io.BytesIO(response.content))
    elif extention == ".xlsx":
        df = pd.read_excel(io.BytesIO(response.content))
    else:
        raise ValueError(f"Unsupported file extension: {extention}. Supported: .csv, .parquet, .xlsx")
    
    # Save the file
    if extention == ".csv":
        df.to_csv(file_path, index=False)
    elif extention == ".parquet":
        df.to_parquet(file_path, index=False)
    elif extention == ".xlsx":
        df.to_excel(file_path, index=False)
    
    return df
    
def download_and_save_csv(url, file_path):
    """
    Download a CSV file from a URL and save it locally.
    
    Parameters:
    -----------
    url : str
        URL to download the CSV file from
    file_path : str
        Local file path where the CSV file will be saved

    Returns:
    --------
    None
        Saves the CSV file locally
    """
    response = requests.get(url)
    response.raise_for_status()

    df = pd.read_csv(io.StringIO(response.text))

    df.to_csv(file_path, index=False) 


def age_group_label(age, minor_threshold=30, senior_threshold=60):
    if age < minor_threshold:
        return "Minor"
    elif age < senior_threshold - 1:
        return "Middle-aged"
    else:
        return "Senior"


def income_band(income, low=80000, high=170000):
    if income < low:
        return "Low"
    elif income <= high:
        return "Medium"
    else:
        return "High"
    

def get_dependant_category(n_dependants):
    if n_dependants == 0:
        return "No dependants"
    elif n_dependants <= 2:
        return "Small family"
    else:
        return "Large family"
    
def set_senior_flag(age):
        return 'Senior' if age >= 60 else 'Non-Senior'


def capitalize_words(s):
    """Return a string with each word's first letter uppercase."""
    if s is None:
        return s
    return " ".join(word.capitalize() for word in str(s).split())
    
