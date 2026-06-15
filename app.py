# Main Flask application — routes and business logic.

from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# -------------------------------------------------------
# HELPER: Database connection
# -------------------------------------------------------
def get_db_connection():
    conn = sqlite3.connect('restaurant.db')
    conn.row_factory = sqlite3.Row
    return conn


# -------------------------------------------------------
# ROUTE 1: Home — redirect to menu
# -------------------------------------------------------
@app.route('/')
def home():
    return redirect(url_for('menu'))


# -------------------------------------------------------
# ROUTE 2: Menu
# -------------------------------------------------------
@app.route('/menu')
def menu():
    conn = get_db_connection()
    items = conn.execute(
        'SELECT * FROM menu ORDER BY category, item_name'
    ).fetchall()
    conn.close()
    return render_template('menu.html', items=items)


# -------------------------------------------------------
# ROUTE 3: Order Form (GET)
# -------------------------------------------------------
@app.route('/order', methods=['GET'])
def order_form():
    conn = get_db_connection()
    menu_items = conn.execute(
        'SELECT * FROM menu ORDER BY category, item_name'
    ).fetchall()
    conn.close()
    return render_template('order.html', menu_items=menu_items)


# -------------------------------------------------------
# ROUTE 4: Place Order (POST)
# -------------------------------------------------------
@app.route('/order', methods=['POST'])
def place_order():
    customer_name = request.form['customer_name'].strip()
    item_name     = request.form['item_name']
    quantity      = int(request.form['quantity'])

    if not customer_name or not item_name or quantity < 1:
        return redirect(url_for('order_form'))

    conn = get_db_connection()

    item = conn.execute(
        'SELECT price FROM menu WHERE item_name = ?', (item_name,)
    ).fetchone()

    if item is None:
        conn.close()
        return redirect(url_for('order_form'))

    total_price = item['price'] * quantity

    conn.execute(
        'INSERT INTO orders (customer_name, item_name, quantity, total_price) VALUES (?, ?, ?, ?)',
        (customer_name, item_name, quantity, total_price)
    )
    conn.commit()
    conn.close()

    return redirect(url_for('view_orders'))


# -------------------------------------------------------
# ROUTE 5: View Orders
# -------------------------------------------------------
@app.route('/orders')
def view_orders():
    conn = get_db_connection()
    orders = conn.execute(
        'SELECT * FROM orders ORDER BY id DESC'
    ).fetchall()
    conn.close()
    return render_template('orders.html', orders=orders)


# -------------------------------------------------------
# ROUTE 6: Delete Order
# -------------------------------------------------------
@app.route('/delete_order/<int:order_id>')
def delete_order(order_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM orders WHERE id = ?', (order_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('view_orders'))


# -------------------------------------------------------
# ROUTE 7: Reservation Form (GET)
# -------------------------------------------------------
@app.route('/reservation', methods=['GET'])
def reservation_form():
    return render_template('reservation.html')


# -------------------------------------------------------
# ROUTE 8: Make Reservation (POST)
# -------------------------------------------------------
@app.route('/reservation', methods=['POST'])
def make_reservation():
    customer_name    = request.form['customer_name'].strip()
    table_number     = request.form['table_number']
    reservation_date = request.form['reservation_date']

    if not customer_name or not table_number or not reservation_date:
        return redirect(url_for('reservation_form'))

    conn = get_db_connection()
    conn.execute(
        'INSERT INTO reservations (customer_name, table_number, reservation_date) VALUES (?, ?, ?)',
        (customer_name, int(table_number), reservation_date)
    )
    conn.commit()
    conn.close()

    return redirect(url_for('view_reservations'))


# -------------------------------------------------------
# ROUTE 9: View Reservations
# -------------------------------------------------------
@app.route('/reservations')
def view_reservations():
    conn = get_db_connection()
    reservations = conn.execute(
        'SELECT * FROM reservations ORDER BY reservation_date ASC'
    ).fetchall()
    conn.close()
    return render_template('reservations.html', reservations=reservations)


# -------------------------------------------------------
# ROUTE 10: Cancel Reservation
# -------------------------------------------------------
@app.route('/cancel_reservation/<int:reservation_id>')
def cancel_reservation(reservation_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM reservations WHERE id = ?', (reservation_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('view_reservations'))


# -------------------------------------------------------
# 404 Error Handler
# -------------------------------------------------------
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


# -------------------------------------------------------
# Run
# -------------------------------------------------------
if __name__ == '__main__':
    app.run(debug=True)
