import random

def otp_encryption(text):
    output=""
    key=""
    for i in range(len(text)):
        num=random.randint(0,255)
        output+=chr((num + ord(text[i])) % 256)
        key+=chr(num)
    return output,key
    
text=input("Enter text you want  encrypt :")
encrypted_text, encryption_key = otp_encryption(text)
print("Encrypted text:", encrypted_text)
print("Key:", encryption_key)
