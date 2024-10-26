import pandas as pd

# Load the CSV files
# file_1_path = "files/token-hd.csv"
file_2_path = "files/token-neth.csv"
file_3_path = "files/tokendolan.csv"

files = [file_2_path, file_3_path]

# Read the first CSV file
df = pd.read_csv(files[0])

# Assume we're interested in a specific column; let's call it 'column_name'
common_values = set(df['From'])
for file in files[1:]:
    df = pd.read_csv(file)
    current_values = set(df['From'])
    common_values.intersection_update(current_values)

common_values_df = pd.DataFrame(list(common_values), columns=['From'])
print(common_values_df)