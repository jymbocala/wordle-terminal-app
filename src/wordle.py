# from enchant import enchant
# d = enchant.Dict("en")

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
  # 1. make a guess
  def make_guess(self, word_guess):
    pass

  # validate word_guess
  # def validate_word_guess(self, word_guess):
  #   self.word_guess = word_guess
  #   if
