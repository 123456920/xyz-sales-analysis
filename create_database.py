import sqlite3

def create_database():
    conn = sqlite3.connect("data/company_xyz.db")
    cursor = conn.cursor()

    # Drop tables if exist
    cursor.execute("DROP TABLE IF EXISTS Sales")
    cursor.execute("DROP TABLE IF EXISTS Orders")
    cursor.execute("DROP TABLE IF EXISTS Customer")
    cursor.execute("DROP TABLE IF EXISTS Items")

    # Create tables
    cursor.execute("""
    CREATE TABLE Customer (
        CustomerID INTEGER PRIMARY KEY,
        Age INTEGER
    )
    """)

    cursor.execute("""
    CREATE TABLE Orders (
        OrderID INTEGER PRIMARY KEY,
        CustomerID INTEGER,
        FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
    )
    """)

    cursor.execute("""
    CREATE TABLE Items (
        ItemID INTEGER PRIMARY KEY,
        ItemName TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE Sales (
        SalesID INTEGER PRIMARY KEY,
        OrderID INTEGER,
        ItemID INTEGER,
        Quantity INTEGER,
        FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
        FOREIGN KEY (ItemID) REFERENCES Items(ItemID)
    )
    """)

    # Insert Items
    cursor.executemany("INSERT INTO Items VALUES (?,?)", [
        (1, 'x'),
        (2, 'y'),
        (3, 'z')
    ])

    # Insert Customers
    cursor.executemany("INSERT INTO Customer VALUES (?,?)", [
        (1, 21),
        (2, 23),
        (3, 35),
        (4, 40)  # outside age range
    ])

    # Insert Orders
    cursor.executemany("INSERT INTO Orders VALUES (?,?)", [
        (1,1),
        (2,1),
        (3,2),
        (4,3),
        (5,4)
    ])

    # Insert Sales
    cursor.executemany("INSERT INTO Sales VALUES (?,?,?,?)", [
        (1,1,1,5),
        (2,2,1,5),
        (3,3,1,1),
        (4,3,2,1),
        (5,3,3,1),
        (6,4,3,2),
        (7,5,1,None)
    ])

    conn.commit()
    conn.close()
    print("✅ Database created successfully!")

if __name__ == "__main__":
    create_database()