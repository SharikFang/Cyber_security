def encryptVigenereCipher(plaintext, key):
    ciphertext = ""
    key_length = len(key)
    key_as_int = [ord(i) for i in key.upper()]
    plaintext_index = 0
    for character in plaintext:
        if character.isalpha():
            if character.islower():
                shift = (ord(character) - ord('a') + key_as_int[plaintext_index % key_length] - ord('A')) % 26
                encrypted_char = chr(shift + ord('a'))
            else:
                shift = (ord(character) - ord('A') + key_as_int[plaintext_index % key_length] - ord('A')) % 26
                encrypted_char = chr(shift + ord('A'))
            ciphertext += encrypted_char
            plaintext_index += 1
        else:
            ciphertext += character
    return ciphertext

def decryptVigenereCipher(ciphertext, key):
    plaintext = ""
    key_length = len(key)
    key_as_int = [ord(i) for i in key.upper()]
    ciphertext_index = 0
    for character in ciphertext:
        if character.isalpha():
            if character.islower():
                shift = (ord(character) - ord('a') - key_as_int[ciphertext_index % key_length] + ord('A')) % 26
                decrypted_char = chr(shift + ord('a'))
            else:
                shift = (ord(character) - ord('A') - key_as_int[ciphertext_index % key_length] + ord('A')) % 26
                decrypted_char = chr(shift + ord('A'))
            plaintext += decrypted_char
            ciphertext_index += 1
        else:
            plaintext += character
    return plaintext

encryptVigenereCipher('police','cip')