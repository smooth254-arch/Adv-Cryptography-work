def rc4(key, text):
    S = list(range(256))
    j = 0

    # KSA
    for i in range(256):
        j = (j + S[i] + ord(key[i % len(key)])) % 256
        S[i], S[j] = S[j], S[i]

    # PRGA
    i = j = 0
    result = []

    for char in text:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        result.append(chr(ord(char) ^ K))

    return ''.join(result)


encrypted = rc4("KEY", "HELLO")
print("RC4 Encrypted:", encrypted)