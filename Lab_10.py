import hashlib
import os
import random
# Password Hashing Function
def hash_password(password, salt=None):
    if salt is None:
        salt = os.urandom(16)
    password_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode(),
        salt,
        100000
    )
    return salt, password_hash
# Password Verification Function
def verify_password(password, salt, stored_hash):
    new_salt, new_hash = hash_password(password, salt)
    if new_hash == stored_hash:
        return True
    else:
        return False
# OTP Generator
def generate_otp():
    otp = random.randint(100000, 999999)
    return str(otp)
# Authentication System
class AuthSystem:

    def __init__(self):
        self.users = {}

    def register(self, username, password):
        salt, password_hash = hash_password(password)
        self.users[username] = (salt, password_hash)

    def login(self, username, password, entered_otp, real_otp):
        if username not in self.users:
            return False, "User not found"
        salt, stored_hash = self.users[username]
        if not verify_password(password, salt, stored_hash):
            return False, "Incorrect password"
        if entered_otp != real_otp:
            return False, "Incorrect OTP"
        return True, "Login successful"

# ---------------- Main Function ----------------
def main():
    auth = AuthSystem()
    # Register User
    auth.register("sudip", "MyStrongPass123")
    # Generate OTP
    real_otp = generate_otp()
    print("Authentication System")
    print()
    print("Generated OTP :", real_otp)
    print()
    # Correct Login
    result = auth.login(
        "sudip",
        "MyStrongPass123",
        real_otp,
        real_otp
    )
    print("Correct Login")
    print(result)
    print()
    # Incorrect OTP
    result = auth.login(
        "sudip",
        "MyStrongPass123",
        "000000",
        real_otp
    )
    print("Incorrect OTP")
    print(result)
    print()
    # Incorrect Password
    result = auth.login(
        "sudip",
        "wrongpass",
        real_otp,
        real_otp
    )
    print("Incorrect Password")
    print(result)
# Run Program
if __name__ == "__main__":
    main()