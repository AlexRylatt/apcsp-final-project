"""
To do:
Give enemies proper xp values
Balance enemies
Maybe add leveling for enemies? New retreat feature makes this less of an issue
"""

import Player_Start as ps
import random
import fancy_print as fp
#"Enemy name":[HP,atk_dmg,mgk_dmg,atk_def,mgk_def,exp,desc]
enemies={
    "Jeremy the Dude Guy":[8,4,34,4,3,100, "Jeremy the Dude Guy, a fine upstanding citizen that spends his time watching Wharfball and drinking mead."],
    "Dire Iyasen":[1,1,1,1,1,100, "A creature of common myth, the Dire Iyasen is found within the Forest of Magnitude, and looks like a deformed koala."],
    "Flying Turtle":[12,3,14,18,20,100, "The Flying Turtle has been questioned by all great philosophers, though it simply flies because it chooses to. This heretic of physics lies within the Desert of Direction."],
    "Tree Octopus":[2,2,2,2,2,100, "The 3 hearted beast that swings from tree to tree, resides in the Forest of Magnitude."],
    "8-Legged Ant":[4,2,2,4,4,100, "Commonly confused with the Unholy Spyder, the 8-legged Ant lives in colonies of upward to 800 others. Beware of the mounds."],
    "Unsalted Butterfly":[42,10,32,8,22,100, "A large winged beast with the power to destroy the 9 realms, left unsalted by the Amish butter churner, and now weaker than imagined. Beware."],
    "Hellbender":[25,12,20,14,16,100, "A slimy and futile creature with capablities of bending flames towards it's enemies. Ironically, the salamander is only found within large water sources."],
    "Leaf Crawler":[2,4,4,2,2,100, "It's not a leaf."],
    "Grass Gobbler":[4,2,2,4,4,100, "This son of a gun not only eats grass, but it gobbles it. Similar to it's cousin, the cow, but it is cooler."],
    "Sussy Giraffe":[12,6,6,8,8,100, "Created by the famous alchemist Jonathon Mock, this sussy giraffe eats beings among the treetops."],
    "Pitbull: Angel":[6,24,3,6,6,100, "\"God gives his tastiest children to the hungriest of pitbulls.\" Beware of this \"friendly\" dog."],
    "Stick With Legs":[8,1,9,2,2,100, "It's a stick, but with legs... Use your imagination. Pick it up."],
    "Troll":[21,24,4,18,5,100, "This large and unwiedly beast sits dormant underneath shelter until provoked otherwise. DO NOT WAKE."],
    "Thief":[8,5,2,3,4,100, "A pickpocketer of towns and populated areas may steal your belongings without you realising. When confronted, may be strapped."],
    "Ginger":[15,14,4,10,2,100, "A freckeled and pasty skinned beast, the ginger is a creature grown from roots that later sprouts from the ground to begin its life."],
    "Desert Crab":[12,4,2,14,13,100, "Crab, but in the desert."],
    "Unholy Spyder":[2,4,4,2,2,100, "This 8 legged spyder is often confused with the 8-legged Ant, except God hates this one."]
    }

bosses={
    "Gilgamesh the Banished":[38,22,6,22,12,100, "Gilgamesh the Banished, a betrayed ruler of a mighty kingdom within the valley of Tholyr. Betrayed by his council of trusted Whal-Marth Artisans, Gilgamesh had been planned on storming an orphanage."], 
    "Unsalted Butterfly":[42,10,32,8,22,100, "A large winged beast with the power to destroy the 9 realms, left unsalted by the Amish butter churner, and now weaker than imagined. Beware."],
    "Hellbender":[25,12,20,14,16,100, "A slimy and futile creature with capablities of bending flames towards it's enemies. Ironically, the salamander is only found within large water sources."],
    "Bartholomew the Fell":[52,28,12,34,10,100, "A fallen paladin, Bartholomew the Fell was cast down by the archangels in response to his crippling alcoholism."],
    "Count Borislav IV":[30,10,20,15,20,100, "Count Borislav IV killed his brother in an attempt to usurp the throne. When he was caught and tried for murder and treason, Borislav fled, and learned the dark arts."]
    }


