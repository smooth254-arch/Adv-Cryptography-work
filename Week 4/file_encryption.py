from Crypto.Cipher import AES

key = b"1234567890123456"

cipher = AES.new(key, AES.MODE_EAX)

with open(r"C:\Users\user\OneDrive\Desktop\Advance cryptography assignment\Week 4\file.txt", "rb") as f:
    data = f.read()

ciphertext, tag = cipher.encrypt_and_digest(data)

with open("encrypted_file.bin", "wb") as f:
    f.write(cipher.nonce)
    f.write(tag)
    f.write(ciphertext)

print("File encrypted successfully")