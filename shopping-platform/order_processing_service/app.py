from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/process_order')
def process_order():
    # Dummy order processing logic
    return jsonify({"message": "Order processed successfully"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8002)
