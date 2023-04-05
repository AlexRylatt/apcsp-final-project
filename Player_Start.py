import random
def stats():
    final=[]
    for i in range(6):
        results=[]
        for i in range(4):
            num=random.randint(1,6)
            results.append(num)
        results.remove(min(results))
        final.append(sum(results))
    return final



player_name=input("What is your character's name?")
player_stats={}
stat_types=["Strength","Dexterity","Constitution","Intelligence","Wisdom","Charisma"]
num_choices=stats()

for item in stat_types:
    print(item)