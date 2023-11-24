import pandas as pd

def scrape_excel_file(file_path, sheet_name):
    try:
        # Read Excel file into a pandas DataFrame
        df = pd.read_excel(file_path, sheet_name=sheet_name)

        # Display the DataFrame (optional)
        print("Data from Excel file:")
        print(df)

        # You can now process or manipulate the data as needed
        # For example, you can access specific columns like this:
        # column_data = df['Column_Name']

        # Or iterate through rows:
        # for index, row in df.iterrows():
        #     print(row['Column_Name'])

    except Exception as e:
        print(f"Error reading Excel file: {e}")

# Example usage
file_path = "path/to/your/excel/file.xlsx"  # Change this to your actual file path
sheet_name = "Sheet1"  # Change this to the name of your sheet

scrape_excel_file(file_path, sheet_name)
