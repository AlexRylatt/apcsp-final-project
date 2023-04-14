import Player_Start as ps
import random
import fancy_print as fp
#"Enemy name":[HP,atk_dmg,mgk_dmg,atk_def,mgk_def,desc]
enemies={
    #"Gilgamesh the Banished":[38,22,6,22,12, "Gilgamesh the Banished, a betrayed ruler of a mighty kingdom within the valley of Tholyr. Betrayed by his council of trusted Whal-Marth Artisans, Gilgamesh had been planned on storming an orphanage."],
    "Jeremy the Dude Guy":[8,4,34,4,3, "Jeremy the Dude Guy, a fine upstanding citizen that spends his time watching Wharfball and drinking mead."],
    "Dire Iyasen":[1,1,1,1,1, "A creature of common myth, the Dire Iyasen is found within the Forest of Magnitude, and looks like a deformed koala."],
    "Flying Turtle":[12,3,14,18,20, "The Flying Turtle has been questioned by all great philosophers, though it simply flies because it chooses to. This heretic of physics lies within the Desert of Direction."],
    #"Bartholomew the Fell":[52,28,12,34,10, "A fallen paladin, Bartholomew the Fell was cast down by the archangels in response to his crippling alcoholism."],
    "Tree Octopus":[2,2,2,2,2, "The 3 hearted beast that swings from tree to tree, resides in the Forest of Magnitude."],
    "8-Legged Ant":[4,2,2,4,4, "Commonly confused with the Unholy Spyder, the 8-legged Ant lives in colonies of upward to 800 others. Beware of the mounds."],
    "Unsalted Butterfly":[42,10,32,8,22, "A large winged beast with the power to destroy the 9 realms, left unsalted by the Amish butter churner, and now weaker than imagined. Beware."],
    "Hellbender":[25,12,20,14,16, "A slimy and futile creature with capablities of bending flames towards it's enemies. Ironically, the salamander is only found within large water sources."],
    "Leaf Crawler":[2,4,4,2,2, "It's not a leaf."],
    "Grass Gobbler":[4,2,2,4,4, "This son of a gun not only eats grass, but it gobbles it. Similar to it's cousin, the cow, but it is cooler."],
    "Sussy Giraffe":[12,6,6,8,8, "Created by the famous alchemist Jonathon Mock, this sussy giraffe eats beings among the treetops."],
    "Pitbull: Angel":[6,24,3,6,6, "\"God gives his tastiest children to the hungriest of pitbulls.\" Beware of this \"friendly\" dog."],
    "Stick With Legs":[8,1,9,2,2, "It's a stick, but with legs... Use your imagination. Pick it up."],
    "Troll":[21,24,4,18,5, "This large and unwiedly beast sits dormant underneath shelter until provoked otherwise. DO NOT WAKE."],
    "Thief":[8,5,2,3,4, "A pickpocketer of towns and populated areas may steal your belongings without you realising. When confronted, may be strapped."],
    "Ginger":[15,14,4,10,2, "A freckeled and pasty skinned beast, the ginger is a creature grown from roots that later sprouts from the ground to begin its life."],
    "Desert Crab":[12,4,2,14,13, "Crab, but in the desert."],
    "Unholy Spyder":[2,4,4,2,2, "This 8 legged spyder is often confused with the 8-legged Ant, except God hates this one."]
    }

bosses={
    "Gilgamesh the Banished":[38,22,6,22,12, "Gilgamesh the Banished, a betrayed ruler of a mighty kingdom within the valley of Tholyr. Betrayed by his council of trusted Whal-Marth Artisans, Gilgamesh had been planned on storming an orphanage."], 
    "Unsalted Butterfly":[42,10,32,8,22, "A large winged beast with the power to destroy the 9 realms, left unsalted by the Amish butter churner, and now weaker than imagined. Beware."],
    "Hellbender":[25,12,20,14,16, "A slimy and futile creature with capablities of bending flames towards it's enemies. Ironically, the salamander is only found within large water sources."],
    "Bartholomew the Fell":[52,28,12,34,10, "A fallen paladin, Bartholomew the Fell was cast down by the archangels in response to his crippling alcoholism."],
    "Count Borislav IV":[30,10,20,15,20, "Count Borislav IV killed his brother in an attempt to usurp the throne. When he was caught and tried for murder and treason, Borislav fled, and learned the dark arts."]
    }

