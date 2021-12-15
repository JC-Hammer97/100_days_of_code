import random

pl_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))


Rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

Paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

Scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

option = [Rock, Paper, Scissors]

cpu = random.randint(0,2)
cpu_choice = option[cpu]

chosen = option[pl_choice]

print(chosen)

print("Computer chose:\n")
print(cpu_choice)

if (chosen == option[0]):
    if (cpu_choice == option[0]):
        print("Draw")

    elif (cpu_choice == option[1]):
        print("You lose")

    elif (cpu_choice == option[2]):
        print("You win!")

elif (chosen == option[1]):
    if cpu_choice == option[0]:
        print("You win!")

    elif cpu_choice == option[1]:
        print("Draw")

    elif cpu_choice == option[2]:
        print("You lose")

elif (chosen == option[2]):
    if cpu_choice == option[0]:
        print("You lose")

    elif cpu_choice == option[1]:
        print("You win!")

    elif cpu_choice == option[2]:
        print("Draw")
