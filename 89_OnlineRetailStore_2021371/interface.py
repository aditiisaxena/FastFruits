import pandas as pd
import mysql.connector
import tkinter as tk
from tkinter import ttk

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="uwu123",
    database="FastFruits"
)

mycursor = mydb.cursor()

def display_table(data):
    window = tk.Tk()
    window.title("Table View")
    table = ttk.Treeview(window, show="headings", columns=tuple(data.columns))
    for column in data.columns:
        table.heading(column, text=column)
    for row in data.to_numpy():
        table.insert("", "end", values=tuple(row))
    scrollbar = ttk.Scrollbar(window, orient="vertical", command=table.yview)
    scrollbar.pack(side="right", fill="y")
    table.configure(yscrollcommand=scrollbar.set)
    table.pack(side="left", fill="both", expand=True)
    window.mainloop()

menu = """
1. View number of orders made by each customer
2. View Salads that are in more than 2 Carts
3. View order totals by Customers and Dark Stores
4. View Total Price of Smoothies Added Between Specific Periods
5. View supplier dues and listing fees by state
6. View total sales by day and status
7. Exit
"""
queryx = """DROP TRIGGER IF EXISTS `check_order_amount`;"""
queryy = """DROP TRIGGER IF EXISTS `check_fruit_exists`;"""
query1 = """SELECT first_name, last_name, (SELECT COUNT(*) FROM `Orders` WHERE cID = Customers.cID) AS NumOrders
FROM Customers;"""
query2 = """SELECT *
FROM `Salad`
WHERE slID IN (SELECT slID FROM `Cart` GROUP BY slID HAVING COUNT(*) > 2);"""
query3 = """SELECT cID, dID, SUM(amount) as total
FROM `Orders`
GROUP BY cID, dID WITH ROLLUP;"""
query4 = """SELECT SUM(price) as total_smoothies
FROM Fruits
WHERE addedDate >= '2022-01-01' AND addedDate <= '2022-03-31';"""
query5 = """SELECT supID,
       SUM(CASE WHEN states = 'California' THEN dues ELSE 0 END) AS CA_dues,
       SUM(CASE WHEN states = 'Calfornia' THEN listing_fee ELSE 0 END) AS CA_listing_fee,
       SUM(CASE WHEN states = 'NewYork' THEN dues ELSE 0 END) AS NY_dues,
       SUM(CASE WHEN states = 'NewYork' THEN listing_fee ELSE 0 END) AS NY_listing_fee,
       SUM(CASE WHEN states = 'Nevada' THEN dues ELSE 0 END) AS TX_dues,
       SUM(CASE WHEN states = 'Nevada' THEN listing_fee ELSE 0 END) AS TX_listing_fee
FROM Suppliers
GROUP BY supID;"""
query6 = """SELECT DATE_FORMAT(orderDate, '%Y-%m-%d') AS day, status, SUM(amount) AS total_sales
FROM Orders
GROUP BY day, status"""
query7a = """
CREATE TRIGGER check_order_amount 
BEFORE INSERT ON `Orders`
FOR EACH ROW
BEGIN
    IF NEW.amount < 100 THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'Order amount cannot be less than 100.';
    END IF;
END;
"""
query7b = """
CREATE TRIGGER `check_fruit_exists`
BEFORE INSERT ON `Smoothies_Ingredients`
FOR EACH ROW
BEGIN
    IF NOT EXISTS (SELECT 1 FROM `Fruits` WHERE `fID` = NEW.`fID`) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Error: Fruit with fID ';
    END IF;
END;
"""
check = True
print("Welcome Admin! What would you like to do?")
mycursor.execute(queryx)
mycursor.execute(queryy)
mycursor.execute(query7a)
mycursor.execute(query7b)
while(check):
    print(menu)
    choice = int(input("Enter your choice: "))
    if choice == 1:
        mycursor.execute(query1)
        df = pd.DataFrame(mycursor.fetchall(), columns=mycursor.column_names)
        display_table(df)
    elif choice == 2:
        mycursor.execute(query2)
        df = pd.DataFrame(mycursor.fetchall(), columns=mycursor.column_names)
        display_table(df)
    elif choice == 3:
        mycursor.execute(query3)
        df = pd.DataFrame(mycursor.fetchall(), columns=mycursor.column_names)
        display_table(df)
    elif choice == 4:
        mycursor.execute(query4)
        df = pd.DataFrame(mycursor.fetchall(), columns=mycursor.column_names)
        display_table(df)
    elif choice == 5:
        mycursor.execute(query5)
        df = pd.DataFrame(mycursor.fetchall(), columns=mycursor.column_names)
        display_table(df)
    elif choice == 6:
        mycursor.execute(query6)
        df = pd.DataFrame(mycursor.fetchall(), columns=mycursor.column_names)
        display_table(df)
    elif choice == 7:
        check = False
        print("Goodbye!")
    else:
        print("Invalid choice!")