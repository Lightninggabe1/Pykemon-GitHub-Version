import random
import keyboard


from typepokemonlist import waterpoke,normalpoke
class Pokemon:
  def __init__(self, name, level, type,health):
        self.name = name
        self.level = level
        self.type = type
        self.health = health
  

  def display_info(self):
        print(f"Name: {self.name}")
        print(f"Level: {self.level}")
        print(f"Type: {self.type}")
        print(f"Health: {self.health}")
class enemypoké:
  def __init__(self, name, level, type,health):
      self.name = name
      self.level = level
      self.type = type
      self.health = health  

  def display_info(self):
      print(f"Name: {self.name}")
      print(f"Level: {self.level}")
      print(f"Type: {self.type}")
      print(f"Health: {self.health}")
    
class Battle:   
  def battle_mechanics(self,pokemon,enemypoké):
    while True:
      if pokemon.health > 0 and enemypoké.health > 0:
        print("1. Battle")
        print("2. Pokémon")
        print("3. Bag")
        print("4. Run")
        battoption = input("What do you want to do? ")
        if battoption == "1" and pokemon in waterpoke:
          print("1. Hydro Pump")
          print("2. Aqua Jet")
          print("3. Water Pulse")
          print("4. Bubble Beam")
          while True:
            if keyboard.read_key() == "1":
              Water.hydro_pump(self, pokemon, enemypoké)
              break
            elif keyboard.read_key() == "2":
              Water.aqua_jet(self,pokemon,enemypoké)
              break
            elif keyboard.read_key()=="3":
              Water.water_pulse(self,pokemon,enemypoké)
              break
            elif keyboard.read_key()=="4":
              Water.bubble_beam(self,pokemon,enemypoké)
              break
        elif battoption == "1" and pokemon in normalpoke:
          print("1. Tackle")
          print("2. Quick Attack")
          print("3. Scratch")
          print("4. Giga Impact")
          while True:
            if keyboard.read_key() == "1":
              Normal.tackle(pokemon, enemypoké)
              break
            elif keyboard.read_key() == "2":
              Normal.quick_attack(pokemon,enemypoké)
              break
            elif keyboard.read_key()=="3":
              Normal.scratch(pokemon,enemypoké)
              break
            elif keyboard.read_key()=="4":
              Normal.giga_impact(pokemon,enemypoké)
              break
        
  # Example usage:
#pikachu.display_info()

# Planned starters:

#pikachu = Pokemon("Pichu", 0, "Electric",85)
#charmander = Pokemon("Charmander", 0, "Fire",90)
#squirtle = Pokemon("Squirtle", 0, "Water",85)
#bulbasaur = Pokemon("Bulbasaur", 0, "Grass",90)
#eevee = Pokemon("Eevee", 0, "Normal",85)  


# Create 5 more Normal type Pokemon instances
#NORMAL
pidgey = Pokemon("Pidgey", 0, "Normal", 90)
rattata = Pokemon("Rattata", 0, "Normal", 85)
meowth = Pokemon("Meowth", 0, "Normal", 95)
digglet = Pokemon("Digglet", 0, "Normal", 100)
snorlax = Pokemon("Munchlax", 0, "Normal", 115)

# Create 5 more Fire type Pokemon instances
flareon = Pokemon("Flareon", 0, "Fire", 90)
arcanine = Pokemon("Arcanine", 0, "Fire", 90)
rapidash = Pokemon("Ponyta", 0, "Fire", 85)
ninetales = Pokemon("Ninetales", 0, "Fire", 90)
magmar = Pokemon("Magmar", 0, "Fire", 85)
class Electric:  
  @staticmethod
  def Thunderbolt(pokemon, enemypoké):
      damage = 20
      print(f"{pokemon} used Thunderbolt! It did {damage} damage!")
      enemypoké.health = enemypoké.health - damage
      return enemypoké.health
  @staticmethod
  def Electro_Ball(pokemon, enemypoké):
      damage = random.randint(14, 17)
      print(f"{pokemon} used Electro Ball! It did {damage} damage!")
      enemypoké.health = enemypoké.health - damage
      return enemypoké.health
  @staticmethod
  def Electroweb( self, pokemon,enemypoké):
      damage = random.randint(11, 14)
      print(f"{pokemon} used Electroweb! It did {damage} damage!")
      enemypoké.health = enemypoké.health - damage
      return enemypoké.health
      
  @staticmethod
  def Thunder( self, pokemon,enemypoké):
      damage = random.randint(12, 16)
      print(f"{pokemon} used Thunder! It did {damage} damage!")
      enemypoké.health = enemypoké.health - damage
      return enemypoké.health

class Fire:  
  @staticmethod  
  def flame_thrower( self, pokemon, enemypoké):
      damage = random.randint(12, 15)
      print(f"{pokemon} used Flame Thrower! It did {damage} damage!")
      enemypoké.health -= damage
      return enemypoké.health
        
  @staticmethod  
  def fire_blast( self, pokemon, enemypoké):
      damage = random.randint(12, 15)
      print(f"{pokemon} used Fire Blast! It did {damage} damage!")
      enemypoké.health -= damage
      return enemypoké.health
  @staticmethod  
  def ember( self, pokemon, enemypoké):
      damage = random.randint(13,17)
      print(f"{pokemon} used Ember! It did {damage} damage!")
      enemypoké.health -= damage
      return enemypoké.health


