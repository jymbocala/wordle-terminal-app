# IMPORTS
from wonderwords import RandomWord
import wordle

# MAIN
if __name__ == "__main__":
  # Introduction
  print('Welcome to Wordle! \n👋 Hello there! I\'m your Wordle companion. Before we dive into the word-guessing fun, may I know your name? Please type it below, and we\'ll get started:')
  name = input(str('Enter your name:  '))
  print(f'Great! Hi, {name}! It\'s nice to meet you. Now, let me explain how Wordle works. \n🧩 Wordle is a word-guessing game where you\'ll need to guess a secret five-letter word. You have six attempts to guess the word correctly. After each guess, I\'ll provide feedback to help you narrow down the possibilities. Each letter in the word will be color-coded to let you know if it\'s in the word, and if it\'s in the right position. Your goal is to crack the code as quickly as possible! \nTo make a guess, simply type a five-letter word, and I\'ll let you know how you\'re doing. \nAre you ready to start playing and put your word skills to the test? \n')

  def user_help():
    # print some helpful information about how the game works
    pass

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

  wordle_word = RandomWord().word(word_min_length=5, word_max_length=5)
  print(f'Wordle_word: {wordle_word}')

  # Create an instance of the GameSession with the word set to wordle_word variable
  game = wordle.GameSession(wordle_word)
  game_round = wordle.GameRound()

  # === GAME SEQUENCE ====
  ask_if_player_is_ready()

  # this while loop will run as long as game is not over
  while not game.is_game_over():
    # tell user to make a guess
    print('Please type a five-letter word to get started.')
    # user inputs a guess
    player_guess = game_round.get_player_guess()
    # give feedback to the user about their guess
    feedback = game.make_guess(player_guess)
    print(feedback)


  # TODO:
  # finish setting 'game over' state
  # re-add the while loop
  # make display method work
