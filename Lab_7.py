import random
# Miller-Rabin Primality Test
def miller_rabin(number, rounds):

    if number < 2:
        return False
    if number == 2 or number == 3:
        return True
    if number % 2 == 0:
        return False
    r = 0
    d = number - 1
    while d % 2 == 0:
        r += 1
        d = d // 2

    for i in range(rounds):
        a = random.randint(2, number - 2)
        x = pow(a, d, number)
        if x == 1 or x == number - 1:
            continue
        is_prime = False
        for j in range(r - 1):
            x = pow(x, 2, number)
            if x == number - 1:
                is_prime = True
                break
        if not is_prime:
            return False
    return True
# ---------------- Main Function ----------------
def main():
    test_numbers = [7, 15, 97, 221, 561, 7919, 104729]
    print("Miller-Rabin Primality Test")
    print()
    for number in test_numbers:
        if miller_rabin(number, 5):
            print(number, "-> Prime")
        else:
            print(number, "-> Composite")
# Run Program
if __name__ == "__main__":
    main()