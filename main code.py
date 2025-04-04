def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():  
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char  
    return result


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)  


if __name__ == "__main__":
    message = input("Enter the message: ")
    shift_value = int(input("Enter shift value: "))

    # Encryption
    encrypted_text = caesar_encrypt(message, shift_value)
    print(f"Encrypted: {encrypted_text}")

    # Decryption
    decrypted_text = caesar_decrypt(encrypted_text, shift_value)
    print(f"Decrypted: {decrypted_text}")
