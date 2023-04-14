import random
import trading as tr
def weapon_sell():
    print("You come across a weapons merchant. His buggy is filled entirely with swords, spears, axes, and arrows.")
    tr.trading(weapons_bank)

def potion_sell():
    print("You come across an alchemist. Her cart is filled with crates of potions and poisons.")
    tr.trading(potions_bank)

def general_sell():
    print("You come across a merchant. He offers a variety of products, some useful, some not.")
    tr.trading(misc_bank)

def travellers():
    print("You come across a group of travelers. They are willing to trade some items.")
    tr.random_trading()

def adventurer():
    print("You come across an adventurer. He is looking to buy or sell treasures.")
    tr.random_trading(misc_bank)

def hunting_party():
    print("You come across a hunting party. They are offering rewards for killing certain monsters.")

def thief():
    print("You come across a common thief. \"Your money or your life\" He says.")

def dungeon():
    print("You come across a dungeon. Monsters lay inside, but so do riches.")

def soldiers():
    print("You come across a group of soldiers. They are offering bounties.")
"""
l=(weapon_sell,potion_sell,general_sell)
random.choice(l)()
"""