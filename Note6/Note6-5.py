num = int(input("Give me a even number: "))
while num & 1:
    num = int(input("Enter again: "))
print("Thank you.", num, "is an even number.")