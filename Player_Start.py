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


def start_game():
    player_name=input("What is your character's name? ")
    player_stats={}
    stat_types=["Strength","Dexterity","Constitution","Intelligence","Wisdom","Charisma"]
    num_choices=stats()

    for item in stat_types:
        print_nums=""
        for nums in num_choices:
            print_nums+=str(nums)+" "
        print(print_nums)
        while True:
            selected_num=int(input("Type which number you would like to apply to "+item+": "))
            if selected_num in num_choices:
                num_choices.remove(selected_num)
                player_stats[item]=selected_num
                break
            else:
                print("That number is not available.")
    print(player_stats)