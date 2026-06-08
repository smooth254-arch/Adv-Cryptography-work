from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

key = RSA.generate(2048)

public_key = key.publickey()

cipher = PKCS1_OAEP.new(public_key)

message = "Hello Eugine"
ciphertext = cipher.encrypt(message.encode())

print("Original Message:", message)
print("Encrypted Message:", ciphertext)