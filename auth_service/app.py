import time
from flask import Flask, jsonify
import random
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from ecdsa import SigningKey, VerifyingKey

app = Flask(__name__)

# RSA Algorithm Implementation
def generate_rsa_keys():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key = private_key.public_key()

    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )

    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    return private_key, public_key

def rsa_algorithm(data):
    private_key, public_key = generate_rsa_keys()

    # Simulate encryption and decryption with RSA
    encrypted = public_key.encrypt(
        data.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    decrypted = private_key.decrypt(
        encrypted,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    return f"RSA Encrypted: {encrypted}, Decrypted: {decrypted.decode()}"

# ECDSA Algorithm Implementation
def ecdsa_algorithm(data):
    # Generate ECDSA keys
    sk = SigningKey.generate(curve='secp256k1')
    vk = sk.get_verifying_key()

    # Simulate signing and verifying data
    signature = sk.sign(data.encode())

    is_valid = vk.verify(signature, data.encode())

    return f"ECDSA Signature: {signature.hex()}, Verification: {is_valid}"

# Kyber Algorithm Simulation (Basic implementation)
def kyber_algorithm(data):
    # Simulated Kyber Key Generation (simplified lattice-like behavior)
    def generate_kyber_keypair():
        # Simplified: Generate public and private "keys"
        private_key = random.randint(1, 1000)  # Random private key
        public_key = private_key * random.randint(1, 1000)  # Public key is a product of private key and random number
        return private_key, public_key

    def kyber_encrypt(public_key, data):
        # Simplified encryption: Data is multiplied by the public key
        return data * public_key
    
    def kyber_decrypt(private_key, encrypted_data):
        # Simplified decryption: Divide the encrypted data by private key (inverse operation)
        return encrypted_data // private_key  # Use integer division for simplicity
    
    private_key, public_key = generate_kyber_keypair()

    # Simulate encrypting and decrypting a message with Kyber
    encrypted_data = kyber_encrypt(public_key, len(data))  # Encrypting data based on its length
    decrypted_data = kyber_decrypt(private_key, encrypted_data)  # Decrypting the encrypted data

    return f"Kyber Encrypted: {encrypted_data}, Decrypted: {decrypted_data}"

# Flask Routes
@app.route('/test_rsa')
def test_rsa():
    start_time = time.time()
    result = rsa_algorithm("test data")
    elapsed_time = (time.time() - start_time) * 1000  # Convert to milliseconds
    return jsonify({
        "algorithm": "RSA",
        "time_taken_ms": elapsed_time,
        "result": result
    })

@app.route('/test_ecdsa')
def test_ecdsa():
    start_time = time.time()
    result = ecdsa_algorithm("test data")
    elapsed_time = (time.time() - start_time) * 1000  # Convert to milliseconds
    return jsonify({
        "algorithm": "ECDSA",
        "time_taken_ms": elapsed_time,
        "result": result
    })

@app.route('/test_kyber')
def test_kyber():
    start_time = time.time()
    result = kyber_algorithm("test data")
    elapsed_time = (time.time() - start_time) * 1000  # Convert to milliseconds
    return jsonify({
        "algorithm": "Kyber",
        "time_taken_ms": elapsed_time,
        "result": result
    })

# Running the Flask app
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
