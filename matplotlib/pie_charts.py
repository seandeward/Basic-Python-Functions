
#* calculate all the stuff
def get_hits_per_day(total:int, day_amount:int):
  return total / day_amount

#* how many days since march 9th?
days = int(8)

programs = {
  'chatgpt'  :  int(300),
  'claude'  :   int(23),
  'copilot'  :  int(42),
  'deepseek' :  int(0),
  'gemini'  :   int(400),
  'grok'   :    int(0),
  'perplexity': int(0),
  'grammarly' : int(11)
}

pie_labels = []
pie_values = []
for key in programs:
  value = int(programs[key])
  if value == int(0):
    continue
  if key != 'grammarly':
    value = get_hits_per_day(value, days)
  pie_labels.append(key)
  pie_values.append(value)

#* run the graph
if __name__ == "__main__":
  import matplotlib.pyplot as plt
  import numpy as np

  y = np.array(pie_values)

  plt.pie(y, labels=pie_labels)
  plt.show()
