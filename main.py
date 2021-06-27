import art
import game_data
from random import randint

print(art.logo)
print("Welcome to the higher lower game")
print("Choose 'higher' or 'lower'")

def show_variante(my_list):
  comparisson = True
  while comparisson:
    idx = randint(0, len(game_data.data)-1)
    for value in my_list:
      if value == idx:
        comparisson = False
      else:
        return
    comparisson = False
  my_list.append(idx)
  return idx
  
  # my_list.append(idx)
  # print(f"Index = {idx}")
  # for value in my_list:
  #   print(f"print listenvalues: {value}")


def program():
  game_data_compare_list = []
  value_A = show_variante(game_data_compare_list)
  value_B = show_variante(game_data_compare_list)
  print(f"Variante A = {value_A}")
  print(f"Variante B = {value_B}")
  
    
program()

