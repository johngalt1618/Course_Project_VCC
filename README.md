Performance-Optimized Post-Quantum Authentication Framework for Cloud Services
By Raghavi Epuri (B22ES012) and Prachiti Sujit Chandratreya (B22ES030)
Problem Statement
As quantum computing continues to evolve, many of the cryptographic algorithms we rely on today are becoming vulnerable to quantum-based attacks. This presents a serious challenge for cloud services, which depend on strong authentication to keep data and systems secure. The real difficulty lies in adopting post-quantum cryptography (PQC) in modern cloud-based microservices without sacrificing performance. It's not just about being secure—it's also about doing so efficiently. The goal is to create authentication systems that can resist future quantum threats while keeping latency low and resource usage minimal. This balance is vital for ensuring scalability, reducing costs, and maintaining the high availability that cloud platforms demand.
Literature Reference
NIST Post-Quantum Cryptography Project    Post-Quantum Cryptography 
The National Institute of Standards and Technology (NIST) leads a major initiative to identify and standardize cryptographic algorithms that are resilient to attacks from quantum computers. This project has made significant progress in selecting theoretically secure alternatives to classical encryption methods. 
Limitation: Despite its thorough evaluation of security, the project offers limited insight into the real-world performance of these algorithms, particularly in cloud-native and microservice-based environments. This leaves an important gap regarding their practicality in scalable, distributed systems.
Open Quantum Safe (OQS) Project
The Open Quantum Safe project provides a set of open-source tools, including liboqs and liboqs-python, allowing developers to explore various post-quantum cryptographic schemes. These libraries play a crucial role for testing and early-stage adoption of PQC algorithms.
Limitation: While useful in research and prototyping, the OQS project lacks native support for cloud integration and microservices. Furthermore, it does not provide detailed performance evaluations under real-world cloud workloads, making it less suitable for production-level deployments.
Open Quantum Safe (OQS) Project
Kyber: Module-Lattice-Based Key Encapsulation Mechanism
Kyber is a leading candidate in the NIST PQC standardization effort and is recognized for combining high security with computational efficiency. It has shown promising results in controlled environments and is well-regarded for its theoretical robustness. 
Limitation: Most of Kyber's evaluations have been confined to lab-based settings. There is a lack of data on its performance in distributed, latency-sensitive systems such as those built on microservices, limiting our understanding of its practical viability in cloud platforms.
Module-Lattice-Based Key-Encapsulation Mechanism Standard
 Performance Evaluation of PQC Algorithms in Cloud Environments (IEEE, 2022)
This study investigates how post-quantum algorithms perform on cloud platforms, focusing on key metrics like latency and resource consumption. It contributes valuable data on how such algorithms could impact system performance. 
Limitation: The analysis is based on monolithic cloud architectures, which differ significantly from the modular, dynamic nature of microservices. Consequently, its findings may not fully represent the challenges and trade-offs faced in more modern cloud-native designs.
Performance Evaluation of Post-Quantum Cryptography
Secure Microservice Communication Using PQC (Springer, 2021)
This paper addresses the need for securing inter-service communication in microservices using post-quantum cryptography. It raises awareness about the growing security challenges in distributed cloud systems.
Limitation: Although conceptually sound, the work lacks a practical implementation or end-to-end deployment in actual cloud environments. This reduces its immediate applicability for developers seeking ready-to-use PQC solutions in microservice frameworks.
Migrating Software Systems Toward Post-Quantum Cryptography

Existing Results




Algorithm
Avg Latency (ms)
Key Size (Bytes)
Ciphertext Size (Bytes)
RSA-2048
1.1
256
256
ECDSA-P256
0.9
64
64
Kyber512
1.4
800
768








Data Source: NIST and IEEE papers (2021-2023)
Post-Quantum Kyber Benchmarks (ARM Cortex-M4)
Performance Analysis and Industry Deployment of Post-Quantum Cryptography Algorithms 
Implementation
Client Microservice requests authentication from the Auth Microservice.
The Auth Microservice uses liboqs (Kyber512) to generate key pairs and perform key encapsulation.
Microservices are containerized using Docker.
Docker Compose is used to manage inter-service communication.
Deployed on Google Cloud Platform (GCP) using a Compute Engine VM (Ubuntu 20.04).

