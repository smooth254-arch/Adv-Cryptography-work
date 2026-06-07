import symmetric, asymmetric, hashing

def main():
    print("CryptographyAssignment")

    choice = input("1-Symmetric 2-Asymmetric 3-Hashing: ")

    if choice == "1":
        symmetric.run()
    elif choice == "2":
        asymmetric.run()
    elif choice == "3":
        hashing.run()
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()