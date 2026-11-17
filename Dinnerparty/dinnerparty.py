import random

print("Enter the number of friends joining (including you):")
count = int(input("> "))

if count <= 0:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    friends = {}
    for i in range(count):
        name = input("> ")
        friends[name] = 0

    print("Enter the total amount:")
    total = float(input("> "))

    share = round(total / count, 2)
    for name in friends:
        friends[name] = share

    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    answer = input("> ")

    if answer == "Yes":
        lucky = random.choice(list(friends))
        print(f"{lucky} is the lucky one!")
        new_share = round(total / (count - 1), 2)
        for name in friends:
            friends[name] = new_share
        friends[lucky] = 0
        print(friends)
    else:
        print("No one is going to be lucky")
        print(friends)
