from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

print("RSA Encryption and decryption results")

key = RSA.generate(2048)

message = "Hello Eugine"

encryptor = PKCS1_OAEP.new(key.publickey())
ciphertext = encryptor.encrypt(message.encode())

decryptor = PKCS1_OAEP.new(key)
plaintext = decryptor.decrypt(ciphertext)

print("Original:", message)
print("Encrypted:", ciphertext)
print("Decrypted:", plaintext.decode())

if plaintext.decode() == message:
    print("TEST PASSED")
else:
    print("TEST FAILED")