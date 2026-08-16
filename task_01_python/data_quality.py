import pandas as pd

file_path = r"D:\BigData Project\Transactions.csv"
chunk_size = 100_000

missing_counts = None
total_rows = 0

for chunk in pd.read_csv(file_path, chunksize=chunk_size):

    total_rows += len(chunk)

    current_missing = chunk.isna().sum()

    if missing_counts is None:
        missing_counts = current_missing
    else:
        missing_counts += current_missing


# Calculate missing percentage
missing_percentage = (missing_counts / total_rows) * 100

result = pd.DataFrame({
    "missing_count": missing_counts,
    "missing_percentage": missing_percentage
})

result = result.sort_values(
    "missing_count",
    ascending=False
)

print("\n===== DATA QUALITY - MISSING VALUES =====")
print("Total Rows:", total_rows)
print()

print(result.to_string())

# Save results
output_file = (
    r"D:\BigData Project\task_01_python"
    r"\results\missing_values.csv"
)

result.to_csv(output_file)

print("\nResult saved to:")
print(output_file)
