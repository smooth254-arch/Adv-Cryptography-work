def run():
    # Simple RSA-like modular exponentiation
    # Using public exponent e=7 and modulus n=33
    msg = int(input("Enter number: "))
    print("Encrypted:", pow(msg, 7, 33))