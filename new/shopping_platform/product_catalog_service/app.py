from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# Static URL of the order processing service
ORDER_PROCESSING_URL = "http://localhost:8007"

@app.route('/')
def product_catalog():
    return render_template('product_catalog.html')

@app.route('/order_processing', methods=['POST'])
def order_processing():
    # Process the order here...
    return redirect(ORDER_PROCESSING_URL)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8006)
