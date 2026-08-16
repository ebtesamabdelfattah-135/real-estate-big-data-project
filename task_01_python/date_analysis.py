import pandas as pd

file_path = r"D:\BigData Project\Transactions.csv"

chunk_size = 100_000

year_counts = {}

min_date = None
max_date = None

for chunk in pd.read_csv(
    file_path,
    chunksize=chunk_size,
    usecols=["instance_date"]
):

    dates = pd.to_datetime(
        chunk["instance_date"],
        format="%d-%m-%Y",
        errors="coerce"
)

    # Minimum date
    chunk_min = dates.min()

    if pd.notna(chunk_min):
        if min_date is None or chunk_min < min_date:
            min_date = chunk_min

    # Maximum date
    chunk_max = dates.max()

    if pd.notna(chunk_max):
        if max_date is None or chunk_max > max_date:
            max_date = chunk_max

    # Count transactions by year
    years = dates.dt.year.value_counts()

    for year, count in years.items():

        if pd.notna(year):

            year = int(year)

            if year not in year_counts:
                year_counts[year] = 0

            year_counts[year] += int(count)


result = pd.DataFrame(
    list(year_counts.items()),
    columns=["year", "transaction_count"]
)

result = result.sort_values(
    "year"
)

print("\n===== DATE ANALYSIS =====")

print("Earliest Transaction Date:", min_date)
print("Latest Transaction Date:", max_date)

print("\nTransactions by Year:")
print(result.to_string(index=False))

print(
    "\nYear with Most Transactions:",
    result.loc[
        result["transaction_count"].idxmax(),
        "year"
    ]
)

print(
    "Maximum Transactions:",
    result["transaction_count"].max()
)
