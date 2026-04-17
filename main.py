name = input("Hello! What is your name? ")
print(f"Nice to meet you, {name}")

play = input("Would you like to play a game? (yes/no) ")

if play.lower() == "yes":
    print("Ok! Let's start... 🎮")

    go = input("Do you go ahead? (yes/no) ")
    if go.lower() == "yes":
        print("You walk forward into the forest...")

        woods = input("You see dark woods. Enter? (yes/no) ")
        if woods.lower() == "yes":
            print("A wolf appears 🐺")

            run = input("Do you run? (yes/no) ")
            if run.lower() == "yes":
                print("You escape!")
            else:
                print("You fight the wolf... risky move!")

        else:
            print("You stay safe... but nothing happens.")
    else:
        print("You stand still forever... game over.")

else:
    print("booo!! 😄")