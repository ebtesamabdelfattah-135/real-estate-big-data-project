import pandas as pd
import matplotlib.pyplot as plt

file_path = r"D:\BigData Project\Transactions.csv"

chunk_size = 100_000

year_counts = {}

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

    years = dates.dt.year.value_counts()

    for year, count in years.items():

        if pd.notna(year):

            year = int(year)

            year_counts[year] = (
                year_counts.get(year, 0) + int(count)
            )


result = pd.DataFrame(
    list(year_counts.items()),
    columns=["year", "transaction_count"]
)

result = result.sort_values("year")


plt.figure(figsize=(12, 6))

plt.plot(
    result["year"],
    result["transaction_count"],
    marker="o"
)

plt.title("Real Estate Transactions by Year")
plt.xlabel("Year")
plt.ylabel("Number of Transactions")
plt.xticks(rotation=45)

plt.tight_layout()

output_file = (
    r"D:\BigData Project\task_01_python"
    r"\results\transactions_by_year.png"
)

plt.savefig(output_file, dpi=300)

plt.show()

print("Chart saved to:")
print(output_file)
