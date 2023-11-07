def encryption_affine(text, a, b):
    alphabet_maj = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet_min = alphabet_maj.lower()
    result = []

    for char in text:
        if char in alphabet_maj:
            index = alphabet_maj.index(char)
            encrypted_index = (a * index + b) % 26
            result.append(alphabet_maj[encrypted_index])
        elif char in alphabet_min:
            index = alphabet_min.index(char)
            encrypted_index = (a * index + b) % 26
            result.append(alphabet_min[encrypted_index])
        else:
            result.append(char)

    return ''.join(result)

def decryption_affine(text, a, b):
    alphabet_maj = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet_min = alphabet_maj.lower()
    result = []

    mod_inverse_a = -1
    for i in range(26):
        if (a * i) % 26 == 1:
            mod_inverse_a = i
            break

    if mod_inverse_a == -1:
        raise ValueError("The modular inverse of 'a' does not exist. Decryption is not possible.")

    for char in text:
        if char in alphabet_maj:
            index = alphabet_maj.index(char)
            decrypted_index = (mod_inverse_a * (index - b)) % 26
            result.append(alphabet_maj[decrypted_index])
        elif char in alphabet_min:
            index = alphabet_min.index(char)
            decrypted_index = (mod_inverse_a * (index - b)) % 26
            result.append(alphabet_min[decrypted_index])
        else:
            result.append(char)

    return ''.join(result)
