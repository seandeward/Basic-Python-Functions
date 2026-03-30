
from termcolor import colored
from time import sleep

color_list = ['red', 'green', 'blue', 'yellow', 'black', 'magenta', 'cyan', 'white', 'grey']

while True:
  for color in color_list:
    print(colored(f"Hello, I'm {color}!", color=color))
    sleep(0.1)
