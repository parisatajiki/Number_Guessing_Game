import random

print("Welcome to the Number Guessing Game!\n Rules of the Game:")
print("- I’m thinking of a number between 1 and 100.\n- Your goal is to guess the number correctly.\n- You can choose a difficulty level")



def menu():
    print("Please select the difficulty level:")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)")

    choice = input("Select the difficulty level : ")
    if choice == "1" :
        global chance
        chance = 10
    elif choice == "2" :
        chance = 5
    elif choice == "3" :
        chance = 3
    else:
        print("Enter number between 1-3 ")


number = random.randint(1,100)
end = False
b = True
while True:
    while b :
        menu()
        for try0 in range(chance):
            my_num = int(input("Enter your number(1,100) : "))
            print(f"This was attempt number = {try0} ")
            if my_num < number:
                print("Choose a bigger number.")
            elif my_num > number:
                print("Choose a smaller number.")
            elif my_num == number:
                print("You guessed it right! You won!")

            if try0 == (chance-1):
                b = False
                print(f"You couldn’t guess it. The number was {number} .\n Do you want play again?\n 1.Yes\n 2.No (Exite) ")
                n = input("Enter num : ")
                if n == "1":
                    b = True
                elif n == "2":
                    end = True
                    break
                else:
                    print("Enter 1 or 2")
    if end == True:
        break
            