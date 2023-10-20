# IMPORTS
from wonderwords import RandomWord
import wordle
# MAIN
# Introduction
print('Welcome to Wordle! \n👋 Hello there! I\'m your Wordle companion. Before we dive into the word-guessing fun, may I know your name? Please type it below, and we\'ll get started:')
name = input(str('Enter your name:  '))
print(f'Great! Hi, {name}! It\'s nice to meet you. Now, let me explain how Wordle works. \n🧩 Wordle is a word-guessing game where you\'ll need to guess a secret five-letter word. You have six attempts to guess the word correctly. After each guess, I\'ll provide feedback to help you narrow down the possibilities. Each letter in the word will be color-coded to let you know if it\'s in the word, and if it\'s in the right position. Your goal is to crack the code as quickly as possible! \nTo make a guess, simply type a five-letter word, and I\'ll let you know how you\'re doing. \nAre you ready to start playing and put your word skills to the test? \n')


def start_new_game():
  print('START')
  wordle_word = RandomWord().word(word_min_length=5, word_max_length=5)
  print(f'The word was {wordle_word}')
  wordle.GameSession(wordle_word)

def user_help():
  print('Help')

def ask_if_player_is_ready():
  q = input(
    str('Type \'YES\' to begin or \'HELP\' if you\'d like more instructions: '))
  if q == 'YES' or q == 'yes':
    print('Starting new game...')
    start_new_game()
  elif q == 'HELP' or q == 'help':
    user_help()
  else:
    print('Oops! Please enter "YES" or "HELP".')
    ask_if_player_is_ready()

def game_finished():
  pass

# GAME SEQUENCE
ask_if_player_is_ready()

# word is sent to wordle.py class GameSession
# tell user to make a guess

