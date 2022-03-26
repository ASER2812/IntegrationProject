#   In this program I set-out to make the creation of a Dungeon and Dragons
# character easier, mainly through the simulation of the dice rolling normally
# involved. The Character Creation process involves generating values that are
# assigned to six attributes inherent to DND characters. Values are generated
# by rolling four dice and adding the largest three rolls, this process is then
# repeated, until six values are generated. Once assigned the values are
# then added to any "bonuses" the new value is referred to as an "Ability
# Scores".A secondary value is derived from each "Ability Score" called a
# "Modifier", this value is generated through the formula ("Ability Score" -
# 10)/2, and rounding down. My goaL was to simulate this process for the user.

import random
import math


# This function takes no input and returns a list of four random integers.
def dice_roller():
    rolls = []
    n = 4
    while n > 0:
        rolls.append(random.randint(1, 6))
        n -= 1
    # Before being returned, the list is sorted from highest to lowest.
    rolls.sort(reverse=True)
    return rolls


# Here a dictionary for the "Dungeons and Dragons" attributes is created
# along with a list of the attributes as keys, for use later.
DND_attributes_bonuses = {}
DND_attributes_keys = ["Strength", "Dexterity", "Constitution",
                       "Intelligence", "Wisdom", "Charisma"]

# Splash Text that welcomes user.
print("Welcome to the Character Stat Roller for 5th Edition")
pause = input("Press Enter to continue\n")
print("Input the total ability bonuses for each attribute:")

# Outer loop cycles through dictionary keys.
for key in DND_attributes_keys:
    # Loops until a good inputs is taken.
    while key not in DND_attributes_bonuses.keys():
        print(key, ":", end="")
        key_bonus = input()
        # noinspection PyBroadException
        try:
            # If good input, The key and value are added to the dictionary.
            key_bonus = int(key_bonus)
            DND_attributes_bonuses.update({key: key_bonus})

        except:
            pass

# Prompts for next phase of program
print("\nRolling will now begin")
print(DND_attributes_bonuses)
pause = input("press Enter to continue\n")

# This list is used to store, the groups of rolls.
initial_rolls = []
# The loop simulates roll 6 groups of four dice.
for x in range(6):
    roll = dice_roller()
    # Each set of rolls is printed for user
    print(x + 1, ":", roll)
    # The sum of the greatest 3 dice of a group gets stored.
    initial_rolls.append(sum(roll[0:3]))

# Prompts for the assignment phase of the program.
print("The sum of the greatest 3 rolls for each Attempt:", initial_rolls)
pause = input("Press Enter to continue\n")

# Prints the list of attributes so that the user can assign them.
print("Assign roll to an attribute:", initial_rolls)

# This list stores attribute selections as the user assigns them.
assigned_rolls = []

# Loops through every dictionary entry, in the form of a tuple.
for key, value in DND_attributes_bonuses.items():
    # This Loop checks for a valid input, a valid input in this case is a value
    # from the rolls list.
    valid_value = False
    while not valid_value:
        print(key, ":", end="")
        chosen_score = input()
        # noinspection PyBroadException
        try:
            chosen_score = int(chosen_score)

            # If the value is a valid form it gets tested against the list.
            if chosen_score in initial_rolls:

                # If that test is also passed, the value is added.
                assigned_rolls.append(chosen_score)

                # The value is removed from the original list so that a value
                # cannot be assigned more than twice.
                initial_rolls.remove(chosen_score)
                valid_value = True
            else:
                pass
        except:
            pass

# This section creates an ordered list of attribute bonuses.
attributes_bonus = []
for key, value in DND_attributes_bonuses.items():
    attributes_bonus.append(int(value))
    DND_attributes_keys.append(key)

# Prompts the user for the results phase of the program.
print("\nThank you, The Ability Scores and Modifiers will now be displayed:")
pause = input("Press Enter to continue\n")

# Prints all the attribute values
print("The Ability Score for each attribute:")
for (item1, item2, item3) in zip(DND_attributes_keys, attributes_bonus,
                                 assigned_rolls):
    print(item1, ":", item2 + item3)

# While printing, this calculates individual attribute_bonuses
print("\nThe Modifier for each attribute:")
for (item1, item2, item3) in zip(DND_attributes_keys,
                                 attributes_bonus,
                                 assigned_rolls):
    # Dungeons and Dragons calculates ability score bonuses through a not so
    # simple algorithm, which is simulated through the equation below.
    print(item1, " modifier: ", math.floor(((item2 + item3) - 10) / 2), sep="")