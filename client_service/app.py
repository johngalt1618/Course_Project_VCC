import requests
import time

def send_request(url):
    response = requests.get(url)
    return response.json()

def benchmark_test(requests_count, concurrency, algorithm):
    url = f"http://auth_service:5000/test_{algorithm.lower()}"
    start_time = time.time()
    for _ in range(requests_count):
        send_request(url)
    end_time = time.time()

    avg_time = (end_time - start_time) * 1000 / requests_count  # Time per request in ms
    requests_per_sec = requests_count / (end_time - start_time)
    
    return avg_time, requests_per_sec

if __name__ == "__main__":
    # You can replace these values with whatever test cases you want
    test_cases = [
        {"requests": 100, "concurrency": 10, "algorithm": "RSA"},
        {"requests": 1000, "concurrency": 50, "algorithm": "ECDSA"},
        {"requests": 500, "concurrency": 20, "algorithm": "Kyber"}
    ]

    for case in test_cases:
        avg_time, requests_sec = benchmark_test(case["requests"], case["concurrency"], case["algorithm"])
        print(f"Test-{case['algorithm']} | Requests: {case['requests']} | Concurrency: {case['concurrency']}")
        print(f"Avg Time (ms): {avg_time} | Requests/sec: {requests_sec}")

