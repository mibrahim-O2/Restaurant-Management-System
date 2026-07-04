<div align="center">

<!-- BADGES -->
![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.x-000000?style=for-the-badge&logo=flask&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)
![Jinja2](https://img.shields.io/badge/Jinja2-Templating-B41717?style=for-the-badge&logo=jinja&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-gold?style=for-the-badge)
<br/>

# RestaurantMS
<br/> 
</div>

## Overview
A web-based Restaurant Management System built using Python and Flask with an SQLite database on the backend and Bootstrap 5 on the frontend.The system covers three things: browsing the menu, placing and managing customer orders, and handling table reservations. The scope is focused and the code is straightforward *NO* login system, *NO* payment flow, just clean backend logic that works.
Built as a hands-on project to practice connecting Flask routes to a real database, handling form submissions, and structuring a multi page web app from scratch.

---

## Features

| Feature | Description |
|---|---|
| View Menu | Browse all items grouped by category with live pricing |
| Place Order | Submit customer orders linked to menu items |
| View Orders | See all active orders in a sortable table |
| Delete Order | Remove any order with a confirmation prompt |
| Reserve Table | Book one of 15 tables for a specific date |
| View Reservations | See all upcoming reservations at a glance |
| Cancel Reservation | Remove any reservation with a single click |
| 404 Page | Custom error page matching the dark theme |

---

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3 |
| Framework | Flask |
| Database | SQLite (via Python's built-in `sqlite3`) |
| Templating | Jinja2 |
| Frontend | Bootstrap 5.3 + Bootstrap Icons |
| Fonts | Playfair Display · Plus Jakarta Sans |
| Styling | Custom CSS with CSS Variables |

---

## Folder Structure

```bash
codealpha-restaurant-management-system/
│
├── app.py                          ← All Flask routes and business logic
├── database.py                     ← Database creation and menu seeding
├── requirements.txt                ← Python dependencies
├── README.md                       ← Project documentation
│
├── templates/
│   ├── base.html                   ← Shared layout: navbar + footer
│   ├── menu.html                   ← Menu display grouped by category
│   ├── order.html                  ← Place order form
│   ├── orders.html                 ← All orders table with delete
│   ├── reservation.html            ← Table reservation form
│   ├── reservations.html           ← All reservations table with cancel
│   └── 404.html                    ← Custom 404 error page
│
├── static/
│   └── style.css                   ← Full custom dark theme CSS
│
└── Screenshots/
    ├── dashboard1.png
    ├── dashboard2.png
    ├── dashboard3.png
    ├── neworder.png
    ├── orderlist.png
    ├── reservation.png
    └── reservationlist.png
```

---

## Database Design

**File:** `restaurant.db`  auto-created by SQLite on first run.

### `menu`

| Column | Type | Description |
|---|---|---|
| id | INTEGER PK | Auto-increment unique identifier |
| item_name | TEXT | Name of the food or drink item |
| price | REAL | Item price in Rs. (supports decimals) |
| category | TEXT | Group: Main Course, Snacks, Drinks, Desserts |

### `orders`

| Column | Type | Description |
|---|---|---|
| id | INTEGER PK | Auto-increment unique identifier |
| customer_name | TEXT | Name of the customer |
| item_name | TEXT | Ordered item (matched from menu) |
| quantity | INTEGER | Number of units ordered |
| total_price | REAL | Calculated as price × quantity |

### `reservations`

| Column | Type | Description |
|---|---|---|
| id | INTEGER PK | Auto-increment unique identifier |
| customer_name | TEXT | Name of the customer |
| table_number | INTEGER | Table number between 1 and 15 |
| reservation_date | TEXT | Date in YYYY-MM-DD format |

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/mibrahim-O2/codealpha-restaurant-management-system.git
cd codealpha-restaurant-management-system
```

### 2. Create and activate virtual environment

```powershell
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```powershell
pip install -r requirements.txt
```

### 4. Initialize the database

```powershell
python database.py
```

### 5. Run the application

```powershell
python app.py
```

### 6. Open browser

```
http://127.0.0.1:5000
```

---

## Routes Reference

| Route | Method | Description |
|---|---|---|
| `/` | GET | Redirects to `/menu` |
| `/menu` | GET | View all menu items by category |
| `/order` | GET | Show the place order form |
| `/order` | POST | Submit and save a new order |
| `/orders` | GET | View all orders |
| `/delete_order/<id>` | GET | Delete an order by ID |
| `/reservation` | GET | Show the table reservation form |
| `/reservation` | POST | Submit and save a new reservation |
| `/reservations` | GET | View all reservations |
| `/cancel_reservation/<id>` | GET | Cancel a reservation by ID |

---

## Screenshots

### Dashboard — Menu Page

![Dashboard Part 1](https://raw.githubusercontent.com/mibrahim-O2/codealpha-restaurant-management-system/main/Screenshots/dasboard1.png)
![Dashboard Part 2](https://raw.githubusercontent.com/mibrahim-O2/codealpha-restaurant-management-system/main/Screenshots/dashboard2%20(2).png)
![Dashboard Part 3](https://raw.githubusercontent.com/mibrahim-O2/codealpha-restaurant-management-system/main/Screenshots/dashboard3.png)

---

### New Order Form

![New Order](https://raw.githubusercontent.com/mibrahim-O2/codealpha-restaurant-management-system/main/Screenshots/neworder.png)

---

### Orders List

![Order List](https://raw.githubusercontent.com/mibrahim-O2/codealpha-restaurant-management-system/main/Screenshots/orderlist.png)

---

### Reservation Form

![Reservation Form](https://raw.githubusercontent.com/mibrahim-O2/codealpha-restaurant-management-system/main/Screenshots/reservation.png)

---

### Reservations List

![Reservations List](https://raw.githubusercontent.com/mibrahim-O2/codealpha-restaurant-management-system/main/Screenshots/reservationlist.png)

---

## How It Works

```
User opens the app
        ↓
Navbar provides access to all sections
        ↓
┌─────────────────────────────────┐
│  MENU  →  /menu                 │
│  All items grouped by category  │
└─────────────────────────────────┘
        ↓
┌──────────────────────────────────────────┐
│  ORDERS  →  /order  (form)               │
│  Select item · enter name · set quantity │
│  Total = price × quantity (auto calc)    │
│  View all at /orders · Delete any order  │
└──────────────────────────────────────────┘
        ↓
┌─────────────────────────────────────────────┐
│  RESERVATIONS  →  /reservation  (form)      │
│  Enter name · pick table · pick date        │
│  View all at /reservations · Cancel any     │
└─────────────────────────────────────────────┘
```

---

## Future Improvements

- User authentication and staff login system
- Table availability check before confirming reservation
- Daily sales reports and order history
- Inventory tracking with low-stock alerts
- Email or SMS confirmation for reservations
- REST API endpoints for mobile app integration
- Admin dashboard with analytics

---

## Author

<div align="center">

**Muhammad Ibrahim**
BS Computer Science (Student)

[![LinkedIn](https://img.shields.io/badge/Connect%20on%20LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/muhammad-ibrahim-o2)

</div>

---
## License

This project is developed for self learning and educational purposes.
&copy; 2026 Muhammad Ibrahim. All rights reserved.

<div align="center">

Built with Python · Flask · SQLite · Bootstrap 5

</div>
