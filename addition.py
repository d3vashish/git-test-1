from flask import Flask, request, jsonify
import subprocess
import time
import requests
import multiprocessing

app = Flask(__name__)

@app.route('/add')
def add():
    try:
        a = float(request.args.get('a', 0))
        b = float(request.args.get('b', 0))
        return jsonify({'result': a + b})
    except ValueError:
        return jsonify({'error': 'Invalid input'}), 400

def run_flask():
    app.run(host='127.0.0.1', port=5000)

if __name__ == "__main__":
    # Run Flask app in background
    p = multiprocessing.Process(target=run_flask)
    p.start()
    time.sleep(3)  # Give it time to start

    try:
        r = requests.get("http://127.0.0.1:5000/add?a=10&b=15")
        if r.status_code == 200 and r.json().get("result") == 25:
            print("✅ Flask addition test passed!")
        else:
            print("❌ Test failed:", r.text)
            exit(1)
    finally:
        p.terminate()
        p.join()
