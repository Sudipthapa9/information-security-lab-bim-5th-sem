import random
# Trial Division Method
def trial_division(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
# Fermat Primality Test
def fermat_test(number, rounds):
    if number < 4:
        return number == 2 or number == 3
    for i in range(rounds):
        a = random.randint(2, number - 2)
        if pow(a, number - 1, number) != 1:
            return False
    return True
# ---------------- Main Function ----------------
def main():
    candidates = [17, 91, 97, 561, 101]
    print("Prime Number Testing")
    print()
    for number in candidates:
        trial = trial_division(number)
        fermat = fermat_test(number, 5)
        print(number)
        print("Trial Division :", trial)
        print("Fermat Test    :", fermat)
        print()
    # Carmichael Number Example
    print("Carmichael Number Demonstration")
    print("2^560 mod 561 =", pow(2, 560, 561))
# Run Program
if __name__ == "__main__":
    main()