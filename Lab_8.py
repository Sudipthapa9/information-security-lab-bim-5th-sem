import hashlib
# MD5 Hash Function
def md5_hash(text):
    return hashlib.md5(text.encode()).hexdigest()
# ---------------- Main Function ----------------
def main():
    # Basic Hashing
    messages = ["HelloWorld", "helloworld", "Sankalpa College"]
    print("MD5 Hash Values")
    print()
    for message in messages:
        print("Message :", message)
        print("Hash    :", md5_hash(message))
        print()
    # Avalanche Effect
    message1 = "HelloWorld"
    message2 = "HelloWorlds"
    print("Avalanche Effect")
    print()
    print("Message :", message1)
    print("Hash    :", md5_hash(message1))
    print()
    print("Message :", message2)
    print("Hash    :", md5_hash(message2))
    print()
    # File Integrity Check
    original = "Confidential Report Version 1"
    tampered = "Confidential Report Version 2"
    original_hash = md5_hash(original)
    tampered_hash = md5_hash(tampered)
    print("File Integrity Check")
    print()
    print("Original Hash :", original_hash)
    print("Tampered Hash :", tampered_hash)
    if original_hash == tampered_hash:
        print("Files are the same.")
    else:
        print("Files have been modified.")
# Run Program
if __name__ == "__main__":
    main()