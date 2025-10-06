import base64
import random

def custom_transposition_encrypt(text):
    """
    Encrypts a string by transposing its characters in a custom pattern.
    """
    if len(text) % 2 != 0:
        text += '_' # Pad if odd length
    
    transposed_text = ""
    for i in range(0, len(text), 2):
        transposed_text += text[i+1] + text[i]
    return transposed_text

def encrypt_flag(flag):
    """
    Performs the two-step encryption process.
    """
    # Step 1: Custom Transposition
    transposed_flag = custom_transposition_encrypt(flag)
    
    # Step 2: Base64 Encoding
    encoded_flag = base64.b64encode(transposed_flag.encode('utf-8')).decode('utf-8')
    
    return encoded_flag

if __name__ == "__main__":
    flag = "flag{this_is_a_test_flag}"
    encrypted_output = encrypt_flag(flag)
    
    with open("cipher.txt", "w") as f:
        f.write(encrypted_output)
    
    print("Encryption complete. Check cipher.txt for the output.")
