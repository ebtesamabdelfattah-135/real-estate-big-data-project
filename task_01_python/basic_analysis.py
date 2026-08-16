import pandas as pd

file_path = r"D:\BigData Project\Transactions.csv"

chunk_size = 100_000

total_rows = 0
total_actual_worth = 0
max_actual_worth = 0
min_actual_worth = None

total_area = 0
area_count = 0

for chunk in pd.read_csv(file_path, chunksize=chunk_size):

    # Number of rows
    total_rows += len(chunk)

    # Actual worth
    total_actual_worth += chunk["actual_worth"].sum()

    chunk_max = chunk["actual_worth"].max()
    if chunk_max > max_actual_worth:
        max_actual_worth = chunk_max

    chunk_min = chunk["actual_worth"].min()

    if min_actual_worth is None or chunk_min < min_actual_worth:
        min_actual_worth = chunk_min

    # Procedure area
    total_area += chunk["procedure_area"].sum()
    area_count += chunk["procedure_area"].count()


# Calculate averages
average_actual_worth = total_actual_worth / total_rows
average_area = total_area / area_count


print("========== BASIC ANALYSIS ==========")

print("Total Transactions:", total_rows)

print("Total Actual Worth:", total_actual_worth)

print("Average Actual Worth:", average_actual_worth)

print("Maximum Actual Worth:", max_actual_worth)

print("Minimum Actual Worth:", min_actual_worth)

print("Average Procedure Area:", average_area)