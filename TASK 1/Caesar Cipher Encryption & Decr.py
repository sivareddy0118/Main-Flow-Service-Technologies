# Simple Caesar Cipher Encryption & Decryption

def encrypt(text, key):
    result = ""
    for char in text:
        if char.isalpha():  # Only shift alphabets
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char  # Keep spaces/symbols as is
    return result

def decrypt(text, key):
    return encrypt(text, -key)  # reverse shift

message = input("Enter a message: ")
key = int(input("Enter key (number): "))

encrypted = encrypt(message, key)
print("Encrypted:", encrypted)

decrypted = decrypt(encrypted, key)
print("Decrypted:", decrypted)
