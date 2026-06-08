def get_valid_input():
    while True:
        text = input("Enter text to encrypt: ")

        if text.strip() == "":
            print("❌ Error: Text cannot be empty")
        elif not any(char.isalpha() for char in text):
            print("❌ Error: Text must contain letters")
        else:
            print("✔ Valid input accepted")
            return text


# Run validation
user_text = get_valid_input()
print("You entered:", user_text)