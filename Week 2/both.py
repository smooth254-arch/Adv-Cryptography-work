def caesar_encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char

    return result
def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


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


def vigenere_decrypt(text, key):
    result = ""
    key = key.lower()
    key_index = 0

    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 97
            shift_base = 65 if char.isupper() else 97

            result += chr((ord(char) - shift_base - shift) % 26 + shift_base)
            key_index += 1
        else:
            result += char

    return result


# ---------------- TEST OUTPUT ----------------
text = "Hello Eugine"

print("ORIGINAL TEXT:", text)

# Caesar
c_encrypted = caesar_encrypt(text, 3)
c_decrypted = caesar_decrypt(c_encrypted, 3)

print("\n--- CAESAR ---")
print("Encrypted:", c_encrypted)
print("Decrypted:", c_decrypted)

# Vigenere
v_encrypted = vigenere_encrypt(text, "KEY")
v_decrypted = vigenere_decrypt(v_encrypted, "KEY")

print("\n--- VIGENERE ---")
print("Encrypted:", v_encrypted)
print("Decrypted:", v_decrypted)