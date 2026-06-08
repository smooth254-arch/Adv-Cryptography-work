from Crypto.Cipher import AES

key = b"1234567890123456"

with open("encrypted_file.bin", "rb") as f:
    nonce = f.read(16)
    tag = f.read(16)
    ciphertext = f.read()

cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)

decrypted = cipher.decrypt(ciphertext)

try:
    cipher.verify(tag)
    print("Decrypted Data:", decrypted.decode())
except ValueError:
    print("Decryption failed: Incorrect key or corrupted file")