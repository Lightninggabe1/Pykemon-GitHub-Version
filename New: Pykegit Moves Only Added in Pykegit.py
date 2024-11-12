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