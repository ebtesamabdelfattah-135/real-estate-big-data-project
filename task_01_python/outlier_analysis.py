import pandas as pd

file_path = r"D:\BigData Project\Transactions.csv"

chunk_size = 100_000

values = []

for chunk in pd.read_csv(
    file_path,
    chunksize=chunk_size,
    usecols=["actual_worth"]
):
    values.extend(
        chunk["actual_worth"]
        .dropna()
        .tolist()
    )

series = pd.Series(values)

Q1 = series.quantile(0.25)
Q3 = series.quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = series[
    (series < lower_bound) |
    (series > upper_bound)
]

print("\n===== OUTLIER ANALYSIS =====")

print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)

print("Lower Bound:", lower_bound)
print("Upper Bound:", upper_bound)

print("Total Valid Values:", len(series))

print("Number of Outliers:", len(outliers))

print(
    "Outlier Percentage:",
    (len(outliers) / len(series)) * 100
)

print("Minimum Value:", series.min())
print("Maximum Value:", series.max())
