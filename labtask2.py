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

# Get input from user
shift = int(input("Enter shift value (number): "))
text = input("Enter text to encrypt: ")

# Encrypt the text
encrypted_text = encryption(shift, text)

# Display results
print(f"Original text: {text}")
print(f"Encrypted text: {encrypted_text}")
print(f"Shift value: {shift}")
