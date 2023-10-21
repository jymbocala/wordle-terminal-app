from PyDictionary import PyDictionary
dictionary=PyDictionary()

print(bool(dictionary.meaning("indentation")))
print(bool(dictionary.meaning("aware")))


class GameSession():
  def __init__(self, wordle, session_guesses=[]):
    self.wordle = wordle
    print("GAMESESSION >>>>> wordle is : " + str(wordle))

  # METHODS
  # 1. display user session guesses with colour indicators
  #


# a GameSession constitutes 6 game rounds where the player makes a guess each round
class GameRound(GameSession):
  def __init__(self, wordle):
    self.wordle = wordle

# METHODS - what can players do in a game round
  # validate word_guess
  def validate_word(word):
    print(f'validating {word}...')
    


  # 1. make a guess
  def make_guess(word_guess):
    print('The user has guessed the word ' + word_guess)



  # loop over guess word characters and check if it matches wordle_word characters