def start():
    name = input("Hello! What is your name? ")
    print(f"Nice to meet you, {name}")
    
    play = input("Would you like to play a game? (yes/no) ")
    
    if play.lower() == "yes":
        forest()
    else:
        print("booo!! 😄 Game over.")

def forest():
    go = input("You walk forward. Do you continue? (yes/no) ")

    if go.lower() == "yes":
        woods()
    else:
        print("You stand still forever... game over.")

def woods():
    print("You enter a dark forest 🌲")
    
    enter = input("Do you enter deeper? (yes/no) ")

    if enter.lower() == "yes":
        wolf()
    else:
        print("You stay safe... but nothing happens.")

def wolf():
    print("A wolf appears 🐺")

    run = input("Do you run? (yes/no) ")

    if run.lower() == "yes":
        print("You escape! 🏃‍♂️")
    else:
        print("You fight the wolf... risky move!")

# start the game
start()