import pandas as pd

# Path to the dataset
file_path = r"D:\BigData Project\Transactions.csv"

# Read only the first 5 rows
df = pd.read_csv(file_path, nrows=5)

print("===== COLUMNS =====")
print(df.columns.tolist())

print("\n===== FIRST 5 ROWS =====")
print(df)

print("\n===== DATA TYPES =====")
print(df.dtypes)

print("\n===== SHAPE =====")
print(df.shape)