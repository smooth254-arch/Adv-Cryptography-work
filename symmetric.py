def run():
    text = input("Enter text: ")
    shift = 3
    result = ""
    for char in text:
        if char.isalpha():
            # Stay within alphabet bounds (a-z or A-Z)
            start = ord('a') if char.islower() else ord('A')
            result += chr(start + (ord(char) - start + shift) % 26)
        else:
            # Keep spaces and symbols as they are
            result += char
    print("Encrypted:", result)