import pandas as pd
from pandas import DataFrame
import chardet

def read_and_trim_csv(filename: str):
    encodings_to_try = ['utf-8', 'latin-1', 'windows-1253']
    
    for encoding in encodings_to_try:
        try:
            cdf = pd.read_csv(filename, encoding=encoding)
            for column in cdf.columns:
                cdf[column] = cdf[column].astype(str).str.replace(r'\W', "")
            return cdf  # Return the cleaned DataFrame if successfully read
        except UnicodeDecodeError:
            continue
    
        raise Exception("Unable to read the CSV file with supported encodings.")

    return(cdf)

# Given a list of file names this function will read and trim all the given files
def clean_files(files: list[str]):
    cleaned_files: list[str] = []
    # Loop through selected files and process them
    for filename in files:
        try:
            cleaned_df = read_and_trim_csv(filename)
            cleaned_files.append(cleaned_df)  # Append cleaned DataFrame to the list
            
        except Exception as e:
            print(f"Error processing {filename}: {e}")
            continue

    return cleaned_files  # Return the list of cleaned DataFrames

def get_dataframes(self, files: list[str]):
    data_df: list[DataFrame] = []
    data_df.extend(clean_files(files))
    return(data_df)


def get_headers(self, files: list[str]):
    headers: list[str] = []
    data_df: list[DataFrame] = []
    data_df.extend(get_dataframes(self,files))
    for df in data_df: headers.extend(df.columns.values.tolist())
    return headers
