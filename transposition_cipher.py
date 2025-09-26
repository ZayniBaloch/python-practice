import random
import string

def split_len(seq, length):
    return [seq[i:i + length] for i in range(0, len(seq), length)]

def add_padding(plaintext, key_length, padding_char='X'):
    remainder = len(plaintext) % key_length
    if remainder != 0:
        padding_needed = key_length - remainder
        plaintext += padding_char * padding_needed
    return plaintext

def validate_key(key):
    try:
        key_digits = sorted([int(d) for d in key])
        expected = list(range(1, len(key) + 1))
        return key_digits == expected
    except ValueError:
        return False

def encode(key, plaintext, preserve_non_alpha=True):
    order = {int(val): num for num, val in enumerate(key)}

    if preserve_non_alpha:
        alpha_chars = []
        non_alpha_positions = {}

        for i, char in enumerate(plaintext):
            if char.isalpha():
                alpha_chars.append(char)
            else:
                non_alpha_positions[len(alpha_chars)] = char

        alpha_text = ''.join(alpha_chars)
        padded_alpha = add_padding(alpha_text, len(key))

        ciphertext = ''
        for index in sorted(order.keys()):
            for part in split_len(padded_alpha, len(key)):
                try:
                    ciphertext += part[order[index]]
                except IndexError:
                    pass

        result = []
        alpha_index = 0

        for i in range(len(plaintext)):
            if i in non_alpha_positions:
                result.append(non_alpha_positions[i])
            elif alpha_index < len(ciphertext):
                result.append(ciphertext[alpha_index])
                alpha_index += 1

        return ''.join(result)
    else:
        padded_text = add_padding(plaintext, len(key))
        ciphertext = ''
        for index in sorted(order.keys()):
            for part in split_len(padded_text, len(key)):
                try:
                    ciphertext += part[order[index]]
                except IndexError:
                    pass
        return ciphertext

def decode(key, ciphertext, preserve_non_alpha=True):
    order = {int(val): num for num, val in enumerate(key)}
    reverse_order = {v: k for k, v in order.items()}

    if preserve_non_alpha:
        alpha_chars = []
        non_alpha_positions = {}

        for i, char in enumerate(ciphertext):
            if char.isalpha():
                alpha_chars.append(char)
            else:
                non_alpha_positions[len(alpha_chars)] = char

        alpha_cipher = ''.join(alpha_chars)
        chunks = split_len(alpha_cipher, len(key))
        plaintext_chunks = []

        for chunk in chunks:
            if len(chunk) < len(key):
                chunk += 'X' * (len(key) - len(chunk))

            decoded_chunk = [''] * len(key)
            for pos in range(len(key)):
                if pos < len(chunk):
                    decoded_chunk[reverse_order[pos]] = chunk[pos]
            plaintext_chunks.append(''.join(decoded_chunk))

        decoded_alpha = ''.join(plaintext_chunks).rstrip('X')

        result = []
        alpha_index = 0

        for i in range(len(ciphertext)):
            if i in non_alpha_positions:
                result.append(non_alpha_positions[i])
            elif alpha_index < len(decoded_alpha):
                result.append(decoded_alpha[alpha_index])
                alpha_index += 1

        return ''.join(result)
    else:
        chunks = split_len(ciphertext, len(key))
        plaintext_chunks = []

        for chunk in chunks:
            if len(chunk) < len(key):
                chunk += 'X' * (len(key) - len(chunk))

            decoded_chunk = [''] * len(key)
            for pos in range(len(key)):
                if pos < len(chunk):
                    decoded_chunk[reverse_order[pos]] = chunk[pos]
            plaintext_chunks.append(''.join(decoded_chunk))

        return ''.join(plaintext_chunks).rstrip('X')

def generate_random_key(length):
    if length > 9:
        chars = list(string.ascii_lowercase[:length])
        random.shuffle(chars)
        return ''.join(str(ord(c) - ord('a') + 1) for c in chars)
    else:
        digits = list(range(1, length + 1))
        random.shuffle(digits)
        return ''.join(str(d) for d in digits)

def get_optimal_key_length(text_length):
    if text_length <= 4:
        return 2
    elif text_length <= 8:
        return 3
    elif text_length <= 16:
        return 4
    elif text_length <= 32:
        return 5
    else:
        return 6

def display_menu():
    print("\n" + "="*50)
    print("    TRANSPOSITION CIPHER TOOL")
    print("="*50)
    print("1. Encode a message")
    print("2. Decode a message")
    print("3. Test with examples")
    print("4. Exit")
    print("="*50)

def run_tests():
    print("\nTest 1 - Original example:")
    result1 = encode('3214', 'HELLO', False)
    print(f"encode('3214', 'HELLO') = {result1}")
    decoded1 = decode('3214', result1, False)
    print(f"decode('3214', '{result1}') = {decoded1}")

    print("\nTest 2 - Mixed case with spaces:")
    test_msg = "Hello World!"
    result2 = encode('3214', test_msg, True)
    print(f"encode('3214', '{test_msg}') = {result2}")
    decoded2 = decode('3214', result2, True)
    print(f"decode('3214', '{result2}') = {decoded2}")

    print("\nTest 3 - Random key generation:")
    test_msg3 = "This is a test"
    random_key = generate_random_key(4)
    result3 = encode(random_key, test_msg3, True)
    decoded3 = decode(random_key, result3, True)
    print(f"Random key: {random_key}")
    print(f"Original: {test_msg3}")
    print(f"Encoded:  {result3}")
    print(f"Decoded:  {decoded3}")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            print("\n--- ENCODE MESSAGE ---")
            message = input("Enter message to encode: ")

            use_custom_key = input("Use custom key? (y/n): ").strip().lower()

            if use_custom_key == 'y':
                while True:
                    key = input("Enter key (e.g., '3214'): ").strip()
                    if validate_key(key):
                        break
                    print("Invalid key! Use consecutive digits starting from 1.")
            else:
                alpha_count = sum(1 for c in message if c.isalpha())
                key_length = get_optimal_key_length(alpha_count)
                key = generate_random_key(key_length)
                print(f"Generated random key: {key}")

            preserve = input("Preserve spaces and punctuation? (y/n): ").strip().lower() == 'y'

            encoded = encode(key, message, preserve)
            print(f"\nOriginal: {message}")
            print(f"Key used: {key}")
            print(f"Encoded:  {encoded}")

        elif choice == '2':
            print("\n--- DECODE MESSAGE ---")
            cipher = input("Enter message to decode: ")

            while True:
                key = input("Enter key used for encoding: ").strip()
                if validate_key(key):
                    break
                print("Invalid key! Use consecutive digits starting from 1.")

            preserve = input("Were spaces and punctuation preserved? (y/n): ").strip().lower() == 'y'

            decoded = decode(key, cipher, preserve)
            print(f"\nEncoded:  {cipher}")
            print(f"Key used: {key}")
            print(f"Decoded:  {decoded}")

        elif choice == '3':
            print("\n--- TEST EXAMPLES ---")
            run_tests()

        elif choice == '4':
            print("\nThanks for using the Transposition Cipher Tool!")
            break

        else:
            print("Invalid choice! Please enter 1, 2, 3, or 4.")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
