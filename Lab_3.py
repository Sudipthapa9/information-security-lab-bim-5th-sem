# Diffie-Hellman Key Exchange
def diffie_hellman(p, g, alice_private, bob_private):
    # Calculate public keys
    alice_public = pow(g, alice_private, p)
    bob_public = pow(g, bob_private, p)
    # Calculate shared secret keys
    alice_shared = pow(bob_public, alice_private, p)
    bob_shared = pow(alice_public, bob_private, p)
    return alice_public, bob_public, alice_shared, bob_shared
# ---------------- Main Function ----------------
def main():
    # Public values
    p = 23
    g = 5

    # Private keys
    alice_private = 6
    bob_private = 15

    # Function call
    alice_public, bob_public, alice_shared, bob_shared = diffie_hellman(
        p, g, alice_private, bob_private
    )

    print("Diffie-Hellman Key Exchange")
    print()

    print("Public Prime (p)      :", p)
    print("Public Generator (g)  :", g)
    print()

    print("Alice Private Key :", alice_private)
    print("Bob Private Key   :", bob_private)
    print()

    print("Alice Public Key  :", alice_public)
    print("Bob Public Key    :", bob_public)
    print()

    print("Alice Shared Key  :", alice_shared)
    print("Bob Shared Key    :", bob_shared)
    print()

    if alice_shared == bob_shared:
        print("Shared keys match.")
    else:
        print("Shared keys do not match.")
# Run Program
if __name__ == "__main__":
    main()