from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
import os


app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flashing messages


PRODUCT_CATALOG_URL = "http://localhost:8006"


# Dummy user database (replace with a real database in a production environment)
user_database = {}

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    # Dummy authentication logic
    if username in user_database and check_password_hash(user_database[username]['password'], password):
         return redirect(PRODUCT_CATALOG_URL)
    else:
        flash("Invalid username or password", "error")
        return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Get form data
        username = request.form.get('username')
        password = request.form.get('password')
        phone = request.form.get('phone')
        address = request.form.get('address')

        # Dummy user registration logic
        if username in user_database:
            flash("Username already exists", "error")
            return render_template('signup.html')
        else:
            # Hash the password before storing it in the database
            hashed_password = generate_password_hash(password)
            user_database[username] = {'password': hashed_password, 'phone': phone, 'address': address}
            flash("Account created successfully. Please log in.", "success")
            # Redirect to the root URL after successful signup
            return redirect(url_for('index'))
    else:
        return render_template('signup.html')

@app.route('/product_catalog')
def product_catalog():
    return render_template('product_catalog.html')

@app.route('/order_processing', methods=['POST'])
def order_processing():
    # Fetch user details from session or database
    # For simplicity, let's assume the user is logged in and their details are stored in session
    username = request.form.get('username')
    user_details = user_database.get(username)

    # Process the order using user details
    # For demonstration purposes, let's just print the details
    print("Order placed by:")
    print("Username:", username)
    print("Phone:", user_details['phone'])
    print("Address:", user_details['address'])

    return render_template('order_processing.html', username=username)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8005)
