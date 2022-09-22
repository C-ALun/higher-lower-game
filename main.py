from art import logo, vs
from replit import clear
from game_data import data
import random


def random_pick(list):
    new_list = []
    for _ in range(2):
        new_list.append(random.choice(list))
    while new_list[0] == new_list[1]:
        new_list[1] = random.choice(list)

    return new_list

def format_data(list):
  name = list['name']
  description = list['description']
  country = list['country']

  return f"{name}, a {description}, from {country}."
  

def compare(list):
    a = list[0]
    print("Compare A: " + format_data(a)) 

    print(vs)

    b = list[1]
    print("Compare B: " + format_data(b)) 

    choose = input("Who has more followers? Type 'A' or 'B': ").upper()

    if a['follower_count'] > b['follower_count'] and choose == 'A':
      return True
    elif a['follower_count'] < b['follower_count'] and choose == 'B':
      return True
    else:
      return False


def game():
  is_game_over = False
  count = 0
  while not is_game_over:
    random_list = random_pick(data)
    answer = compare(random_list)

    if not answer:
      is_game_over = True
      message = f"Sorry, that's wrong. Final score: {count}"
    else:
      count += 1
      message = f"You're right! Current score: {count}."
    clear()
    print(logo)
    print(message)
    
print(logo)
game()