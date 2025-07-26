#global and local scope basics
enemies = 1
def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")
increase_enemies()
print(f"enemies outside function: {enemies}")
# Local Scope
def drink_potion():
    potion_strength = 2
    print(potion_strength)
drink_potion()
# Can't access this potion_strength outside of its scope
# print(potion_strength)
# Global Scope
player_health = 10
def game():
    def drink_potion():
        potion_strength = 2
        print(player_health)
    drink_potion()
print(player_health)

#block scope
game_level = 10
enemies = ["Skeleton", "Zombie", "Alien"]
def create_enemy():
    new_enemy = ""
    if game_level < 5:
        new_enemy = enemies[0]
    print(new_enemy)

#global variables
# Modifying Global Scope
enemies = 1
# def increase_enemies():
#     global enemies
#     enemies += 1
#     print(f"enemies inside function: {enemies}")
def increase_enemies(enemy):
    print(f"enemies inside function: {enemy}")
    return enemy + 1
enemies = increase_enemies(enemies)
print(f"enemies outside function: {enemies}")
