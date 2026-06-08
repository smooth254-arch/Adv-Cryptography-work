from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

key = RSA.generate(2048)

public_key = key.publickey()

encryptor = PKCS1_OAEP.new(public_key)

message = "Hello Eugine"

ciphertext = encryptor.encrypt(message.encode())

decryptor = PKCS1_OAEP.new(key)

plaintext = decryptor.decrypt(ciphertext)

print("Encrypted:", ciphertext)
print("Decrypted:", plaintext.decode())