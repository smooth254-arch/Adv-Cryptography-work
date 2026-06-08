import time
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

data = b"Hello Eugine" * 10000

key = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_EAX)

start = time.time()
ciphertext, tag = cipher.encrypt_and_digest(data)
end = time.time()

print("AES Encryption Completed")
print("Time Taken:", end - start, "seconds")
print("Data Size:", len(data))