import hashlib
# SHA-1 Hash Function
def sha1_hash(text):
    return hashlib.sha1(text.encode()).hexdigest()
# SHA-256 Hash Function
def sha256_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()
# SHA-512 Hash Function
def sha512_hash(text):
    return hashlib.sha512(text.encode()).hexdigest()
# ---------------- Main Function ----------------
def main():
    message = "Information Security Lab"
    sha1 = sha1_hash(message)
    sha256 = sha256_hash(message)
    sha512 = sha512_hash(message)
    print("SHA Hash Algorithms")
    print()
    print("Message :", message)
    print()
    print("SHA-1   :", sha1)
    print("SHA-256 :", sha256)
    print("SHA-512 :", sha512)
    print()
    print("SHA-1 Length   :", len(sha1) * 4, "bits")
    print("SHA-256 Length :", len(sha256) * 4, "bits")
    print("SHA-512 Length :", len(sha512) * 4, "bits")
    print()
    # Avalanche Effect
    message1 = "password123"
    message2 = "password124"
    print("Avalanche Effect")
    print()
    print("Message :", message1)
    print("SHA-256 :", sha256_hash(message1))
    print()
    print("Message :", message2)
    print("SHA-256 :", sha256_hash(message2))
# Run Program
if __name__ == "__main__":
    main()