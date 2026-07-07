# Caesar Cipher
def caesar_encrypt(text, key):
    encrypted = ""
    for ch in text:
        # Check uppercase letters
        if ch >= 'A' and ch <= 'Z':
            encrypted = encrypted + chr(((ord(ch) - ord('A') + key) % 26) + ord('A'))
        # Check lowercase letters
        elif ch >= 'a' and ch <= 'z':
            encrypted = encrypted + chr(((ord(ch) - ord('a') + key) % 26) + ord('a'))
        # Keep spaces and symbols unchanged
        else:
            encrypted = encrypted + ch
    return encrypted
def caesar_decrypt(text, key):
    return caesar_encrypt(text, -key)

# ---------------- Playfair Cipher ----------------
def build_matrix(key):
    key = key.upper()
    key = key.replace("J", "I")
    letters = []
    # Add key letters
    for ch in key:
        if ch.isalpha() and ch not in letters:
            letters.append(ch)
    # Add remaining letters
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    for ch in alphabet:
        if ch not in letters:
            letters.append(ch)
    matrix = []
    index = 0
    for i in range(5):
        row = []
        for j in range(5):
            row.append(letters[index])
            index = index + 1
        matrix.append(row)
    return matrix
def find_position(matrix, letter):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == letter:
                return i, j
def playfair_encrypt(text, key):
    matrix = build_matrix(key)
    text = text.upper()
    text = text.replace("J", "I")
    plain = ""
    for ch in text:
        if ch.isalpha():
            plain = plain + ch
    pairs = []
    i = 0
    while i < len(plain):
        first = plain[i]
        if i + 1 < len(plain):
            second = plain[i + 1]
        else:
            second = "X"
        if first == second:
            pairs.append(first + "X")
            i = i + 1
        else:
            pairs.append(first + second)
            i = i + 2
    cipher = ""
    for pair in pairs:
        a = pair[0]
        b = pair[1]
        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)
        # Same row
        if r1 == r2:
            cipher = cipher + matrix[r1][(c1 + 1) % 5]
            cipher = cipher + matrix[r2][(c2 + 1) % 5]

        # Same column
        elif c1 == c2:
            cipher = cipher + matrix[(r1 + 1) % 5][c1]
            cipher = cipher + matrix[(r2 + 1) % 5][c2]
        # Rectangle rule
        else:
            cipher = cipher + matrix[r1][c2]
            cipher = cipher + matrix[r2][c1]
    return cipher
plain_text = "SUDIP_MONARCHY"
key = 3
encrypted = caesar_encrypt(plain_text, key)
decrypted = caesar_decrypt(encrypted, key)

print("Caesar Cipher")
print("Plain Text :", plain_text)
print("Encrypted  :", encrypted)
print("Decrypted  :", decrypted)
print()
playfair_key = "SUDIP_MONARCHY"
playfair_text = "WEAPON_GUN"
playfair_cipher = playfair_encrypt(playfair_text, playfair_key)
print("Playfair Cipher")
print("Plain Text :", playfair_text)
print("Encrypted  :", playfair_cipher)