#Inventory
armor_bank={"Leather Armor":[1,1],"Studded Leather Armor":[3,3],"Chainmail Armor":[6,5],"Iron Armor":[7,7],"Steel Armor":[9,7],"Wizard Cloak":[2,13],"Mithril":[10,14]}
#weapons_bank=[["Stick",1,0],["Wooden Sword",2,0],["Plastic Lightsaber",1,12],["Morning Star",4,0],["Blessed Chancla",5,5],["Crossbow",8,0],["Inferno Staff",1,15],["Mithril Longsword",20,22],["Iron Shortsword",7,0],["Holy Warhammer",17,5]]
weapons_bank={"Big Stick":[0,0],"Iron Sword":[3,0],"Plastic Lightsaber":[1,6],"Morning Star":[4,0],"Crossbow":[6,0],"Inferno Staff":[1,7],"Mithrill Broadsword":[12,14],"Holy Hand Grenade of Antioch":[0,20]}
potions_bank={"Health Potion I":4,"Health Potion II":8,"Health Potion III":16}
player_armors=[]
player_weapons=[]
player_potions=[["Health Potion I",4]]
#This is what the player will start with
equip_armor=["Leather Armor",armor_bank["Leather Armor"]]
equip_weapon=["Big Stick",weapons_bank["Big Stick"]]

#This is just debug equipment
#equip_weapon=["Kill",[100,100]]
#equip_armor=["No",[100,100]]

def battle(foe_list):
    foe, stats = random.choice(list(foe_list.items()))
    encounter_enemy=[foe,stats.copy()]
    foe=encounter_enemy[0]
    stats=encounter_enemy[1]
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
            fp.f_print("You have "+str(hp)+" hit points remaining.")
            fp.f_print("Choose an action: Attack, Magic Attack, Block, Potion, Retreat")

            while True:
                action=input("")
                if action.title()=="Attack":
                    roll=random.randint(1,20)+hit_bonus
                    if roll>=stats[3]+enemy_block_bonus:
                        fp.f_print("Hit!")
                        fp.f_print("Deals "+str(base_atk+equip_weapon[1][0])+" damage.")
                        stats[0]-=base_atk+equip_weapon[1][0]
                    else:
                        fp.f_print("Miss!")
                    break

                elif action.title()=="Magic Attack":
                    roll=random.randint(1,20)+hit_bonus
                    if roll>=stats[4]+enemy_block_bonus:
                        fp.f_print("Hit!")
                        fp.f_print("Deals "+str(base_matk+equip_weapon[1][1])+" damage.")
                        stats[0]-=base_matk+equip_weapon[1][1]
                    else:
                        fp.f_print("Miss!")
                    break

                elif action.title()=="Block":
                    block_bonus=5
                    fp.f_print("You block, increasing defenses.")
                    break

                elif action.title()=="Potion":
                    use_potion()
                    break
                
                elif action.title()=="Retreat":
                    roll=random.randint(1,3)
                    if roll==1:
                        fp.f_print(player_name+" retreated from the battle.")
                        return hp,player_exp
                    else:
                        fp.f_print(player_name+" was unable to escape.")
                    break
                
                else:
                    fp.f_print("Invalid input")
                
            turn=False
            enemy_block_bonus=0
            if stats[0]<=0:
                fp.f_print(foe+" died!")
                fp.f_print("You gained "+str(stats[-2])+" experience.")
                return hp, stats[-2]+player_exp
        

        #Enemy turn
        else:
            fp.f_print(foe+"'s turn:")
            enemy_action=random.choice(("a","ma","a","ma","b"))

            if enemy_action=="a":
                print(foe+" attacks.")
                roll=random.randint(1,20)
                if roll>=base_def+block_bonus+equip_armor[1][0]:
                    fp.f_print(foe+" hits!")
                    fp.f_print("Deals "+str(stats[1])+" damage.")
                    hp-=stats[1]
                else:
                    fp.f_print(foe+" misses!")

            elif enemy_action=="ma":
                print(foe+" attacks with magic.")
                roll=random.randint(1,20)
                if roll>=base_mdef+block_bonus+equip_armor[1][1]:
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


