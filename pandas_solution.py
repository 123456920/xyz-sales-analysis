import pandas as pd
from db_connection import get_connection
from config import OUTPUT_FILE


def fetch_data_pandas():
    try:
        conn = get_connection()

        # Load tables into DataFrames
        customers = pd.read_sql("SELECT * FROM Customer", conn)
        orders = pd.read_sql("SELECT * FROM Orders", conn)
        sales = pd.read_sql("SELECT * FROM Sales", conn)
        items = pd.read_sql("SELECT * FROM Items", conn)

        conn.close()

        # Merge tables (Customer → Orders → Sales → Items)
        df = customers.merge(orders, on="CustomerID") \
                      .merge(sales, on="OrderID") \
                      .merge(items, on="ItemID")

        # Filter age 18-35 and ignore NULL quantities
        df = df[(df["Age"].between(18, 35)) & (df["Quantity"].notna())]

        # Group and sum
        result = df.groupby(
            ["CustomerID", "Age", "ItemName"],
            as_index=False
        )["Quantity"].sum()

        # Remove zero totals
        result = result[result["Quantity"] > 0]

        # Rename columns to required format
        result.columns = ["Customer", "Age", "Item", "Quantity"]

        # Sort like SQL output
        result = result.sort_values(["Customer", "Item"])

        return result

    except Exception as e:
        print("Pandas Processing Error:", e)
        return pd.DataFrame()


def write_to_csv(df):
    try:
        df.to_csv(OUTPUT_FILE, sep=";", index=False)
        print("✅ Pandas CSV generated successfully!")
    except Exception as e:
        print("CSV Writing Error:", e)


if __name__ == "__main__":
    df = fetch_data_pandas()
    write_to_csv(df)