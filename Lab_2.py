# Vigenere Cipher
def vigenere_encrypt(text, key):
    key = key.upper()
    encrypted = ""
    j = 0

    for ch in text:
        if ch.isalpha():
            shift = ord(key[j % len(key)]) - ord('A')
            if ch.isupper():
                base = ord('A')
            else:
                base = ord('a')
            encrypted += chr((ord(ch) - base + shift) % 26 + base)
            j += 1
        else:
            encrypted += ch
    return encrypted
def vigenere_decrypt(text, key):
    key = key.upper()
    decrypted = ""
    j = 0
    for ch in text:
        if ch.isalpha():
            shift = ord(key[j % len(key)]) - ord('A')
            if ch.isupper():
                base = ord('A')
            else:
                base = ord('a')
            decrypted += chr((ord(ch) - base - shift) % 26 + base)
            j += 1
        else:
            decrypted += ch
    return decrypted
# ---------------- Rail Fence Cipher ----------------
def rail_fence_encrypt(text, rails):
    fence = []
    for i in range(rails):
        fence.append([])
    rail = 0
    direction = 1

    for ch in text:
        fence[rail].append(ch)
        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1
        rail += direction
    cipher = ""
    for row in fence:
        cipher += "".join(row)
    return cipher
def rail_fence_decrypt(cipher, rails):
    pattern = []
    rail = 0
    direction = 1
    for i in range(len(cipher)):
        pattern.append(rail)
        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1
        rail += direction
    counts = []
    for r in range(rails):
        counts.append(pattern.count(r))
    rows = []
    index = 0

    for count in counts:
        rows.append(list(cipher[index:index + count]))
        index += count
    pointers = [0] * rails
    plain = ""
    for r in pattern:
        plain += rows[r][pointers[r]]
        pointers[r] += 1
    return plain
# ---------------- Main Function ----------------
def main():
    # Vigenere Cipher
    plain_text = "ATTACKATDAWN"
    key = "LEMON"

    encrypted = vigenere_encrypt(plain_text, key)
    decrypted = vigenere_decrypt(encrypted, key)

    print("Vigenere Cipher")
    print("Plain Text :", plain_text)
    print("Encrypted  :", encrypted)
    print("Decrypted  :", decrypted)

    print()

    # Rail Fence Cipher
    plain_text = "DEFENDTHEEASTWALL"
    rails = 3

    encrypted = rail_fence_encrypt(plain_text, rails)
    decrypted = rail_fence_decrypt(encrypted, rails)

    print("Rail Fence Cipher")
    print("Plain Text :", plain_text)
    print("Encrypted  :", encrypted)
    print("Decrypted  :", decrypted)
# Run Program
if __name__ == "__main__":
    main()