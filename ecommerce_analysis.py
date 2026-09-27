import pandas as pd

df = pd.read_csv("ecommerce_sales.csv")
df["Order_Date"] = pd.to_datetime(df["Order_Date"])
df["Revenue"] = df["Quantity"] * df["Unit_Price"]

print("===== E-COMMERCE DATA ANALYSIS =====")
print(f"\nTotal Revenue: ₹{df['Revenue'].sum():,.0f}")
print(f"Total Orders: {df['Order_ID'].nunique()}")
print(f"Total Quantity Sold: {df['Quantity'].sum()}")

order_totals = df.groupby("Order_ID")["Revenue"].sum()
print(f"Average Order Value: ₹{order_totals.mean():,.2f}")

category_revenue = df.groupby("Category")["Revenue"].sum().sort_values(ascending=False)
city_revenue = df.groupby("City")["Revenue"].sum().sort_values(ascending=False)
product_revenue = df.groupby("Product")["Revenue"].sum().sort_values(ascending=False)

print("\nRevenue by Category:\n", category_revenue)
print("\nRevenue by City:\n", city_revenue)
print("\nRevenue by Product:\n", product_revenue)

df["Month"] = df["Order_Date"].dt.to_period("M")
monthly_revenue = df.groupby("Month")["Revenue"].sum()
print("\nMonthly Revenue:\n", monthly_revenue)

print(f"\nTop Revenue Product: {product_revenue.idxmax()}")
print(f"Top Revenue City: {city_revenue.idxmax()}")

category_revenue.to_csv("category_revenue_summary.csv", header=["Revenue"])
city_revenue.to_csv("city_revenue_summary.csv", header=["Revenue"])
product_revenue.to_csv("product_revenue_summary.csv", header=["Revenue"])
monthly_revenue.to_csv("monthly_revenue_summary.csv", header=["Revenue"])
