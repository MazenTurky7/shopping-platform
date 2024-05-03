from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/authenticate')
def authenticate_user():
    # Dummy authentication logic
    return jsonify({"message": "User authenticated successfully"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
