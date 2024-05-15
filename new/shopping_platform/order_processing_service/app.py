from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    # Here you would retrieve the shirt name from the product catalog service
    shirt_name = "Ronaldo Shirt"  # Replace this with the actual shirt name
    return render_template('order_processing.html', shirt_name=shirt_name)

@app.route('/process_order', methods=['POST'])
def process_order():
    shirt_name = request.form['shirt_name']
    username = request.form['username']
    address = request.form['address']
    phone = request.form['phone']
    
    # You can process the order here
    # For now, let's just print the details
    print("New Order:")
    print("Shirt Name:", shirt_name)
    print("Username:", username)
    print("Address:", address)
    print("Phone:", phone)

    # Return a success message or redirect to a thank you page
    return "Order placed successfully!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8007)
