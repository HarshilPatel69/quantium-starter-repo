import pandas as pd

input_files = [
    "data/daily_sales_data_0.csv",
    "data/daily_sales_data_1.csv",
    "data/daily_sales_data_2.csv",
]

all_data = pd.concat([pd.read_csv(file) for file in input_files])

pink_only = all_data[all_data["product"] == "pink morsel"]

prices = pink_only["price"].str.replace("$", "", regex=False).astype(float)

sales = prices * pink_only["quantity"]

output = pd.DataFrame({
    "Sales": sales,
    "Date": pink_only["date"],
    "Region": pink_only["region"],
})

output.to_csv("formatted_sales_data.csv", index=False)

print("Done! Wrote", len(output), "rows to formatted_sales_data.csv")
