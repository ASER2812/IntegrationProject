import random
import math


def Dice_Roller():  # function that will always roll 4 d6(6-sided dice),
    # sort the rolls from highest to lowest, and spit out a list of 4 numbers
    rolls = []
    n = 4
    while n > 0:
        rolls.append(random.randint(1, 6))
        n -= 1
    rolls.sort(reverse=True)
    return rolls


attributes = {}
attributes_keys = ["Strength", "Dexterity", "Constitution",
                   "Intelligence", "Wisdom", "Charisma"]
print("Welcome to the Character Stat Roller for 5th Edition")
input("Press Enter to continue\n")
print("Input the total ability bonuses for each attribute:")
for key in attributes_keys:
    while key not in attributes.keys():
        print(key, ":", end="")
        key_bonus = input()
        # noinspection PyBroadException
        try:
            key_bonus = int(key_bonus)
            attributes.update({key: key_bonus})

        except:
            pass
print("Rolling will now begin")
print(attributes)
input("press Enter to continue\n")
initial_rolls = []
for x in range(6):
    roll = Dice_Roller()
    print(x + 1, ":", roll)
    initial_rolls.append(sum(roll[0:3]))
print("The sum of the greatest 3 rolls for each Attempt:", initial_rolls)
input("Press Enter to continue\n")
print("Assign roll to attribute:", initial_rolls)
sorted_rolls = []
for key, value in attributes.items():
    valid_value = False
    while not valid_value:
        print(key, ":", end="")
        chosen_score = input()
        # noinspection PyBroadException
        try:
            chosen_score = int(chosen_score)
            if chosen_score in initial_rolls:
                sorted_rolls.append(chosen_score)
                initial_rolls.remove(chosen_score)
                valid_value = True
            else:
                pass
        except:
            pass
attributes_bonus = []
for key, value in attributes.items():
    attributes_bonus.append(int(value))
    attributes_keys.append(key)
print()
print("Thank you, The Ability Scores and Modifiers will now be displayed:")
input("Press Enter to continue\n")
print("The Ability Score for each attribute:")
for (item1, item2, item3) in zip(attributes_keys, attributes_bonus,
                                 sorted_rolls):
    print(item1, ":", item2 + item3)
print("\nThe Modifier for each attribute:")
for (item1, item2, item3) in zip(attributes_keys, attributes_bonus,
                                 sorted_rolls):
    print(item1, " modifier: ", math.floor(((item2 + item3) - 10) / 2), sep="")
