import random

player_health = 100
monster_health = 100

while player_health > 0 and monster_health > 0:
    player_damage = random.randint(5, 15)
    monster_health -= player_damage
    print("Monster health:", monster_health)

    monster_damage = random.randint(1, 10)
    player_health -= monster_damage
    print("Player health:", player_health)

print("Fight ended")