class Water:
  @staticmethod
  def hydro_pump( self, pokemon, enemypoké):
    damage = random.randint(14, 18)
    print(f"{pokemon} used Hydro Pump! It did {damage} damage!")
    enemypoké.health -= damage
    return enemypoké.health
  @staticmethod 
  def bubble_beam( self, pokemon, enemypoké):
    damage = random.randint(13, 17)
    print(f"{pokemon} used Bubble Beam! It did {damage} damage!")
    enemypoké.health -= damage
    return enemypoké.health
  @staticmethod
  
  def water_pulse( self, pokemon, enemypoké):
    damage = random.randint(14, 17)
    print(f"{pokemon} used Water Pulse! It did {damage} damage!")
    enemypoké.health -= damage
    return enemypoké.health
  @staticmethod  
  def aqua_jet( self, pokemon, enemypoké):
    damage = random.randint(15, 18)
    print(f"{pokemon} used Aqua Jet! It did {damage} damage!")
    enemypoké.health -= damage
    return enemypoké.health
  
class Fighting:  
  @staticmethod
  def high_jump_kick(pokemon,enemypoké):
    damage = random.randint(14,16)
    print(f"{pokemon} used High Jump Kick! It did {damage} damage!")
    enemypoké.health -= damage
    return enemypoké.heal  @staticmethod
  
  def close_combat(pokemon,enemypoké):
    damage = random.randint(14,18)
    print(f"{pokemon} used Close Combat! It did {damage} damage!")
    enemypoké.health -= damage
    return enemypoké.heal  
  @staticmethod
  def aura_sphere(pokemon,enemypoké):
    damage = random.randint(13,17)
    print(f"{pokemon} used Aura Sphere! It did {damage} damage!")
    enemypoké.health -= damage
    return enemypoké.heal  @staticmethod
  
  def focus_blast(pokemon,enemypoké):
    damage = random.randint(14,16)
    print(f"{pokemon} used Focus Blast! It did {damage} damage!")
    enemypoké.health -= damage
    return enemypoké.health
    
class Psychic:  
  @staticmethod
  def psychic(pokemon,enemypoké):
    damage = random.randint(13,16)
    print(f"{pokemon} used Psychic! It did {damage} damage!")
    enemypoké.health -= damage
    return enemypoké.heal  @staticmethod
  
  def psycho_boost( pokemon , enemypoké):
    damage = random.randint(15,18)
    print(f"{pokemon} used Psycho Boost! It did {damage} damage!")
    enemypoké.health -= damage
    return enemypoké.heal  @staticmethod
  
  def psycho_cut( self, pokemon, enemypoké):
    damage = random.randint(14,16)
    print(f"{pokemon} used Psycho Cut! It did {damage} damage!")
    enemypoké.health -= damage
    return enemypoké.heal  @staticmethod
  
  def psybeam(pokemon,enemypoké):
    damage = random.randint(13,15)
    print(f"{pokemon} used Psybeam! It did {damage} damage!")
    enemypoké.health -= damage
    return enemypoké.health

class Rock:
  @staticmethod  
  def rock_throw(pokemon,enemypoké):
    damage = random.randint(14,16)
    print(f"{pokemon} used Rock Throw! It did {damage} damage!")
    enemypoké.health -= damage
    return enemypoké.health
  @staticmethod
  def rock_slide(pokemon,enemypoké):
    damage = random.randint(13,16)
    print(f"{pokemon} used Rock Slide! It did {damage} damage!")
    enemypoké.health -= damage
    return enemypoké.health  
  @staticmethod
  def stone_edge(pokemon,enemypoké):
    damage = random.randint(14,18)
    print(f"{pokemon} used Stone Edge! It did {damage} damage!")
    enemypoké.health -= damage
    return enemypoké.health  
  @staticmethod
  def stealth_rock(pokemon,enemypoké):
    damage =random.randint(13,16)
    print(f"{pokemon} used Stealth Rock! It did {damage} damage!")
    enemypoké.health -= damage
    return enemypoké.health  

class Normal:
  @staticmethod
  def quick_attack(pokemon,enemypoké):
    damage=random.randint(13,16)
    print(f"{pokemon} used Quick Attack! It did {damage} damage!")
    enemypoké.health -= damage
    return enemypoké.health
  @staticmethod
  def tackle(pokemon,enemypoké):
    damage=random.randint(12,15)
    print(f"{pokemon} used Tackle! It did {damage} damage!")
    enemypoké.health -= damage
    return enemypoké.health
  @staticmethod
  def scratch(pokemon,enemypoké):
    damage=random.randint(12,15)
    print(f"{pokemon} used Scratch! It did {damage} damage!")
    enemypoké.health -= damage
    return enemypoké.health
  @staticmethod
  def giga_impact(pokemon,enemypoké):
    damage=random.randint(14,18)
    print(f"{pokemon} used Giga Impact! It did {damage} damage!")
    enemypoké.health -= damage
    return enemypoké.health
class Ice:
  @staticmethod
  def icicle_spear(pokemon,enemypoké):
    possible_damage=random.randint(6,7)
    times = random.randint(2,5)
    damage=times*possible_damage
    print(f"{pokemon} used Icicle Spear! It did {damage} damage!")
    enemypoké.health -= damage
    return enemypoké.health
  @staticmethod
  def ice_beam(pokemon,enemypoké):
    damage=random.randint(13,18)
    print(f"{pokemon} used Ice Beam! It did {damage} damage!")
    enemypoké.health -= damage
    return enemypoké.health
  @staticmethod
  def snowstorm(pokemon,enemypoké):
    damage=random.randint(14,17)
    print(f"{pokemon} used Ice Fang! It did {damage} damage!")
    enemypoké.health -= damage
    return enemypoké.health
  