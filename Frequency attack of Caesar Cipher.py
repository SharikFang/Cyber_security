
def frequencyAttackCaesarCipher(ciphertext):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    frequency = {}
    for letter in ciphertext:
        if letter.isalpha():
            letter = letter.upper()
            if letter in frequency:
                frequency[letter] += 1
            else:
                frequency[letter] = 1

    most_common_letter = max(frequency, key=frequency.get)

    shift = (alphabet.find(most_common_letter) - alphabet.find('E')) % 26

    decryptedText = ""
    for character in ciphertext:
        if character.isalpha():
            character = character.upper()
            if character in alphabet:
                index = alphabet.find(character)
                shiftedIndex = (index - shift) % 26
                decryptedText += alphabet[shiftedIndex]
            else:
                decryptedText += character
        else:
            decryptedText += character

    print("Decrypted Text:", decryptedText)

frequencyAttackCaesarCipher('police')
