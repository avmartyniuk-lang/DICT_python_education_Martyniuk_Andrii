print("Hello! My name is Kirill")
print("I was created in 2026")

print("Please, remind me your name.")
name = input("> ")
print(f"What a great name you have, {name}!")

print("Let me guess your age.\nEnter remainders of dividing your age by 3, 5 and 7.")
remainder3 = input("> ")
remainder3 = int(remainder3)
remainder5 = input("> ")
remainder5 = int(remainder5)
remainder7 = input("> ")
remainder7 = int(remainder7)
age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
print(f"Your age is {age}; that's a good time to start programming")

print("Now I will prove to you that I can count to any number you want.")
number = input("> ")
number = int(number)
for x in range(number + 1):
    print(f"{x} !")
print("Completed, have a nice day!")

print("Let's test your programming knowledge.")
print("In most programming languages, what is the index of the first element in an array?")
print("1. -1")
print("2. It depends on the array size")
print("3. 0")
print("4. 1")
while True:
    answer = input("> ")
    answer = int(answer)
    if answer == 3:
        break
    print("Please, try again")
print("Congratulations, have a nice day!")
