#Write a Python program to create a Caesar Cipher Tool that takes a text message and a
#  user-specified shift value as input. The program should encode or decode the message by
#  shifting alphabetic characters while keeping spaces, numbers, and special symbols 
# unchanged. The program should also validate the input using basic string methods.
# Caesar Cipher Program

def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            # Handle uppercase letters
            if char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))

            # Handle lowercase letters
            else:
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))

        else:
            # Keep spaces, numbers and special characters unchanged
            result += char

    return result


# Taking input from the user
text = input("Enter the message: ")

# Validate that message is not empty
if text.strip() == "":
    print("Error: Message cannot be empty.")
else:
    shift_input = input("Enter shift value: ")

    # Check whether shift value is a number
    if shift_input.lstrip('-').isdigit():
        shift = int(shift_input)

        choice = input("Enter E for Encode or D for Decode: ").upper()

        if choice == "E":
            result = caesar_cipher(text, shift)
            print("Encrypted message:", result)

        elif choice == "D":
            result = caesar_cipher(text, -shift)
            print("Decrypted message:", result)

        else:
            print("Invalid choice. Please enter E or D.")

    else:
        print("Error: Shift value must be an integer.")