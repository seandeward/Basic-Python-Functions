
class Character:
  def __init__(self, name,
      max_hp, max_stress, Evasion, maj_thresh, sev_thresh, armor_score, Strength, Agility, Finesse, Knowledge, Instinct, Presence):
    self.name = name
    self.hp = max_hp
    self.stress = max_stress
    self.evasion = Evasion
    self.major_threshold = maj_thresh
    self.severe_threshold = sev_thresh
    self.armor = armor_score
    self.strength = Strength
    self.agility = Agility
    self.finesse = Finesse
    self.knowledge = Knowledge
    self.instinct = Instinct
    self.presence = Presence
