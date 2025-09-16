key='abcdefghijklmnopqrstuvwxyz'
def encryption(n, plaintext):
    output=""
    for char in plaintext.lower():
        try:
            i=(key.index(char)+n)%len(key)
            output+=key[i]
        except:
            output+=char
    return output
# for decryption
def decryption(n,encrypted_text):
    output=""
    for char in encrypted_text:
        try:
            i=(key.index(char)-n)%len(key)
            output+=key[i]
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



# get input from user
shift = int(input("Enter shift value (number): "))
text = input("Enter text to encrypt: ")

# encrypt the text
encrypted_text = encryption(shift, text)
decrypted_text=decryption(shift,encrypted_text)


# Display results
print(f"Original text: {text}")
print(f"Encrypted text: {encrypted_text}")
print(f"Shift value: {shift}")
print(f"decrypted text: {decrypted_text}")

bruteforced=brute_force_decryption(encrypted_text)



