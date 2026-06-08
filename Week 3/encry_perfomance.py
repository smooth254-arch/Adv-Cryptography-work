import time

start = time.time()

text = "HELLO" * 1000
key = "KEY"

def simple_xor(text, key):
    return ''.join(chr(ord(c) ^ ord(key[0])) for c in text)

encrypted = simple_xor(text, key)

end = time.time()

print("Encryption Done")
print("Time taken:", end - start, "seconds")
print("Output length:", len(encrypted))