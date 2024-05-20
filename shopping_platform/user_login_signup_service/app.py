# Import necessary modules
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
import os
import secrets

# Initialize Flask application
app = Flask(__name__)

# Generate a random secret key for session management
secret_key = secrets.token_hex(16)

# Set secret key for session management
app.secret_key = secret_key

# URL of the Product Catalog service
PRODUCT_CATALOG_URL = "http://localhost:8006"

# Dummy user database (replace with a real database in a production environment)
user_database = {}

# Define routes and their corresponding functions

# Route for the homepage
@app.route('/')
def index():
    return render_template('userlogin.html')

# Route for user login
@app.route('/login', methods=['POST'])
def login():
    # Retrieve username and password from the login form
    username = request.form.get('username')
    password = request.form.get('password')
    
    # Dummy authentication logic
    if username in user_database and check_password_hash(user_database[username]['password'], password):
         # Redirect to the Product Catalog page if authentication succeeds
         return redirect(PRODUCT_CATALOG_URL)
    else:
        # Flash an error message if authentication fails and render the login page again
        flash("Invalid username or password", "error")
        return render_template('userlogin.html')

# Route for user signup
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
            # Flash an error message if the username already exists
            flash("Username already exists", "error")
            return render_template('usersignup.html')
        else:
            # Hash the password before storing it in the database
            hashed_password = generate_password_hash(password)
            user_database[username] = {'password': hashed_password, 'phone': phone, 'address': address}
            # Flash a success message and redirect to the login page after successful signup
            flash("Account created successfully. Please log in.", "success")
            return redirect(url_for('index'))
    else:
        return render_template('usersignup.html')



# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8005)
