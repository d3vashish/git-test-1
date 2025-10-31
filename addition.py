from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add')
def add():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a is None or b is None:
        return jsonify({'error': 'Provide both a and b'}), 400
    result = a + b
    print(f"Addition result: {a} + {b} = {result}")  # ✅ visible in terminal
    return jsonify({'result': result})

if __name__ == "__main__":
    print("🚀 Starting Flask server on http://127.0.0.1:5000")
    app.run(host='127.0.0.1', port=5000)