def battle():
    foe, stats = random.choice(list(enemies.items()))
    fp.f_print("You come across a "+foe+".")
    fp.f_print(stats[-1])
    hp=current_hp
    block_bonus=0
    enemy_block_bonus=0
    turn=True
    while True:
        #Player turn
        if turn:
            fp.f_print(player_name+"'s turn:")
            fp.f_print("Choose an action: Attack, Magic Attack, Block, Potion")
            action=input("")

            if action.title()=="Attack":
                roll=random.randint(1,20)+hit_bonus
                if roll>=stats[3]+enemy_block_bonus:
                    fp.f_print("Hit!")
                    fp.f_print("Deals "+str(base_atk)+" damage.")
                    stats[0]-=base_atk
                else:
                    fp.f_print("Miss!")

            elif action.title()=="Magic Attack":
                roll=random.randint(1,20)+hit_bonus
                if roll>=stats[4]+enemy_block_bonus:
                    fp.f_print("Hit!")
                    fp.f_print("Deals "+str(base_matk)+" damage.")
                    stats[0]-=base_matk
                else:
                    fp.f_print("Miss!")

            elif action.title()=="Block":
                block_bonus=5
                fp.f_print("You block, increasing defenses.")

            elif action.title()=="Potion":
                print("potion")

            turn=False
            enemy_block_bonus=0
            if stats[0]<=0:
                fp.f_print(foe+" died!")
                break
        

        #Enemy turn
        else:
            fp.f_print(foe+"'s turn:")
            enemy_action=random.choice(("a","ma","a","ma","b"))

            if enemy_action=="a":
                print(foe+" attacks.")
                roll=random.randint(1,20)
                if roll>=base_def+block_bonus:
                    fp.f_print(foe+" hits!")
                    fp.f_print("Deals "+str(stats[1])+" damage.")
                    hp-=stats[1]
                else:
                    fp.f_print(foe+" misses!")

            elif enemy_action=="ma":
                print(foe+" attacks with magic.")
                roll=random.randint(1,20)
                if roll>=base_mdef+block_bonus:
                    fp.f_print(foe+" hits!")
                    fp.f_print("Deals "+str(stats[2])+" damage.")
                    hp-=stats[2]
                else:
                    fp.f_print(foe+" misses!")

            elif enemy_action=="b":
                print(foe+" blocks.")
                enemy_block_bonus=3

            turn=True
            block_bonus=0
            if hp<=0:
                fp.f_print(player_name+" died")
                quit()

def reset_stats():
    base_atk=player_lvl+atk_bonus
    base_matk=player_lvl+matk_bonus
    base_def=10+player_lvl+atk_bonus
    base_mdef=10+player_lvl+matk_bonus
    base_hp=(player_lvl+hp_bonus)*2
    current_hp=base_hp

player_info=ps.start_game()
player_lvl=1
player_name=player_info[0]
atk_bonus=player_info[1]["Attack"]
def_bonus=player_info[1]["Defence"]
matk_bonus=player_info[1]["Magic Attack"]
mdef_bonus=player_info[1]["Magic Defence"]
hp_bonus=player_info[1]["Health"]
hit_bonus=player_info[1]["Hit Chance"]

base_atk=player_lvl+atk_bonus
base_matk=player_lvl+matk_bonus
base_def=10+player_lvl+atk_bonus
base_mdef=10+player_lvl+matk_bonus
base_hp=(player_lvl+hp_bonus)*2
current_hp=base_hp

battle()