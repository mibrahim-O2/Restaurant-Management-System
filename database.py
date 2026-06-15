# database.py
# Creates the SQLite database and seeds the menu.
# Run once: python database.py

import sqlite3

def initialize_database():
    conn = sqlite3.connect('restaurant.db')
    cursor = conn.cursor()

    # Create menu table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS menu (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item_name TEXT NOT NULL,
            price REAL NOT NULL,
            category TEXT NOT NULL
        )
    ''')

    # Create orders table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT NOT NULL,
            item_name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            total_price REAL NOT NULL
        )
    ''')

    # Create reservations table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reservations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT NOT NULL,
            table_number INTEGER NOT NULL,
            reservation_date TEXT NOT NULL
        )
    ''')

    # Seed menu only if empty
    cursor.execute('SELECT COUNT(*) FROM menu')
    if cursor.fetchone()[0] == 0:
        menu_items = [
            ('Chicken Burger',       350.00, 'Main Course'),
            ('Beef Steak',           850.00, 'Main Course'),
            ('Grilled Fish',         700.00, 'Main Course'),
            ('Veggie Wrap',          280.00, 'Main Course'),
            ('Club Sandwich',        320.00, 'Snacks'),
            ('French Fries',         180.00, 'Snacks'),
            ('Spring Rolls',         220.00, 'Snacks'),
            ('Mango Juice',          120.00, 'Drinks'),
            ('Lemon Soda',           100.00, 'Drinks'),
            ('Mineral Water',         60.00, 'Drinks'),
            ('Chocolate Cake',       200.00, 'Desserts'),
            ('Ice Cream (2 scoops)', 150.00, 'Desserts'),
            ('Brownie Fudge',        180.00, 'Desserts'),
        ]
        cursor.executemany(
            'INSERT INTO menu (item_name, price, category) VALUES (?, ?, ?)',
            menu_items
        )
        print("Menu items seeded.")

    conn.commit()
    conn.close()
    print("Database ready. Run: python app.py")


if __name__ == '__main__':
    initialize_database()