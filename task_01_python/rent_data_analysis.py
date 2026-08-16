import pandas as pd

file_path = r"D:\BigData Project\Transactions.csv"

chunk_size = 100_000

results = {}

for chunk in pd.read_csv(file_path, chunksize=chunk_size):

    grouped = chunk.groupby(
        "trans_group_en",
        dropna=False
    ).agg(
        transaction_count=("transaction_id", "count"),
        missing_rent_value=("rent_value", lambda x: x.isna().sum()),
        total_rent_value=("rent_value", "sum")
    ).reset_index()

    for _, row in grouped.iterrows():

        group = row["trans_group_en"]

        if group not in results:
            results[group] = {
                "transaction_count": 0,
                "missing_rent_value": 0,
                "total_rent_value": 0
            }

        results[group]["transaction_count"] += row["transaction_count"]
        results[group]["missing_rent_value"] += row["missing_rent_value"]
        results[group]["total_rent_value"] += row["total_rent_value"]


final_result = pd.DataFrame.from_dict(
    results,
    orient="index"
).reset_index()

final_result = final_result.rename(
    columns={"index": "trans_group_en"}
)

final_result["missing_percentage"] = (
    final_result["missing_rent_value"]
    / final_result["transaction_count"]
    * 100
)

print("\n===== RENT DATA ANALYSIS =====")
print(final_result.to_string(index=False))