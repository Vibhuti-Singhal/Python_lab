import sys
# Caesar Cipher function
def caesar(text, shift):
    result = ""
    for c in text:
        if c.isupper():
            # Shift uppercase letters
            result += chr((ord(c) - 65 + shift) % 26 + 65)
        elif c.islower():
            # Shift lowercase letters
            result += chr((ord(c) - 97 + shift) % 26 + 97)
        else:
            # Keep spaces and special characters unchanged
            result += c
    return result

# Check for command-line input
if len(sys.argv) >= 3:
    text = sys.argv[1]
    shift = int(sys.argv[2])
    print("Encrypted:", caesar(text, shift))
    print("Decrypted:", caesar(text, -shift))

# Otherwise take input from the user
else:
    text = input("Enter text: ")
    shift = int(input("Enter shift: "))
    choice = input("Enter E for Encryption or D for Decryption: ").upper()

    if choice == "E":
        print("Encrypted:", caesar(text, shift))

    elif choice == "D":
        print("Decrypted:", caesar(text, -shift))

    else:
        print("Invalid choice!")