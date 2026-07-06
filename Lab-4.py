from math import gcd
# Generate Public and Private Keys
def generate_keypair(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 2
    while gcd(e, phi) != 1:
        e += 1
    d = pow(e, -1, phi)
    return (e, n), (d, n)
# Encryption Function
def encrypt(public_key, message):
    e, n = public_key
    cipher = []
    for ch in message:
        cipher.append(pow(ord(ch), e, n))

    return cipher
# Decryption Function
def decrypt(private_key, cipher):

    d, n = private_key

    message = ""

    for value in cipher:
        message += chr(pow(value, d, n))

    return message
# ---------------- Main Function ----------------
def main():
    # Prime numbers
    p = 61
    q = 53
    # Generate keys
    public_key, private_key = generate_keypair(p, q)

    # Message
    message = "HI"

    # Encrypt and Decrypt
    encrypted = encrypt(public_key, message)
    decrypted = decrypt(private_key, encrypted)

    # Display Output
    print("RSA Algorithm")
    print()

    print("Public Key  :", public_key)
    print("Private Key :", private_key)
    print()

    print("Original Message :", message)
    print("Encrypted Message:", encrypted)
    print("Decrypted Message:", decrypted)
# Run Program
if __name__ == "__main__":
    main()