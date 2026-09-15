"""
Pandas Basic Operations — Beginner Practice
Run: python pandas_basic_operations.py
Install: pip install pandas
"""

import pandas as pd


def main():
    print("=" * 50)
    print("PANDAS BASIC OPERATIONS")
    print("=" * 50)

    # 1. Creating DataFrames
    data = {
        "name": ["Manas", "Kunal", "Anant", "Riya", "Amit"],
        "age": [21, 22, 20, 23, 21],
        "city": ["Jamshedpur", "Ranchi", "Patna", "Kolkata", "Bokaro"],
        "salary": [50000, 45000, 40000, 60000, 38000],
    }
    df = pd.DataFrame(data)
    print("\n1. Creating a DataFrame")
    print(df)

    # 2. Inspecting data
    print("\n2. Inspecting Data")
    print("First 3 rows:\n", df.head(3))
    print("Last 2 rows:\n", df.tail(2))
    print("Shape (rows, cols):", df.shape)
    print("Column names:", list(df.columns))
    print("Data types:\n", df.dtypes)
    print("Quick stats:\n", df.describe())

    # 3. Selecting columns & rows
    print("\n3. Selecting Data")
    print("Single column:\n", df["name"])
    print("Multiple columns:\n", df[["name", "salary"]])
    print("Row by label (loc):\n", df.loc[0])
    print("Rows by position (iloc) [0:2]:\n", df.iloc[0:2])

    # 4. Filtering
    print("\n4. Filtering")
    print("Age > 21:\n", df[df["age"] > 21])
    print("City == Jamshedpur:\n", df[df["city"] == "Jamshedpur"])
    print("Salary between 40k-55k:\n", df[df["salary"].between(40000, 55000)])

    # 5. Adding & dropping columns
    print("\n5. Adding / Dropping Columns")
    df["salary_lakhs"] = df["salary"] / 100000
    print("Added salary_lakhs:\n", df[["name", "salary_lakhs"]])
    df = df.drop(columns=["salary_lakhs"])
    print("Dropped it. Columns now:", list(df.columns))

    # 6. Sorting
    print("\n6. Sorting")
    print("By salary (desc):\n", df.sort_values("salary", ascending=False))
    print("By age (asc) then salary (desc):\n", df.sort_values(["age", "salary"], ascending=[True, False])[["name", "age", "salary"]])

    # 7. Grouping & aggregation
    print("\n7. GroupBy & Aggregation")
    print("Mean salary by city:\n", df.groupby("city")["salary"].mean())
    print("Count by age:\n", df.groupby("age")["name"].count())
    print("Multiple aggregations on salary:\n", df.groupby("city")["salary"].agg(["mean", "max", "count"]))

    # 8. Handling missing data
    print("\n8. Missing Data")
    df_missing = df.copy()
    df_missing.loc[1, "salary"] = None
    df_missing.loc[3, "city"] = None
    print("Missing counts:\n", df_missing.isnull().sum())
    filled = df_missing["salary"].fillna(df_missing["salary"].mean())
    print("Salary after fillna(mean):\n", filled)
    print("Rows with any NaN dropped:\n", df_missing.dropna())

    # 9. Applying functions
    print("\n9. Apply / Map")
    df["category"] = df["salary"].apply(lambda x: "High" if x >= 50000 else "Normal")
    print("Salary category:\n", df[["name", "salary", "category"]])
    df["name_upper"] = df["name"].str.upper()
    print("Uppercase names:", df["name_upper"].tolist())

    # 10. Series basics
    print("\n10. Series Basics")
    s = pd.Series([10, 20, 30, 40], index=["a", "b", "c", "d"])
    print("Series:", s.tolist())
    print("Sum:", s.sum(), "| Mean:", s.mean())
    print("Max index:", s.idxmax())

    # 11. Reading / writing files (CSV)
    print("\n11. CSV Round-trip")
    df.to_csv("sample_output.csv", index=False)
    df_read = pd.read_csv("sample_output.csv")
    print("Read back from CSV — same shape?", df_read.shape == df.shape)

    print("\n" + "=" * 50)
    print("Done! Try loading your own CSV with pd.read_csv()")
    print("=" * 50)


if __name__ == "__main__":
    main()
