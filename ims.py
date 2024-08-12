import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3


class InventorySystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System")
        self.root.geometry("900x700")

        # Set color themes
        self.bg_color = "#f0f0f0"
        self.btn_color = "#4CAF50"
        self.btn_text_color = "white"
        self.label_color = "#333"
        self.entry_bg_color = "white"

        # Initialize database connection
        self.conn = sqlite3.connect('inventory.db')
        self.cursor = self.conn.cursor()

        # Create tables
        self.create_tables()

        # Create login widgets
        self.create_login_widgets()

    def create_tables(self):
        # Create products table
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT,
                            quantity INTEGER,
                            price REAL,
                            category TEXT)''')

        # Create transactions table
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS transactions (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            product_id INTEGER,
                            transaction_type TEXT,
                            quantity INTEGER,
                            FOREIGN KEY (product_id) REFERENCES products(id))''')

        # Create sales table
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS sales (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            product_id INTEGER,
                            quantity INTEGER,
                            revenue REAL,
                            FOREIGN KEY (product_id) REFERENCES products(id))''')

    def create_login_widgets(self):
        login_frame = tk.Frame(self.root, padx=20, pady=20, bg=self.bg_color)
        login_frame.pack(expand=True)

        self.label_username = tk.Label(login_frame, text="Username:", bg=self.bg_color, fg=self.label_color)
        self.label_username.grid(row=0, column=0, padx=10, pady=5)
        self.entry_username = tk.Entry(login_frame, bg=self.entry_bg_color)
        self.entry_username.grid(row=0, column=1, padx=10, pady=5)

        self.label_password = tk.Label(login_frame, text="Password:", bg=self.bg_color, fg=self.label_color)
        self.label_password.grid(row=1, column=0, padx=10, pady=5)
        self.entry_password = tk.Entry(login_frame, show="*", bg=self.entry_bg_color)
        self.entry_password.grid(row=1, column=1, padx=10, pady=5)

        self.button_login = tk.Button(login_frame, text="Login", bg=self.btn_color, fg=self.btn_text_color, command=self.login)
        self.button_login.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        # Input validation
        if not username or not password:
            messagebox.showerror("Error", "Username and password cannot be empty.")
            return

        # Hardcoded roles: admin and user
        if username == "admin" and password == "admin123":
            self.role = "admin"
            self.show_product_management_screen()
        elif username == "user" and password == "user123":
            self.role = "user"
            self.show_product_management_screen()
        else:
            messagebox.showerror("Error", "Invalid username or password")

    def show_product_management_screen(self):
        # Destroy login widgets
        for widget in self.root.winfo_children():
            widget.destroy()

        self.main_frame = tk.Frame(self.root, padx=20, pady=20, bg=self.bg_color)
        self.main_frame.pack(expand=True, fill=tk.BOTH)

        # Create product management widgets
        self.create_product_management_widgets()

        # Display product and transaction lists
        self.create_listboxes()

        # Create sales report button
        self.button_generate_report = tk.Button(self.main_frame, text="Generate Sales Report",
                                                bg=self.btn_color, fg=self.btn_text_color,
                                                command=self.generate_sales_report)
        self.button_generate_report.grid(row=9, column=2, padx=10, pady=5, sticky='ew')

        self.button_clear_invoice = tk.Button(self.main_frame, command=self.clear_invoice,
                                              bg=self.btn_color, fg=self.btn_text_color, bd=0)
        self.button_clear_invoice.grid(row=9, column=0, padx=10, pady=5, sticky='ew')

        # Create clear invoice button
        self.button_clear_invoice = tk.Button(self.main_frame, text="Clear Invoice",
                                              bg=self.btn_color, fg=self.btn_text_color, command=self.clear_invoice)
        self.button_clear_invoice.grid(row=9, column=0, padx=10, pady=5, sticky='ew')

        # Create logout button
        self.button_logout = tk.Button(self.main_frame, text="Logout", bg=self.btn_color, fg=self.btn_text_color, command=self.logout)
        self.button_logout.grid(row=10, column=2, padx=10, pady=5, sticky='ew')

        # Populate product and transaction lists
        self.populate_product_list()
        self.populate_transaction_list()
        self.check_low_stock()

    def create_product_management_widgets(self):
        self.label_title = tk.Label(self.main_frame, text="Product Management", font=("Helvetica", 16))
        self.label_title.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        self.label_product_name = tk.Label(self.main_frame, text="Product Name:")
        self.label_product_name.grid(row=1, column=0, padx=10, pady=5)
        self.entry_product_name = tk.Entry(self.main_frame)
        self.entry_product_name.grid(row=1, column=1, padx=10, pady=5)

        self.label_quantity = tk.Label(self.main_frame, text="Quantity:")
        self.label_quantity.grid(row=2, column=0, padx=10, pady=5)
        self.entry_quantity = tk.Entry(self.main_frame)
        self.entry_quantity.grid(row=2, column=1, padx=10, pady=5)

        self.label_price = tk.Label(self.main_frame, text="Price:")
        self.label_price.grid(row=3, column=0, padx=10, pady=5)
        self.entry_price = tk.Entry(self.main_frame)
        self.entry_price.grid(row=3, column=1, padx=10, pady=5)

        self.label_category = tk.Label(self.main_frame, text="Category:")
        self.label_category.grid(row=4, column=0, padx=10, pady=5)
        self.entry_category = tk.Entry(self.main_frame)
        self.entry_category.grid(row=4, column=1, padx=10, pady=5)

        self.button_add_product = tk.Button(self.main_frame, text="Add Product", bg=self.btn_color, fg=self.btn_text_color, command=self.add_product)
        self.button_add_product.grid(row=5, column=0, padx=10, pady=5)

        self.button_update_product = tk.Button(self.main_frame, text="Update Product", bg=self.btn_color, fg=self.btn_text_color, command=self.update_product)
        self.button_update_product.grid(row=5, column=1, padx=10, pady=5)

        if self.role == "admin":
            self.button_delete_product = tk.Button(self.main_frame, text="Delete Product", bg=self.btn_color, fg=self.btn_text_color, command=self.delete_product)
            self.button_delete_product.grid(row=5, column=2, padx=10, pady=5)

        self.button_sell_product = tk.Button(self.main_frame, text="Sell Product", bg=self.btn_color, fg=self.btn_text_color, command=self.sell_product)
        self.button_sell_product.grid(row=6, column=0, padx=10, pady=5)

        self.button_purchase_product = tk.Button(self.main_frame, text="Purchase Product", bg=self.btn_color, fg=self.btn_text_color, command=self.purchase_product)
        self.button_purchase_product.grid(row=6, column=1, padx=10, pady=5)

    def create_listboxes(self):
        # Product List
        self.label_product_list = tk.Label(self.main_frame, text="Product List")
        self.label_product_list.grid(row=7, column=0, columnspan=2, padx=10, pady=5)

        self.product_listbox = tk.Listbox(self.main_frame, width=50, height=10)
        self.product_listbox.grid(row=8, column=0, columnspan=2, padx=10, pady=5)
        self.product_listbox.bind('<<ListboxSelect>>', self.display_quantity)

        # Transaction List
        self.label_transaction_list = tk.Label(self.main_frame, text="Transaction List")
        self.label_transaction_list.grid(row=7, column=2, padx=10, pady=5)

        self.transaction_listbox = tk.Listbox(self.main_frame, width=50, height=10)
        self.transaction_listbox.grid(row=8, column=2, padx=10, pady=5)

    def clear_invoice(self):
        self.transaction_listbox.delete(0, tk.END)

    def populate_product_list(self):
        self.product_listbox.delete(0, tk.END)
        self.cursor.execute("SELECT id, name, quantity, price, category FROM products")
        products = self.cursor.fetchall()
        for product in products:
            self.product_listbox.insert(tk.END, f"{product[0]} - {product[1]}, Qty: {product[2]}, Price: ${product[3]:.2f}, Category: {product[4]}")

    def populate_transaction_list(self):
        self.transaction_listbox.delete(0, tk.END)
        self.cursor.execute("SELECT t.id, p.name, t.transaction_type, t.quantity FROM transactions t JOIN products p ON t.product_id = p.id")
        transactions = self.cursor.fetchall()
        for transaction in transactions:
            self.transaction_listbox.insert(tk.END, f"{transaction[0]} - {transaction[1]}, Type: {transaction[2]}, Qty: {transaction[3]}")

    def display_quantity(self, event):
        selected_index = self.product_listbox.curselection()
        if selected_index:
            selected_product = self.product_listbox.get(selected_index)
            product_id = int(selected_product.split(' - ')[0])  # Extract product ID
            self.cursor.execute("SELECT quantity FROM products WHERE id = ?", (product_id,))
            product = self.cursor.fetchone()
            if product:
                self.entry_quantity.delete(0, tk.END)
                self.entry_quantity.insert(tk.END, product[0])

    def validate_product_inputs(self, name, quantity, price, category):
        if not name or not quantity or not price or not category:
            messagebox.showwarning("Warning", "Please fill all fields.")
            return False
        try:
            quantity = int(quantity)
            if quantity <= 0:
                messagebox.showwarning("Warning", "Quantity must be a positive integer.")
                return False
        except ValueError:
            messagebox.showwarning("Warning", "Quantity must be a valid integer.")
            return False

        try:
            price = float(price)
            if price < 0:
                messagebox.showwarning("Warning", "Price must be a non-negative number.")
                return False
        except ValueError:
            messagebox.showwarning("Warning", "Price must be a valid number.")
            return False

        return True

    def add_product(self):
        name = self.entry_product_name.get()
        quantity = self.entry_quantity.get()
        price = self.entry_price.get()
        category = self.entry_category.get()

        if not self.validate_product_inputs(name, quantity, price, category):
            return

        self.cursor.execute("INSERT INTO products (name, quantity, price, category) VALUES (?, ?, ?, ?)",
                            (name, quantity, price, category))
        self.conn.commit()
        self.populate_product_list()
        messagebox.showinfo("Success", "Product added successfully.")

    def update_product(self):
        selected_index = self.product_listbox.curselection()
        if not selected_index:
            messagebox.showwarning("Warning", "Please select a product to update.")
            return

        selected_product = self.product_listbox.get(selected_index)
        product_id = int(selected_product.split(' - ')[0])  # Extract product ID

        name = self.entry_product_name.get()
        quantity = self.entry_quantity.get()
        price = self.entry_price.get()
        category = self.entry_category.get()

        if not self.validate_product_inputs(name, quantity, price, category):
            return

        self.cursor.execute("UPDATE products SET name = ?, quantity = ?, price = ?, category = ? WHERE id = ?",
                            (name, quantity, price, category, product_id))
        self.conn.commit()
        self.populate_product_list()
        messagebox.showinfo("Success", "Product updated successfully.")

    def delete_product(self):
        if self.role != "admin":
            messagebox.showerror("Error", "Only admin users can delete products.")
            return

        selected_index = self.product_listbox.curselection()
        if not selected_index:
            messagebox.showwarning("Warning", "Please select a product to delete.")
            return

        selected_product = self.product_listbox.get(selected_index)
        product_id = int(selected_product.split(' - ')[0])  # Extract product ID

        confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this product?")
        if confirm:
            self.cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
            self.conn.commit()
            self.populate_product_list()
            messagebox.showinfo("Success", "Product deleted successfully.")

    def sell_product(self):
        selected_index = self.product_listbox.curselection()
        if not selected_index:
            messagebox.showwarning("Warning", "Please select a product to sell.")
            return

        selected_product = self.product_listbox.get(selected_index)
        product_id = int(selected_product.split(' - ')[0])  # Extract product ID
        quantity = self.entry_quantity.get()

        if not quantity:
            messagebox.showwarning("Warning", "Please enter quantity to sell.")
            return

        try:
            quantity = int(quantity)
            if quantity <= 0:
                messagebox.showwarning("Warning", "Quantity must be a positive integer.")
                return
        except ValueError:
            messagebox.showwarning("Warning", "Quantity must be a valid integer.")
            return

        # Fetch the current quantity of the selected product
        self.cursor.execute("SELECT quantity, price FROM products WHERE id = ?", (product_id,))
        product = self.cursor.fetchone()

        if not product or product[0] < quantity:
            messagebox.showwarning("Warning", "Insufficient stock.")
            return

        # Update product quantity
        new_quantity = product[0] - quantity
        self.cursor.execute("UPDATE products SET quantity = ? WHERE id = ?", (new_quantity, product_id))
        self.conn.commit()

        # Record the sale in the transactions and sales tables
        self.cursor.execute("INSERT INTO transactions (product_id, transaction_type, quantity) VALUES (?, 'sale', ?)",
                            (product_id, quantity))
        revenue = product[1] * quantity
        self.cursor.execute("INSERT INTO sales (product_id, quantity, revenue) VALUES (?, ?, ?)",
                            (product_id, quantity, revenue))
        self.conn.commit()

        self.populate_product_list()
        self.populate_transaction_list()
        messagebox.showinfo("Success", "Product sold successfully.")

    def purchase_product(self):
        selected_index = self.product_listbox.curselection()
        if not selected_index:
            messagebox.showwarning("Warning", "Please select a product to purchase.")
            return

        selected_product = self.product_listbox.get(selected_index)
        product_id = int(selected_product.split(' - ')[0])  # Extract product ID
        quantity = self.entry_quantity.get()

        if not quantity:
            messagebox.showwarning("Warning", "Please enter quantity to purchase.")
            return

        try:
            quantity = int(quantity)
            if quantity <= 0:
                messagebox.showwarning("Warning", "Quantity must be a positive integer.")
                return
        except ValueError:
            messagebox.showwarning("Warning", "Quantity must be a valid integer.")
            return

        # Fetch the current quantity of the selected product
        self.cursor.execute("SELECT quantity FROM products WHERE id = ?", (product_id,))
        product = self.cursor.fetchone()

        # Update product quantity
        new_quantity = product[0] + quantity
        self.cursor.execute("UPDATE products SET quantity = ? WHERE id = ?", (new_quantity, product_id))
        self.conn.commit()

        # Record the purchase in the transactions table
        self.cursor.execute("INSERT INTO transactions (product_id, transaction_type, quantity) VALUES (?, 'purchase', ?)",
                            (product_id, quantity))
        self.conn.commit()

        self.populate_product_list()
        self.populate_transaction_list()
        messagebox.showinfo("Success", "Product purchased successfully.")

    def check_low_stock(self):
        # Check for low-stock products
        self.cursor.execute("SELECT name, quantity FROM products WHERE quantity < 10")
        low_stock_products = self.cursor.fetchall()

        if low_stock_products:
            warning_message = "The following products are low in stock:\n"
            warning_message += "\n".join([f"{product[0]}: {product[1]} units" for product in low_stock_products])
            messagebox.showwarning("Low Stock Warning", warning_message)

    def generate_sales_report(self):
        self.cursor.execute("SELECT p.name, s.quantity, s.revenue FROM sales s JOIN products p ON s.product_id = p.id")
        sales = self.cursor.fetchall()

        report = "Sales Report\n"
        report += "Product Name | Quantity Sold | Revenue\n"
        report += "-"*40 + "\n"
        for sale in sales:
            report += f"{sale[0]} | {sale[1]} | ${sale[2]:.2f}\n"

        # Display the sales report in another window
        report_window = tk.Toplevel(self.root)
        report_window.title("Sales Report")
        report_text = tk.Text(report_window, wrap="word", padx=10, pady=10)
        report_text.insert(tk.END, report)
        report_text.pack(expand=True, fill="both")
        report_text.config(state=tk.DISABLED)  # To make report read-only

    def logout(self):
        self.main_frame.destroy()
        self.create_login_widgets()

if __name__ == "__main__":
    root = tk.Tk()
    app = InventorySystem(root)
    root.mainloop()
