
class Fighter:
  def __init__(self, name, health, stamina, mana):
    self.name = name
    self.health = health
    self.stamina = stamina
    self.mana = mana


fighter_one = Fighter('guy', 100, 80, 0)

print(f"[-] Fighter_one")
print(f"      - Name = {fighter_one.name}")
print(f"      - Health = {fighter_one.health}")
print(f"      - Stamina = {fighter_one.stamina}")
print(f"      - Mana = {fighter_one.mana}")
