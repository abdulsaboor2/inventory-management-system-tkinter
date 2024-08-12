# Inventory Management System

This project is a comprehensive Inventory Management System built using Python and Tkinter. The application is designed to manage products, transactions, and sales efficiently. One of the key aspects of this system is its robust input validation, ensuring data integrity and preventing common user errors.

## Features
+ **User Authentication**: Admin and User roles with different permissions.
+ **Product Management**: Add, update, delete, and categorize products.
+ **Sales and Purchase Tracking**: Track sales and purchases and generate reports.
+ **Low Stock Alerts**: Automatic notifications for items with low stock levels.
+ **Clear Invoice**: Clear all transactions from the system.

## Key Validation Features:
1. **Product Input Validation:**
    - **Empty Field Checks**: The system ensures that all necessary fields (Product Name, Quantity, Price, and Category) are filled out before allowing a product to be added or updated.
    - **Quantity Validation**: The quantity field is validated to ensure it is a positive integer. This prevents the entry of invalid or negative quantities.
    - **Price Validation**: The price field is validated to ensure it is a non-negative float. This ensures that the prices are always realistic and non-negative.
    - **Category Field Validation**: Ensures the category is a non-empty string, safeguarding against missing or incorrect categorizations.
2. **User Login Validation:**
    - **Empty Field Checks**: Both username and password fields are required to be filled out before attempting to log in.
    - **Role-Based Access Control**: The system validates user credentials against predefined roles (admin and user), granting appropriate access levels.
3. **Transaction Validation:**
    - **Sufficient Stock Checks**: During the sale of a product, the system checks to ensure there is enough stock available before completing the transaction.
    - **Quantity Validation**: For both purchasing and selling, the quantity must be a valid positive integer, ensuring meaningful and correct transactions.
4. **Low Stock Alerts:**
    - The system automatically checks for products with low stock (less than 10 units) and alerts the user, helping prevent stockouts.

## Installation

1. **Clone the Repository:**
```
git clone https://github.com/abdulsaboor2/inventory-management-system-tkinter.git
cd Inventory-Management-System
```
2. **Install the Required Libraries:**
Tkinter comes pre-installed with Python, but if you need to install it, use:
```
pip install tk
```
3. **Run the Application:**
```
python ims.py
```

## Usage

+ **Login as either admin or user:**
    - Admin: admin/admin123
    - User: user/user123
+ Manage your inventory by adding, updating, or deleting products.
+ Track sales and purchases and generate sales reports.
+ Logout and manage your session effectively.


# Interface
**Login**

![image](https://github.com/user-attachments/assets/00aa6f5f-6d28-495e-a337-42e89ad13bec)

**Dashboard**

![image](https://github.com/user-attachments/assets/e0239ab5-0227-4804-a461-a7f5f2d72387)

**Add Item**

![image](https://github.com/user-attachments/assets/132ebafb-508e-41df-a203-b5ac0f68f114)

**Update Item**

**Before**

![image](https://github.com/user-attachments/assets/52624573-3823-41de-859e-719425cb88b4)

**After**

![image](https://github.com/user-attachments/assets/95d9b909-51fc-4340-9eef-092edeb0db48)

**Sell Item**

![image](https://github.com/user-attachments/assets/4b8323bc-b453-40a5-8457-59b21c3a84eb)

**Purchase Items From Given Items**

![image](https://github.com/user-attachments/assets/e32a70ae-bf01-4b7a-9bdc-19d4c91c276c)

**Generate Reports**

![image](https://github.com/user-attachments/assets/63563606-37d8-4e5d-bfd1-e2a23d259ef1)

**Delete Item**

Before

![image](https://github.com/user-attachments/assets/65d98479-4cc0-4007-90c1-683086acbff4)

After

![image](https://github.com/user-attachments/assets/06126f97-6804-416f-b65a-81fc28460eb9)

**Low Stock Alert**

![image](https://github.com/user-attachments/assets/4f4dbd70-f8dd-4cdb-a7a7-d6cd7a3da446)


## Contributing

Contributions are welcome! Please create a pull request or open an issue for suggestions.
