import pandas as pd

file_path = r"D:\BigData Project\Transactions.csv"

chunk_size = 100_000

total_rows = 0

for chunk in pd.read_csv(file_path, chunksize=chunk_size):
    total_rows += len(chunk)

print("Total number of rows:", total_rows)