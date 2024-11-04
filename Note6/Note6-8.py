n = int(input("Enter a number: "))
print("Second largest factors is:")
i = n - 1
while i>0:
    if n%i == 0:
        print(i)
        break
    i-=1
