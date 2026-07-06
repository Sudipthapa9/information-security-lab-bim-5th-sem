
def gcd_euclid(a, b):
    steps = []
    while b != 0:
        steps.append((a, b, a % b))
        a, b = b, a % b
    return a, steps
 
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    return g, y1, x1 - (a // b) * y1
 
def euler_totient(n):
    result, temp, p = n, n, 2
    while p * p <= temp:
        if temp % p == 0:
            while temp % p == 0:
                temp //= p
            result -= result // p
        p += 1
    if temp > 1:
        result -= result // temp
    return result
 
# Driver code
a, b = 270, 192
g, steps = gcd_euclid(a, b)
for x, y, r in steps:
    print(f"{x} = {x//y}*{y} + {r}")
print("GCD =", g)
 
g2, x, y = extended_gcd(a, b)
print(f"Extended Euclidean: x={x}, y={y} => {a}*{x} + {b}*{y} = {a*x + b*y}")
 
for n in [9, 10, 36]:
    print(f"phi({n}) =", euler_totient(n))
