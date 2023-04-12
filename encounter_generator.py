import random
def roll_encounter():
    encounter_roll=random.randint(1,100)
    if encounter_roll<=50:
        battle_encounter()
    elif encounter_roll<=75:
        friendly_encounter()
    else:
        print("No encounter")

def battle_encounter():
    print("1")

def friendly_encounter():
    print("2")