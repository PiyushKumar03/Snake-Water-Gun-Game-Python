#Snake Water Gun Game -

import random

print("SNAKE WATER GUN GAME")
""" Game Description - if User choose snake and cpu choose water, so user is winner and vice-versa.
If User choose water and cpu choose Gun, so user is winner and vice-versa.
 If User choose gun and cpu choose snake, so user is winner and vice-versa.
 If, By chance both choose same(snake, water or gun), so their no points.
 Those win more match, will win the game."""

print("What is your choice-")
count = 10
total_move = 1
cpu_won = 0
user_won = 0
while count >= total_move:
    user_choice = input("Choose 's' for snake, 'w' for water & 'g' for gun-\t")
    list_choice = ["s", "w", "g"]
    cpu_choice = random.choice(list_choice)
    if user_choice == cpu_choice:
        pass
    elif user_choice == "s" and cpu_choice == "w":
        user_won += 1

    elif user_choice == "s" and cpu_choice == "g":
        cpu_won += 1

    elif user_choice == "w" and cpu_choice == "s":
        cpu_won += 1

    elif user_choice == "w" and cpu_choice == "g":
        user_won += 1

    elif user_choice == "g" and cpu_choice == "s":
        user_won += 1

    elif user_choice == "g" and cpu_choice == "w":
        cpu_won += 1

    else:
        print("Dont choose wrong word, Game over")
        break
    count -= 1
    print(f"Remaining life: {count}")

print(f"CPU Won {cpu_won} times and User Won {user_won} times.")
if cpu_won < user_won:
    print("User is winner.")
elif cpu_won > user_won:
    print("Cpu is Winner.")
else:
    print("Both have same points. So, their is no Winner...")

