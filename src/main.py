# IMPORTS
from wonderwords import RandomWord
import wordle

# MAIN
if __name__ == "__main__":
  # Introduction
  print('Welcome to Wordle! \n👋 Hello there! I\'m your Wordle companion. Before we dive into the word-guessing fun, may I know your name? Please type it below, and we\'ll get started:')
  name = input(str('Enter your name:  '))
  print(f'Great! Hi, {name}! It\'s nice to meet you. Now, let me explain how Wordle works. \n🧩 Wordle is a word-guessing game where you\'ll need to guess a secret five-letter word. You have six attempts to guess the word correctly. After each guess, I\'ll provide feedback to help you narrow down the possibilities. Each letter in the word will be color-coded to let you know if it\'s in the word, and if it\'s in the right position. Your goal is to crack the code as quickly as possible! \nTo make a guess, simply type a five-letter word, and I\'ll let you know how you\'re doing. \nAre you ready to start playing and put your word skills to the test? \n')

  wordle_word = RandomWord().word(word_min_length=5, word_max_length=5)
  print(f'Wordle_word: {wordle_word}')
  
  game = wordle.GameSession(wordle_word)
  

  def user_help():
    pass
    # print some helpful information about how the game works

  def ask_if_player_is_ready():
    q = input(
      str('Type \'YES\' to begin or \'HELP\' if you\'d like more instructions: '))
    if q == 'YES' or q == 'yes':
      print('Starting new game...')
      
    elif q == 'HELP' or q == 'help':
      user_help()
    else:
      print('Oops! Please enter "YES" or "HELP".')
      ask_if_player_is_ready()



  # === GAME SEQUENCE ====
  ask_if_player_is_ready()
  # word is sent to wordle.py class GameSession
  # tell user to make a guess
  print('Please type a five-letter word to get started.')

  # user inputs a guess
  # guess word is sent to wordle.py class GameRound
  player_guess = ''


  def guess_word():
    player_guess = input(str('Guess 1/6: '))
    # check if word is 5 characters long
    if len(player_guess) != 5:
      print('Please enter a five-letter word!')
      guess_word()
    else:
      # check if word is in the dictionary
      is_in_dictionary = wordle.GameRound.check_dictionary(player_guess)
      if not is_in_dictionary:
        print(f'Could not find the word "{
              player_guess}" in the dictionary. Try again.')
        guess_word()
      else:
        print(f'"{player_guess}" is in the dictionary!')
    
    print('WILL THIS PRINT EVERYTIME I MAKE AN ERROR GUESS??')
    # answer for above: this prints at the end of this function.. but = to the amount of errors


  guess_word()


  # wordle.GameRound.make_guess(player_guess)

  # validate word guess with if statement

  # it valdiates that the word is an english word and is 5 characters length
