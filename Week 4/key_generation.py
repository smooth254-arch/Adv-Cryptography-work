from Crypto.Random import get_random_bytes

key = get_random_bytes(16)

print("Generated AES Key:", key)
print("Key Length:", len(key), "bytes")