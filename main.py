import art
import game_data
import clear
from random import randint

print(art.logo)
print("Welcome to the higher lower game")
print("Choose 'higher' or 'lower'\n")


def equal_value(value, list):
  for x in list:
    if value == x:
      return True
  return False

def show_variante(my_list):
  comparisson = True
  while comparisson:
    idx = randint(0, len(game_data.data)-1)
    comparisson = equal_value(idx, my_list)
  my_list.append(idx)
  return idx

'''
Gewinn Meldung
'''
def you_win():
  print("\n***************************************")
  print("**********You Win, Next Round**********")
  print("***************************************\n")
 


def program():
  counter = 0
  play_again = True
  game_data_compare_list = []
  idx_A = show_variante(game_data_compare_list)
  game_data_compare_list.append(idx_A)
  while play_again:
    A = game_data.data[idx_A]['follower_count']
    idx_B = show_variante(game_data_compare_list)
    for value in game_data.data[idx_A]:
      print(f"{value}: {game_data.data[idx_A][value]}")    
    print(f"{art.vs}\n")
    for value in game_data.data[idx_B]:
      if value != 'follower_count':
        print(f"{value}: {game_data.data[idx_B][value]}")
    B = game_data.data[idx_B]['follower_count']
    print(f"Der Wert von B: {B}")
    # print(f"follower_count: {B}")
    print(f"\nIs '{game_data.data[idx_B]['name']}' follower count higher or lower than '{game_data.data[idx_B]['name']}'?")
    decission = input(f"\nChoose 'H' for 'Higher' or 'L' for 'Lower'\n")
    idx_A = idx_B
    if decission == 'H' and B > A:
      counter += 1
      you_win()
    elif decission == 'L' and A > B:
      counter += 1
      you_win()
    else:
      play_again = False
      print(f"You lose. Your score = {counter}")
    


  
    
program()

