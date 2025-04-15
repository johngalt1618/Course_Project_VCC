from flask import Flask, jsonify
import time
import random

app = Flask(__name__)

# Hardcoding RSA, ECDSA, and Kyber algorithms as functions.
def rsa_algorithm(data):
    # Simulating RSA encryption and decryption
    time.sleep(random.uniform(0.05, 0.1))  # Simulating time delay for RSA
    return "RSA Result: " + str(data)

def ecdsa_algorithm(data):
    # Simulating ECDSA signing and verification
    time.sleep(random.uniform(0.02, 0.07))  # Simulating time delay for ECDSA
    return "ECDSA Result: " + str(data)

def kyber_algorithm(data):
    # Simulating Kyber encryption and decryption
    time.sleep(random.uniform(0.03, 0.08))  # Simulating time delay for Kyber
    return "Kyber Result: " + str(data)

@app.route('/test_rsa')
def test_rsa():
    start_time = time.time()
    result = rsa_algorithm("test data")
    elapsed_time = (time.time() - start_time) * 1000  # Convert to milliseconds
    return jsonify({"algorithm": "RSA", "time_taken_ms": elapsed_time, "result": result})

@app.route('/test_ecdsa')
def test_ecdsa():
    start_time = time.time()
    result = ecdsa_algorithm("test data")
    elapsed_time = (time.time() - start_time) * 1000  # Convert to milliseconds
    return jsonify({"algorithm": "ECDSA", "time_taken_ms": elapsed_time, "result": result})

@app.route('/test_kyber')
def test_kyber():
    start_time = time.time()
    result = kyber_algorithm("test data")
    elapsed_time = (time.time() - start_time) * 1000  # Convert to milliseconds
    return jsonify({"algorithm": "Kyber", "time_taken_ms": elapsed_time, "result": result})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

