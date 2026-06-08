def vigenere_encrypt(text, key):
    result = ""
    key = key.lower()
    key_index = 0

    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 97
            shift_base = 65 if char.isupper() else 97

            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
            key_index += 1
        else:
            result += char

    return result


text = "HELLO HAMZA"
key = "KEY"

encrypted = vigenere_encrypt(text, key)
print("Text:", text)
print("Key:", key)
print("Encrypted:", encrypted)