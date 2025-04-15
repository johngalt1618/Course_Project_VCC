import requests
import time
import concurrent.futures
from flask import Flask, jsonify

app = Flask(__name__)

# Function to send a single request to the URL
def send_request(url):
    response = requests.get(url)
    return response.json()

# Benchmarking function to simulate concurrent requests
def benchmark_test(requests_count, concurrency, algorithm):
    url = f"http://auth_service:8080/test_{algorithm.lower()}"
    start_time = time.time()
    
    # Using ThreadPoolExecutor to simulate concurrency
    with concurrent.futures.ThreadPoolExecutor(max_workers=concurrency) as executor:
        futures = [executor.submit(send_request, url) for _ in range(requests_count)]
        # Wait for all requests to complete
        concurrent.futures.wait(futures)
    
    end_time = time.time()

    avg_time = (end_time - start_time) * 1000 / requests_count  # Time per request in ms
    requests_per_sec = requests_count / (end_time - start_time)
    
    return avg_time, requests_per_sec

@app.route('/benchmark', methods=['GET'])
def benchmark():
    # Test cases, you can adjust these as needed
    test_cases = [
        {"requests": 100, "concurrency": 10, "algorithm": "RSA"},
        {"requests": 100, "concurrency": 50, "algorithm": "ECDSA"},
        {"requests": 100, "concurrency": 20, "algorithm": "Kyber"}
    ]

    results = []
    
    # Run the benchmark tests
    for case in test_cases:
        avg_time, requests_sec = benchmark_test(case["requests"], case["concurrency"], case["algorithm"])
        result = {
            "algorithm": case["algorithm"],
            "requests": case["requests"],
            "concurrency": case["concurrency"],
            "avg_time_ms": round(avg_time, 2),
            "requests_per_sec": round(requests_sec, 2)
        }
        results.append(result)

    return jsonify(results)

if __name__ == "__main__":
    # Start the Flask app on port 5000
    app.run(host='0.0.0.0', port=5000)  # Listening on port 5000
