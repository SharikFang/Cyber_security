def modInverse(a, m):
    a = a % m
    for x in range(1, m):
        if ((a * x) % m == 1):
            return x
    return 1


def encryptAffineCipher(plaintext, a, b):
    ciphertext = ""
    for character in plaintext:
        if character.isalpha():
            if character.islower():
                encrypted_char = chr(((a * (ord(character) - ord('a')) + b) % 26) + ord('a'))
            else:
                encrypted_char = chr(((a * (ord(character) - ord('A')) + b) % 26) + ord('A'))
            ciphertext += encrypted_char
        else:
            ciphertext += character
    return ciphertext



def decryptAffineCipher(ciphertext, a, b):
    plaintext = ""
    mod_inverse = modInverse(a, 26)
    if mod_inverse == 1:
        return "Invalid 'a' value. Modular inverse does not exist."
    else:
        for character in ciphertext:
            if character.isalpha():
                if character.islower():
                    decrypted_char = chr((mod_inverse * (ord(character) - ord('a') - b) % 26) + ord('a'))
                else:
                    decrypted_char = chr((mod_inverse * (ord(character) - ord('A') - b) % 26) + ord('A'))
                plaintext += decrypted_char
            else:
                plaintext += character
    return plaintext

encryptAffineCipher('Police in boot',2,3)