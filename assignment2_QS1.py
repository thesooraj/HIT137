import os

# This part makes sure the script finds the files in the same folder
# My lecturer said this is the safest way to handle file paths
current_folder = os.path.dirname(os.path.abspath(__file__))

def encrypt_logic(text, s1, s2):
    result = ""
    for char in text:
        # Check for lowercase letters first
        if char.islower():
            # first half: a to m
            if 'a' <= char <= 'm':
                shift = s1 * s2
                # use 97 for 'a'
                new_pos = (ord(char) - 97 + shift) % 26
                result += chr(new_pos + 97)
            # second half: n to z
            else:
                shift = s1 + s2
                new_pos = (ord(char) - 97 - shift) % 26
                result += chr(new_pos + 97)
        
        # Check for uppercase letters
        elif char.isupper():
            # first half: A to M
            if 'A' <= char <= 'M':
                shift = s1
                # use 65 for 'A'
                new_pos = (ord(char) - 65 - shift) % 26
                result += chr(new_pos + 65)
            # second half: N to Z
            else:
                shift = s2 * s2
                new_pos = (ord(char) - 65 + shift) % 26
                result += chr(new_pos + 65)
        
        # Numbers and symbols don't change
        else:
            result += char
    return result

def decrypt_logic(text, s1, s2):
    result = ""
    for char in text:
        if char.islower():
            if 'a' <= char <= 'm':
                shift = s1 * s2
                # Move backward for decryption
                new_pos = (ord(char) - 97 - shift) % 26
                result += chr(new_pos + 97)
            else:
                shift = s1 + s2
                # Move forward (reverse of backward)
                new_pos = (ord(char) - 97 + shift) % 26
                result += chr(new_pos + 97)
        
        elif char.isupper():
            if 'A' <= char <= 'M':
                shift = s1
                new_pos = (ord(char) - 65 + shift) % 26
                result += chr(new_pos + 65)
            else:
                shift = s2 * s2
                new_pos = (ord(char) - 65 - shift) % 26
                result += chr(new_pos + 65)
        else:
            result += char
    return result

# Main part of the program
def main():
    try:
        # Get numbers from the user
        shift1 = int(input("Enter first shift value: "))
        shift2 = int(input("Enter second shift value: "))

        # 1. Read the original file
        path_raw = os.path.join(current_folder, "raw_text.txt")
        file1 = open(path_raw, "r")
        original_data = file1.read()
        file1.close()

        # 2. Encrypt and save
        encrypted_data = encrypt_logic(original_data, shift1, shift2)
        path_enc = os.path.join(current_folder, "encrypted_text.txt")
        file2 = open(path_enc, "w")
        file2.write(encrypted_data)
        file2.close()
        print("Done encrypting!")

        # 3. Decrypt and save to a new file
        decrypted_data = decrypt_logic(encrypted_data, shift1, shift2)
        path_dec = os.path.join(current_folder, "decrypted_text.txt")
        file3 = open(path_dec, "w")
        file3.write(decrypted_data)
        file3.close()
        print("Done decrypting!")

        # 4. Final verification check
        if original_data == decrypted_data:
            print("Everything matches! Decryption was successful.")
        else:
            print("Something went wrong, the files are different.")

    except Exception as e:
        print("Check if raw_text.txt is in the folder. Error:", e)

# Run the main function
main()