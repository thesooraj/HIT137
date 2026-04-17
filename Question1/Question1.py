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
                # First half a-m: shift forward by shift1 * shift2
                encrypted += shift_forward(c, (shift1 * shift2) % 13)
            else:
                # Second half n-z: shift backward by shift1 + shift2
                encrypted += chr((p - (shift1 + shift2)) % 13 + 110)
        elif 'A' <= c <= 'Z':
            p = ord(c) - 65
            if p <= 12:
                # First half A-M: shift backward by shift1
                encrypted += shift_backward_upper(c, shift1 % 13)
            else:
                # Second half N-Z: shift forward by shift2 squared
                encrypted += chr((p + shift2 ** 2) % 13 + 78)
        else:
            encrypted += c
    
    with open("encrypted_text.txt", "w") as f:
        f.write(encrypted)
    print("Encryption completed → encrypted_text.txt")


# ---------------- DECRYPTION ---------------- #

def decrypt_file(shift1, shift2):
    with open("encrypted_text.txt", "r") as f:
        text = f.read()
    
    decrypted = ""
    for c in text:
        if 'a' <= c <= 'z':
            p = ord(c) - 97
            if p <= 12:
                # Reverse first half: shift backward by shift1 * shift2
                decrypted += shift_backward(c, (shift1 * shift2) % 13)
            else:
                # Reverse second half: shift forward by shift1 + shift2
                decrypted += chr((p + (shift1 + shift2)) % 13 + 110)
        elif 'A' <= c <= 'Z':
            p = ord(c) - 65
            if p <= 12:
                # Reverse first half: shift forward by shift1
                decrypted += shift_forward_upper(c, shift1 % 13)
            else:
                # Reverse second half: shift backward by shift2 squared
                decrypted += chr((p - shift2 ** 2) % 13 + 78)
        else:
            decrypted += c
    
    with open("decrypted_text.txt", "w") as f:
        f.write(decrypted)
    print("Decryption completed → decrypted_text.txt")



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
