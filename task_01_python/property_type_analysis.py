import pandas as pd

file_path = r"D:\BigData Project\Transactions.csv"

chunk_size = 100_000

results = []

for chunk in pd.read_csv(file_path, chunksize=chunk_size):

    chunk = chunk.dropna(subset=["property_type_en"])

    grouped = chunk.groupby("property_type_en").agg(
        transaction_count=("transaction_id", "count"),
        total_value=("actual_worth", "sum"),
        average_value=("actual_worth", "mean"),
        maximum_value=("actual_worth", "max"),
        minimum_value=("actual_worth", "min")
    ).reset_index()

    results.append(grouped)

# Combine all chunks
final_result = pd.concat(results)

# Re-aggregate because the same property type can exist in multiple chunks
final_result = final_result.groupby("property_type_en").agg(
    transaction_count=("transaction_count", "sum"),
    total_value=("total_value", "sum")
).reset_index()

# Calculate overall average
average_values = []

for chunk in pd.read_csv(file_path, chunksize=chunk_size):
    chunk = chunk.dropna(subset=["property_type_en"])

    avg = chunk.groupby("property_type_en")["actual_worth"].mean()
    average_values.append(avg)

average_result = pd.concat(average_values)

average_result = average_result.groupby(level=0).mean().reset_index()
average_result.columns = ["property_type_en", "average_value"]

final_result = final_result.merge(
    average_result,
    on="property_type_en"
)

final_result = final_result.sort_values(
    "transaction_count",
    ascending=False
)

print("\n===== PROPERTY TYPE ANALYSIS =====")
print(final_result.to_string(index=False))