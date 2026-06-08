from Crypto.PublicKey import RSA

key = RSA.generate(2048)

private_key = key.export_key()
public_key = key.publickey().export_key()

print("Public Key:")
print(public_key.decode())

print("\nPrivate Key:")
print(private_key.decode())