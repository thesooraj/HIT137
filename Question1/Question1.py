import os

# ---------------- SHIFT HELPERS ---------------- #

def shift_forward(c, shift):
    return chr((ord(c) - ord('a') + shift) % 26 + ord('a'))

def shift_backward(c, shift):
    return chr((ord(c) - ord('a') - shift) % 26 + ord('a'))

def shift_forward_upper(c, shift):
    return chr((ord(c) - ord('A') + shift) % 26 + ord('A'))

def shift_backward_upper(c, shift):
    return chr((ord(c) - ord('A') - shift) % 26 + ord('A'))


# ---------------- ENCRYPTION ---------------- #

def encrypt_file(shift1, shift2):
    with open("raw_text.txt", "r") as f:
        text = f.read()

    encrypted = ""

    for c in text:
        # lowercase
        if 'a' <= c <= 'z':
            if c <= 'm':
                shift = shift1 * shift2
                encrypted += shift_forward(c, shift)
            else:
                shift = shift1 + shift2
                encrypted += shift_backward(c, shift)

        # uppercase
        elif 'A' <= c <= 'Z':
            if c <= 'M':
                shift = shift1
                encrypted += shift_backward_upper(c, shift)
            else:
                shift = shift2 ** 2
                encrypted += shift_forward_upper(c, shift)

        # others unchanged
        else:
            encrypted += c

    with open("encrypted_text.txt", "w") as f:
        f.write(encrypted)


# ---------------- DECRYPTION ---------------- #

def decrypt_file(shift1, shift2):
    with open("encrypted_text.txt", "r") as f:
        text = f.read()

    decrypted = ""

    for c in text:
        # lowercase
        if 'a' <= c <= 'z':
            if c <= 'm':
                shift = shift1 * shift2
                decrypted += shift_backward(c, shift)
            else:
                shift = shift1 + shift2
                decrypted += shift_forward(c, shift)

        # uppercase
        elif 'A' <= c <= 'Z':
            if c <= 'M':
                shift = shift1
                decrypted += shift_forward_upper(c, shift)
            else:
                shift = shift2 ** 2
                decrypted += shift_backward_upper(c, shift)

        # others unchanged
        else:
            decrypted += c

    with open("decrypted_text.txt", "w") as f:
        f.write(decrypted)


# ---------------- VERIFICATION ---------------- #

def verify():
    with open("raw_text.txt", "r") as f:
        original = f.read()

    with open("decrypted_text.txt", "r") as f:
        decrypted = f.read()

    if original == decrypted:
        print("Decryption successful ✅")
    else:
        print("Decryption failed ❌")


# ---------------- MAIN PROGRAM ---------------- #

def main():
    try:
        shift1 = int(input("Enter shift1: "))
        shift2 = int(input("Enter shift2: "))
    except:
        print("Invalid input. Please enter integers.")
        return

    encrypt_file(shift1, shift2)
    print("Encryption completed → encrypted_text.txt")

    decrypt_file(shift1, shift2)
    print("Decryption completed → decrypted_text.txt")

    verify()


if __name__ == "__main__":
    main()