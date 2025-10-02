letter="abcdefghijklmnopqrstuvwxyz"

def extend_key(text, key):
    i=(len(text)//len(key)) +1
    fkey=(key*i)[:len(text)]
    return fkey


def vigenere_encryption(text,key):

    text=text.lower()
    output=""

    for t ,k in zip(text, key):
        i=letter.index(t)
        k=letter.index(k)
        output+=letter[(i+k) % 26]
    return output

def vigenere_decryption(text,key):
    output=""
    for t ,k in zip(text, key):
        i=letter.index(t)
        k=letter.index(k)
        output+=letter[(i-k) % 26]
    return output

text=input("Enter text you wanna encrypt :")
key=input("Enter the key :")
key=extend_key(text,key)
encrpted=vigenere_encryption(text,key)
print(encrpted)
decrypted=vigenere_decryption(encrpted,key)
print(decrypted)





