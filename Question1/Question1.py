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
        if 'a' <= c <= 'z':
            p = ord(c) - 97
            if p <= 12:
                encrypted += chr((p + shift1 * shift2) % 13 + 97)
            else:
                encrypted += chr((p - (shift1 + shift2)) % 13 + 110)
        elif 'A' <= c <= 'Z':
            p = ord(c) - 65
            if p <= 12:
                encrypted += chr((p - shift1) % 13 + 65)
            else:
                encrypted += chr((p + shift2 ** 2) % 13 + 78)
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
        if 'a' <= c <= 'z':
            p = ord(c) - 97
            if p <= 12:
                decrypted += chr((p - shift1 * shift2) % 13 + 97)
            else:
                decrypted += chr((p + (shift1 + shift2)) % 13 + 110)
        elif 'A' <= c <= 'Z':
            p = ord(c) - 65
            if p <= 12:
                decrypted += chr((p + shift1) % 13 + 65)
            else:
                decrypted += chr((p - shift2 ** 2) % 13 + 78)
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