import enchant

class GameSession():
  def __init__(self, wordle, session_guesses=[]):
    self.wordle = wordle

  # METHODS
  # 1. display user session guesses with colour indicators
  # 



# a GameSession constitutes 6 game rounds where the player makes a guess each round
class GameRound(GameSession):
  def __init__(self,wordle, user_guess):
    super().__init(self, wordle)
    user_guess = user_guess

# METHODS - what can players do in a game round
  # 1. make a guess
  pass