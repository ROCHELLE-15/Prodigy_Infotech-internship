def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                encrypted_text += chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            elif char.isupper():
                encrypted_text += chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                decrypted_text += chr((ord(char) - ord('a') - shift_amount) % 26 + ord('a'))
            elif char.isupper():
                decrypted_text += chr((ord(char) - ord('A') - shift_amount) % 26 + ord('A'))
        else:
            decrypted_text += char
    return decrypted_text

def main():
    while True:
        choice = input("Do you want to (e)ncrypt or (d)ecrypt a message? Enter 'e' or 'd': ").lower()
        if choice not in ['e', 'd']:
            print("Invalid choice. Please enter 'e' for encrypt or 'd' for decrypt.")
            continue
        
        message = input("Enter the message: ")
        shift = int(input("Enter the shift value: "))
        
        if choice == 'e':
            result = encrypt(message, shift)
            print(f"Encrypted message: {result}")
        elif choice == 'd':
            result = decrypt(message, shift)
            print(f"Decrypted message: {result}")
        
        another = input("Do you want to encrypt/decrypt another message? (yes/no): ").lower()
        if another != 'yes':
            break

if __name__ == "__main__":
    main()
