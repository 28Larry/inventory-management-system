# Function to establish MySQL connection
import mysql.connector
def connect_to_database():
    return mysql.connector.connect(
    host="localhost",
    user="root",
    password="rlawi",
    database="Inventory management system")
        
#function for creating the database Inventory mangement system
# Function to create product table
#Function to add a product
def add_product(name, quantity, price):
   try:
        connection = connect_to_database()
        cursor = connection.cursor()
        return connection
        sql = "INSERT INTO Product table (name, Quantity, Price) VALUES (lawi, 25,1000 )"
        cursor.execute(sql, (name, quantity, price))
        connection.commit()
        print("Product added successfully!")
   except mysql.connector.Error as error:
        print("Error adding product:", error)
   finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Function to update product quantity
#Function to add to quantity table

def update_product_quantity(product_id, new_quantity):
    try:
        connection = connect_to_database()
        cursor = connection.cursor()
        sql = "UPDATE  Set Quantity = 15 WHERE Quantity =25"
        cursor.execute(sql, (new_quantity, product_id))
        connection.commit()
        print("Product quantity updated successfully!")
    except mysql.connector.Error as error:
        print("Error updating product quantity:", error)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Add more functions for other modules (e.g., Purchase Management, Sales Management, User Management)

# Example usage
add_product("Mouse", 10, 800)
update_product_quantity(1, 15)

