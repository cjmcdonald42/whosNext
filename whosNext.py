"""
        package:  whosNext.py
         author:  Charles J McDonald «cmcdonald@woonsocketschools.com»
           date:  2024.12.06

    description:  This script will randomly select a name from a list of names until everyone has had a turn.

"""

import random

# PTech 10 Students
names = ["Evan", "Rey", "Maya", "Jaydriel", "Jaxon", "Ethan", "Kristina"]

# PTech 09 Students
# names = ["Lucas", "Jvion", "Damian", "Alice", "Nicolas", "Zack", "Jonathan", "Corbin"]

while names:
    name = random.choice(names)
    print(f"Our next presenters will be: {name}'s group. \n")
    names.remove(name)
    if names:
        input("Press Enter to pick the next name...")
    else:
        print("All names have been chosen.")
