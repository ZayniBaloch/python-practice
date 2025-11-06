def col_encrypt(plaintext, key_size):
    plaintext = plaintext.replace(" ", "").lower()

    # pad with 'q'
    while len(plaintext) % key_size != 0:
        plaintext += "q"

    # read column-wise
    ciphertext = ""
    for col in range(key_size):
        ciphertext += plaintext[col::key_size]
    return ciphertext


def col_decrypt(ciphertext, key_size):
    n_rows = len(ciphertext) // key_size
    plaintext = ""

    # transpose back (row-wise)
    for row in range(n_rows):
        for col in range(key_size):
            plaintext += ciphertext[col * n_rows + row]

    return plaintext.rstrip("q")


# --- Main Program ---
plaintext = input("Enter text to encrypt: ")
key_size = int(input("Enter key size (e.g., 4): "))

cipher = col_encrypt(plaintext, key_size)
print(f"\n🔒 Encrypted: {cipher}")
print(f"🔓 Decrypted: {col_decrypt(cipher, key_size)}")
