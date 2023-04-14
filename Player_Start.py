import random
import fancy_print as fp
def stats():
    final=[]
    for i in range(6):
        results=[]
        for i in range(4):
            num=random.randint(1,6)
            results.append((num-10)%2)
        results.remove(min(results))
        final.append(sum(results))
    return final


def start_game():
    fp.f_print("What is your character's name? ")
    player_name=input("")
    player_stats={}
    stat_types=["Attack","Defence","Health","Magic Attack","Magic Defence","Hit Chance"]
    num_choices=stats()

    for item in stat_types:
        print_nums=""
        for nums in num_choices:
            print_nums+=str(nums)+" "
        fp.f_print(print_nums)
        while True:
            fp.f_print("Type which number you would like to use as a bonus to "+item+": ")
            selected_num=int(input(""))
            if selected_num in num_choices:
                num_choices.remove(selected_num)
                player_stats[item]=selected_num
                break
            else:
                fp.f_print("That number is not available.")
    return[player_name, player_stats]