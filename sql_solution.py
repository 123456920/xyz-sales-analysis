import csv
from db_connection import get_connection
from config import OUTPUT_FILE


def fetch_data_sql():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        query = """
        SELECT 
            c.CustomerID AS Customer,
            c.Age,
            i.ItemName AS Item,
            SUM(s.Quantity) AS Quantity
        FROM Customer c
        JOIN Orders o ON c.CustomerID = o.CustomerID
        JOIN Sales s ON o.OrderID = s.OrderID
        JOIN Items i ON s.ItemID = i.ItemID
        WHERE c.Age BETWEEN 18 AND 35
          AND s.Quantity IS NOT NULL
        GROUP BY c.CustomerID, c.Age, i.ItemName
        HAVING SUM(s.Quantity) > 0
        ORDER BY c.CustomerID, i.ItemName;
        """

        cursor.execute(query)
        rows = cursor.fetchall()

        conn.close()
        return rows

    except Exception as e:
        print("SQL Query Error:", e)
        return []


def write_to_csv(data):
    try:
        with open(OUTPUT_FILE, mode="w", newline="") as file:
            writer = csv.writer(file, delimiter=";")
            writer.writerow(["Customer", "Age", "Item", "Quantity"])
            for row in data:
                writer.writerow(row)

        print("✅ CSV file generated successfully!")

    except Exception as e:
        print("CSV Writing Error:", e)


if __name__ == "__main__":
    data = fetch_data_sql()
    write_to_csv(data)