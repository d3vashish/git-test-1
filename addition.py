from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add', methods=['GET'])
def add_numbers():
    # Get numbers from query parameters
    num1 = request.args.get('num1', type=float)
    num2 = request.args.get('num2', type=float)

    # Validate input
    if num1 is None or num2 is None:
        return jsonify({"error": "Please provide both num1 and num2 parameters"}), 400

    result = num1 + num2
    return jsonify({"num1": num1, "num2": num2, "sum": result})

if __name__ == '__main__':
    app.run(debug=True)
