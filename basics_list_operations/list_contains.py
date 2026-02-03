# checking if an item is in a list

fruits = ["apple", "orange", "banana"]
print("banana" in fruits) # prints True
print("banana" not in fruits) # prints False


# function example
def is_top_weapon(weapon, weapons):
    return weapon in weapons

if __name__ == "__main__":
    top_weapons = [
        "sword of justice",
        "sword of slashing",
        "stabby daggy",
        "great axe",
        "silver bow",
        "spellbook",
        "spiked knuckles",
    ]
    weapon = "spellbook"
    print(is_top_weapon(weapon, top_weapons)) # prints True