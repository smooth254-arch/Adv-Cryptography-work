from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

key = get_random_bytes(16)  # 128-bit key
cipher = AES.new(key, AES.MODE_EAX)

text = "Hello Eugine"
data = text.encode()

nonce = cipher.nonce
ciphertext, tag = cipher.encrypt_and_digest(data)

print("Original:", text)
print("Encrypted:", ciphertext)