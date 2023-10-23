from PyDictionary import PyDictionary
dictionary = PyDictionary()


class GameSession():
  def __init__(self, wordle_word, ):
    self.wordle_word = wordle_word
    print("GAMESESSION >>>>> wordle is : " + str(wordle_word))

  # METHODS
  # display user session guesses with colour indicators


# a GameSession constitutes 6 game rounds where the player makes a guess each round
class GameRound(GameSession):
  # def __init__(self, wordle):
  #   self.wordle = wordle

  # validate word_guess
  def check_dictionary(word):
    print(f'checking: {word}...')
    is_in_dictionary = bool(dictionary.meaning(word))
    print(f'checking: {is_in_dictionary}')
    return is_in_dictionary

  # make a guess
  def make_guess(word_guess):
    print('The user has guessed the word ' + word_guess)
  # loop over guess word characters and check if it matches wordle_word characters