def open_inventory():
    global equip_armor, equip_weapon
    fp.f_print("Current armor equipped: "+equip_armor[0])
    fp.f_print("Current weapon equipped: "+equip_weapon[0])
    fp.f_print("Armor owned:")
    for item in player_armors:
        print(item[0])
    fp.f_print("Weapons owned:")
    for item in player_weapons:
        print(item[0])
    fp.f_print("Potions owned:")
    for item in player_potions:
        print(item[0])
    fp.f_print("Select an action: Back, Unequip Armor, Unequip Weapon, Equip Armor, Equip Weapon")
    action=input("").title()

    if action=="Unequip Armor":
        if equip_armor[0]=="None":
            fp.f_print("Not wearing armor.")
        else:
            player_armors.append([equip_armor[0],equip_armor[1]])
            equip_armor=["None",0,0]
            fp.f_print("Armor unequiped.")

    elif action=="Unequip Weapon":
        if equip_weapon[0]=="None":
            fp.f_print("Not wielding a weapon.")
        else:
            player_weapons.append([equip_weapon[0],equip_weapon[1]])
            equip_weapon=["None",0,0]
            fp.f_print("Weapon unequiped.")

    elif action=="Equip Armor":
        if equip_armor[0]=="None":
            fp.f_print("Enter which armor you would like to equip")
            equiping=input("").title()
            armor_names = [names[0] for names in player_armors]
            if equiping in armor_names:
                equip_armor[0]=equiping
                equip_armor[1]=armor_bank[equiping]
                for item in player_armors:
                    if item[0]==equiping:
                        player_armors.remove(item)
                        break
                fp.f_print("Equiped "+equiping)
            else:
                fp.f_print("Armor not in inventory")
        else:
            fp.f_print("Already wearing armor")

    elif action=="Equip Weapon":
        if equip_weapon[0]=="None":
            fp.f_print("Enter which weapon you would like to equip")
            equiping=input("").title()
            weapon_names = [names[0] for names in player_weapons]
            if equiping in weapon_names:
                equip_armor[0]=equiping
                equip_weapon[1]=weapons_bank[equiping]
                for item in player_weapons:
                    if item[0]==equiping:
                        player_weapons.remove(item)
                        break
                fp.f_print("Equiped "+equiping)
            else:
                fp.f_print("Weapon not in inventory")
        else:
            fp.f_print("Already wielding weapon")


def use_potion():
    global current_hp
    fp.f_print("Select a potion to use")
    selection=input("").title()
    p_potions_names=[names[0] for names in player_potions]
    if selection in p_potions_names:
        current_hp+=potions_bank[selection]
        if current_hp>base_hp:
            current_hp=current_hp
        for item in player_potions:
                    if item[0]==selection:
                        player_potions.remove(item)
                        break
        fp.f_print("Used "+selection)
    else:
        fp.f_print("Invalid input")

def roll_loot():
    loot_roll=random.choice(("p","p","p","w","a"))
    if loot_roll=="p":
        random_potion=random.choice(list(potions_bank.keys()))
        player_potions.append([random_potion,potions_bank[random_potion]])
        fp.f_print("You got "+random_potion)
    elif loot_roll=="w":
        random_weapon=random.choice(list(weapons_bank.keys()))
        player_weapons.append([random_weapon,weapons_bank[random_weapon]])
        fp.f_print("You got "+random_weapon)
    elif loot_roll=="a":
        random_armor=random.choice(list(armor_bank.keys()))
        player_armors.append([random_armor,armor_bank[random_armor]])
        fp.f_print("You got "+random_armor)
    

def encounters():
    global chance_of_boss
    global chance_of_loot
    odds=["basic"]*25+["boss"]*chance_of_boss+["loot"]*chance_of_loot+["healing"]*5
    encounter_selected=random.choice(odds)
    hp=current_hp
    exp=player_exp
    if encounter_selected=="basic":
        hp,exp=battle(enemies)
    elif encounter_selected=="boss":
        hp,exp=battle(bosses)
        chance_of_boss=-1
    elif encounter_selected=="loot":
        roll_loot()
        chance_of_loot=-1
    elif encounter_selected=="healing":
        fp.f_print("You come across a room you can heal in. Health restored to full.")
        return base_hp,exp
    return hp,exp

player_info=ps.start_game()
player_lvl=1
player_exp=0
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

chance_of_loot=0
chance_of_boss=0

while True:
    fp.f_print("Enter an action: Go, Inventory, Potion")
    action=input("")
    if action.title()=="Go":
        current_hp,player_exp=encounters()
        chance_of_loot+=2
        chance_of_boss+=1
    elif action.title()=="Inventory":
        open_inventory()
    elif action.title()=="Potion":
        use_potion()
    else:
        print("Invalid input")
    
    #Level up
    if player_exp==player_lvl*100:
        player_exp=0
        player_lvl+=1
        #Redo stats
        base_atk=player_lvl+atk_bonus
        base_matk=player_lvl+matk_bonus
        base_def=10+player_lvl+atk_bonus
        base_mdef=10+player_lvl+matk_bonus
        base_hp=(player_lvl+hp_bonus)*2
        current_hp=base_hp
        fp.f_print(player_name+" leveled up to level "+str(player_lvl))
