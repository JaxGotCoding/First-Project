import random
def game():
    player_health = 100
    monster_health = 50
    print("A monster appears!")

def start():
    name = input("Hello! What is your name? ")
    print(f"Nice to meet you, {name}")

    play = input("Would you like to play a game? (yes/no) ")

    if play.lower() == "yes":
        game_state = {
            "health": 100
        }
        forest(game_state)
    else:
        print("booo!! 😄 Game over.")


def show_health(state):
    print(f"❤️ Health: {state['health']}")


def damage(state, amount):
    state["health"] = random.randint(10, 20)
    monster_health -= damage
    print(f"You take {amount} damage!")
    show_health(state)

    if state["health"] <= 0:
        print("💀 You died!")
        exit()

def attack_points():
    if attack_points > 50:
     print(f"you loose {show_health}")
    else:
        attack_points <= 50
        print("your lucky, you take no dmamage")


def forest(state):
    print("\n🌲 You walk forward into the forest.")

    go = input("Do you continue? (yes/no) ")

    if go.lower() == "yes":
        woods(state)
    else:
        print("You stand still forever... game over.")


def woods(state):
    print("\n🌲🌲 You enter a dark forest.")

    enter = input("Do you go deeper? (yes/no) ")

    if enter.lower() == "yes":
        wolf(state)
    else:
        print("You stay safe... but nothing happens.")


def wolf(state):
    print("\n🐺 A wolf appears!")

    run = input("Do you run? (yes/no) ")

    if run.lower() == "yes":
        print("🏃‍♂️ You escape safely!")
    else:
        print("You fight the wolf!")

        damage(state, 30)

        if state["health"] > 0:
            print("You survived the fight... barely.")


# start game
start()