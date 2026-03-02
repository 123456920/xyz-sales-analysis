# XYZ Sales Analysis

## Objective

The goal of this assignment is to analyze sales data and extract the total quantities purchased per customer aged 18–35.

Two separate solutions are implemented:

1. Pure SQL solution  
2. Pandas solution  

Both solutions produce identical CSV output.

---

## Database Design

Tables:

- Customer (CustomerID, Age)
- Orders (OrderID, CustomerID)
- Items (ItemID, ItemName)
- Sales (SalesID, OrderID, ItemID, Quantity)

Business Rules:

- A sales receipt can have multiple items.
- Clerk records all items including non-purchased (Quantity = NULL).
- Each customer can have multiple orders.
- Only customers aged 18–35 are included.
- Items with total quantity = 0 are omitted.
- NULL quantities are ignored.

---

## Setup Instructions

Clone repository:

git clone https://github.com/123456920/xyz-sales-analysis.git

Create virtual environment:

python -m venv venv

Activate (Windows):

venv\Scripts\activate.bat

Install dependencies:

pip install -r requirements.txt

Create database:

python create_database.py

---

## Run SQL Solution

python sql_solution.py

---

## Run Pandas Solution

python pandas_solution.py

---

## Output Format

Customer;Age;Item;Quantity

Example:

1;21;x;10
2;23;x;1
2;23;y;1
2;23;z;1
3;35;z;2

---

## Technical Notes

- SQL performs aggregation inside SQLite.
- Pandas performs merge + groupby in memory.
- Both implementations generate identical results.

---

## Author

GitHub: https://github.com/123456920