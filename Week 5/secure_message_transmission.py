from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

receiver_key = RSA.generate(2048)

public_key = receiver_key.publickey()

message = "Hello Eugine"

sender_cipher = PKCS1_OAEP.new(public_key)
encrypted_message = sender_cipher.encrypt(message.encode())

print("Message Sent:")
print(encrypted_message)

receiver_cipher = PKCS1_OAEP.new(receiver_key)
decrypted_message = receiver_cipher.decrypt(encrypted_message)

print("\nMessage Received:")
print(decrypted_message.decode())