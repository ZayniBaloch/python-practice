
letters="abcdefghijklmnopqrstuvwxyz"
def encryption(n, plaintext):
    output=""
    for char in plaintext.lower():
        try:
            i=(letters.index(char)+n)%len(letters)
            output+=letters[i]
        except:
            output+=char
    return output
# decryption
def decryption(n,encrypted_text):
    output=""
    for char in encrypted_text:
        try:
            i=(letters.index(char)-n)%len(letters)
            output+=letters[i]
        except:
            output+=char
    return output

# now try to bruteforce it and shifts known
def brute_force_decryption(encrypted_text):
    results=[]
    for int in range(26):
        output=""
        for char in encrypted_text:
            try:
                i=(key.index(char)-int)%len(key)
                output+=key[i]
            except:
                output+=char
        print(f"shift={int}: {output}")
        results.append((int,output))
    return results




key=input("Enter the key: ")
text = input("Enter text to encrypt: ")


if len(key) < 5:
    print("Error: Key must be greater than 5 characters!")
    exit()

if len(text) < 16:
    print("text length must be greater then 16 !")
    exit()

shift=(len(key) * 12) % 26


encrypted_text = encryption(shift, text)
decrypted_text=decryption(shift,encrypted_text)



print(f"Original text: {text}")
print(f"Encrypted text: {encrypted_text}")
print(f"Shift value: {shift}")
print(f"decrypted text: {decrypted_text}")

# bruteforced=brute_force_decryption(encrypted_text)



