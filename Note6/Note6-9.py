n = int(input("Enter a number: "))
is_prime = True
if n ==1:
    print("Primate number.")
if n == 2 or n == 3:
    print("Prime number.")
for i in range(2, int(n)):
    if n%i == 0:
        print("Not a prime number.")
        is_prime = False
if is_prime:
    print("Prime number.")