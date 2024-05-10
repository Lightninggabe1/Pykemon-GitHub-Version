from pokemontype import Pokemon, Electric, Fire, Fighting, enemypoké
from regionpokemon import kanto, kalos
from colours import lightgrey, darkgrey, red, green, yellow, blue, purple, cyan, white, default, bold, underline, blink, reverse, black, strikethrough, platinum, ironc, gold, silver, copper, paleyellow, lime, turquoise, teal
import sys,time
import subprocess,os
import random

def sprint(str):
   for c in str + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(3./90)
def clear():
  _=os.system('clear')
def oneprint(s):
  for c in s:
      sys.stdout.write(c)
      sys.stdout.flush()
      time.sleep(0.05)


sprint("Welcome to Py.kémon!")
name = input("What is your name?\n")
sprint(f"Hello {name}!")
sprint("Choose a region.")
print("1. Kanto")
#print(f"{strikethrough}2. Kalos (Gen 6)[Pokémon X & Y){default}{darkgrey}(Coming soon)")
#print(f"{strikethrough}3. Alola (Gen 7{default}{darkgrey}(Coming soon)")
#print(f"{strikethrough}4. Galar (Gen 8){default}{darkgrey}(Coming soon)") 
#print(f"{strikethrough}5. Paldea (Gen 9){default}{darkgrey}(Coming soon){default}")
region = input(f"Choose a region (1,{strikethrough}2,3,4,5{default}[Coming soon]'): ")
if region == "1":
  sprint(f"Welcome to Kanto, {name}! My name is Professor Acacia.")
  sprint(f"Choose your Starter from these Pokémon: #001: {green}Bulbasaur{default}, #004: {red}Charmander{default}, #007: {blue}Squirtle{default}")
  reply = input(f"{darkgrey}[Reply]': 1. I choose Bulbasaur! 2. I choose Charmander! 3. I choose Squirtle! 4. Is there any other Pokémon?{default}")
  if reply == "1":
    sprint("[Professor Acacia]' You chose Bulbasaur!")
    sprint("Bulbasaur is a Grass and Poison type Pokémon.")
    sprint("There is a plant seed on its back right from the day this Pokémon is born. The seed slowly grows larger. While it is young, it uses the nutrients that are stored in the seed on its back in order to grow.")
    currentpokemon = Pokemon("Bulbasaur", 0,"Grass & Poison",90)
  elif reply  == "2":
    sprint("[Professor Acacia]' You chose Charmander!")
    sprint("Charmander is a Fire type Pokémon.")
    sprint("It has a preference for hot things. When it rains, steam is said to spout from the tip of its tail.")
    sprint("From the time it is born, a flame burns at the tip of its tail. Its life would end if the flame were to go out.")
    currentpokemon = Pokemon("Charmander",0,"Fire",90)
  elif reply == "3":
    sprint("[Professor Acacia]' You chose Squirtle!")
    sprint("Squirtle is a water type Pokémon." )
    sprint("When it feels threatened, it retracts its long neck into its shell and squirts out water with vigorous force.")
    currentpokemon = Pokemon("Squirtle",0,"Water",85)
  elif reply == "4":
    sprint("[Professor Acacia]' Ah...Well, we do have some other Pokémon that you might like...")
    sprint("Yes, yes, we do have a Pikachu and an Eevee...Which one would you like?")
    choose_2 = input(f"{darkgrey}[Reply]': 1. I choose Pikachu! 2. I choose Eevee!{default}")
    if choose_2 == "1":
      sprint("[Professor Acacia]'You chose Pikachu!'")
      sprint("'When it is angered, it immediately discharges the energy stored in the pouches in its cheeks. When several of these Pokémon gather, their electricity can build and cause lightning storms.'")
      currentpokemon = Pokemon("Pikachu",0,"Electric",85)
    elif choose_2 == "2":
      sprint("[Professor Acacia]'You chose Eevee!")
      sprint("Its genetic code is irregular. It may mutate if it is exposed to radiation from element stones. Its ability to evolve into many forms allows it to adapt smoothly and perfectly to any environment.'")
      currentpokemon = Pokemon("Eevee", 0, "Normal", 85)
  sprint("[Professor Acacia]'You may now begin your journey!")
  #sprint("[Professor Acacia]'Oh, I forgot. You can choose a Pokédex form.'")
  #sprint("[Professor Acacia]'The Kanto Pokedex, Galar Pokedex, Kalos Pokédex, and the Alolan Pokédex are your Pokédex options. Which one will you choose?'")
  #pokedex = input(f"{darkgrey}1. I choose the Kanto Pokedex! 2. I choose the Galar Pokedex! 3. I choose the Kalos Pokedex! 4. I choose the Alolan Pokedex! {default}")
  
elif region == "4":
  sprint("You have chosen Alola!")
  sprint("Choose an island.")
  print("1. Melemele Island")
  print("2. Akala Island")
  print("3. Ula'ula Island")
  print("4. Poni Island")
  print("5. Aether Paradise")
  alolanisland = input("Choose a island (1,2,3,4,5): ")

pokemontype = input("Type your choice here: ")

