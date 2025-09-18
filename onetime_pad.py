import random
import secrets

def otp_encryption(text):
    output=""
    key=""
    for i in range(len(text)):
        num=secrets.randbelow(256)
        output+=chr((num + ord(text[i])) % 256)
        key+=chr(num)
    return output,key
    
    
def otp_decryption(encrypted_text, key):
    output = ""
    for i in range(len(encrypted_text)):
        key_num = ord(key[i])
        decrypted_char = chr((ord(encrypted_text[i]) - key_num) % 256)
        output += decrypted_char
    return output

text=input("Enter text you want  encrypt :")
text = text.encode('latin-1').decode('latin-1')
encrypted_text, encryption_key = otp_encryption(text)
print("Encrypted text:", encrypted_text)
print("Key:", encryption_key)
print(otp_decryption(encrypted_text,encryption_key))
