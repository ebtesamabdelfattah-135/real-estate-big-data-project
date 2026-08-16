import pandas as pd

file_path = r"D:\BigData Project\Transactions.csv"
chunk_size = 100_000

results = []

for chunk in pd.read_csv(file_path, chunksize=chunk_size):

    chunk = chunk.dropna(
        subset=["property_type_en", "actual_worth"]
    )

    grouped = chunk.groupby("property_type_en").agg(
        transaction_count=("transaction_id", "count"),
        total_value=("actual_worth", "sum"),
        minimum_value=("actual_worth", "min"),
        maximum_value=("actual_worth", "max")
    ).reset_index()

    results.append(grouped)


# Combine results from all chunks
final_result = pd.concat(results)

# Re-aggregate all chunks
final_result = final_result.groupby(
    "property_type_en"
).agg(
    transaction_count=("transaction_count", "sum"),
    total_value=("total_value", "sum"),
    minimum_value=("minimum_value", "min"),
    maximum_value=("maximum_value", "max")
).reset_index()

# Calculate exact average
final_result["average_value"] = (
    final_result["total_value"]
    / final_result["transaction_count"]
)

# Arrange columns
final_result = final_result[
    [
        "property_type_en",
        "transaction_count",
        "total_value",
        "average_value",
        "minimum_value",
        "maximum_value"
    ]
]

# Sort by number of transactions
final_result = final_result.sort_values(
    "transaction_count",
    ascending=False
)

print("\n===== PROPERTY TYPE ANALYSIS =====")
print(final_result.to_string(index=False))


# Save results
output_file = (
    r"D:\BigData Project\task_01_python"
    r"\results\property_type_analysis.csv"
)

final_result.to_csv(
    output_file,
    index=False
)

print("\nResult saved to:")
print(output_file)
