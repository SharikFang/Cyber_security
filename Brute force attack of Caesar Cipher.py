def bruteForceCaesarCipher(ciphertext):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for shift in range(1, 26):
        decryptedText = ""
        for character in ciphertext:
            if character in alphabet:
                index = alphabet.find(character)
                shiftedIndex = (index - shift) % 26
                decryptedText += alphabet[shiftedIndex]
            else:
                decryptedText += character
        print("Shift {}: {}".format(shift, decryptedText))

bruteForceCaesarCipher('police')
