age = float(input("How old are you? \n"))
if age >= 12 and age<60: price = 498
elif age >= 3 and age<=11: price = 249
elif (age<=2 and age>=0) or age>=65: price = 0
elif age <=64 and age>=60: price = 100
print("Your ticket price: $", str(price))