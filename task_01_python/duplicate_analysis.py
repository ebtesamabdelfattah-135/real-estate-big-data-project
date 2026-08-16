import pandas as pd

file_path = r"D:\BigData Project\Transactions.csv"
chunk_size = 100_000

seen_ids = set()
duplicate_count = 0
total_rows = 0

for chunk in pd.read_csv(
    file_path,
    chunksize=chunk_size,
    usecols=["transaction_id"]
):

    total_rows += len(chunk)

    for transaction_id in chunk["transaction_id"]:

        if transaction_id in seen_ids:
            duplicate_count += 1
        else:
            seen_ids.add(transaction_id)


print("\n===== DUPLICATE ANALYSIS =====")

print("Total Transactions:", total_rows)

print("Unique Transaction IDs:", len(seen_ids))

print("Duplicate Transaction IDs:", duplicate_count)

duplicate_percentage = (
    duplicate_count / total_rows
) * 100

print(
    "Duplicate Percentage:",
    duplicate_percentage
)