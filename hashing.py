import hashlib

def run():
    text = input("Enter text: ")
    print("Hash:", hashlib.sha256(text.encode()).hexdigest())