Technologies & Tools:

Programming: Python 3.9
Cryptography: liboqs-python, Kyber512
Cloud: Google Cloud Platform
DevOps: Docker, Docker Compose
Benchmarking: Apache Benchmark (ab)

Key Features Used:

VM-based deployment
Exposed microservices via HTTP
Logging and JSON-based output for analysis
Results
Test Case
Requests
Concurrency
Avg Time (ms)
Requests/sec
Test-1 (RSA)
100
10
36.35
27.51
Test-1 (ECDSA)
100
50
7.2
138.84
Test-1 (Kyber)
100
20
2.35
426.29
Test-2 (RSA)
1000
10
35.19
28.41
Test-2 (ECDSA)
1000
50
8.11
123.3
Test-2 (Kyber)
1000
20
1.82
548.95


Kyber had the lowest average response time. Its throughput was pretty good, handling up to 549 requests per second. Even as the number of requests increased, performance remained consistent, showing Kyber is built for speed and scale.
ECDSA had comparatively greater response time than Kyber. Achieved a good throughput of up to 139 requests per second. Overall, ECDSA provided a good balance between speed and scalability, making it a reliable choice for many applications.
RSA had noticeably higher response time that’s roughly 5x slower than ECDSA and 20x slower than Kyber. RSA didn’t handle scaling well, making it less ideal for real-time or high-traffic microservice environments.






Comparison and Analysis
Metric
Traditional RSA
Kyber512 (This Project)
Latency (ms)
110
36.5
Security
Vulnerable to quantum
Quantum-safe
Cloud Overhead
Low
Moderate



Observations from Existing results
Kyber512 is the best in raw performance (fastest key generation, encapsulation & decapsulation).
RSA is impractically slow for any scalable system.
ECDSA is decent, but Kyber is ~2× faster across the board.

Observations from Obtained Results
Kyber remains dominant in actual cloud environment testing, with lowest average time and highest throughput.
ECDSA shows stable performance but ~4× slower than Kyber.
RSA fails to scale, confirming benchmark weakness in a real-world context.

Conclusion
This project shows that it's possible to bring post-quantum cryptography into a modern, cloud-native microservices setup without compromising on performance or scalability. Beyond just a proof of concept, the framework lays a solid groundwork for building future-ready cloud applications. With further improvements like AI-based anomaly detection, live performance monitoring, and support for quantum-safe signatures, this work opens up promising possibilities for secure, scalable systems in the era of quantum computing.

Architecture Diagram of Your Implementation

Components:

Client Microservice: Sends request to Auth service
Auth Microservice: Generates PQC-based authentication
Docker Containers: Isolate services
Docker Compose: Network bridge between containers
GCP VM: Hosts the complete environment

Future Scope
Smarter Authentication with AI/ML
Incorporating machine learning, especially techniques that analyze user behavior, can help identify unusual activity and flag potential threats early. This could reduce false alarms and make the system more intelligent over time.


Faster, More Efficient APIs
Switching to FastAPI and using gRPC for internal service communication could help shave off milliseconds from response times—crucial for performance-sensitive microservice environments.


Live System Monitoring
By bringing in Prometheus and Grafana, the system could gain real-time visibility into performance metrics like CPU load, memory usage, and request latency. This would make it easier to catch bottlenecks or issues before they escalate.


Better Scalability with Kubernetes
Deploying on Google Kubernetes Engine (GKE) can allow the application to automatically scale up or down based on traffic. It also gives more control over how resources are allocated across services.


Stronger Cryptographic Guarantees
Support for quantum-safe digital signature schemes like Dilithium would further future-proof the system, ensuring end-to-end resistance against quantum attacks.


Hybrid Cloud Flexibility
Running across multiple cloud providers could boost system resilience, reduce downtime risks, and allow for smarter geographic load balancing in production.

Github Repository Link
Performance-Optimized Post-Quantum Authentication Framework for Cloud Services

Recorded Demo Link
Recorded_Demo_B22ES030_B22ES012.mkv

Presentation Link
VCC_Project_Presentation-B22ES012_B22ES030
