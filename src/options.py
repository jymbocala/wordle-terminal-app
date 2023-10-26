import os
from wonderwords import RandomWord


class Options:
  def __init__(self):
    self.word_length = 5  # default word length

  def display_options(self):
    os.system('clear' if os.name == 'posix' else 'cls')
    while True:
      print("OPTIONS MENU")
      print("Available commands:")
      print("1. Adjust word length from 3-7 to increase or decrease difficulty, default is set to 5 (e.g., 'length4')")
      print("2. Start the game with updated settings (type 'start' or 's')")

      choice = input("Type a command to change the setting: ")

      if choice.startswith("length"):
        try:
          length = int(choice[6:])
          if 3 <= length <= 7:
            # Adjust the word length
            self.set_word_length(length)
            os.system('clear' if os.name == 'posix' else 'cls')
            print(f"Word length set to {length}.\n\n\n")
          else:
            os.system('clear' if os.name == 'posix' else 'cls')
            print("Invalid word length. Please enter a number between 3 and 7.")
        except ValueError:
          os.system('clear' if os.name == 'posix' else 'cls')
          print(
            "Invalid command format. Use 'length' followed by a number (e.g., 'length5').")

      elif choice.lower() == "start" or choice.lower() == "s":
        return True  # Settings were adjusted, and the game should start

      else:
        print("Invalid command. Please choose a valid command from the list.")

  def set_word_length(self, length):
    self.word_length = length

  def generate_wordle_word(self):
    return RandomWord().word(word_min_length=self.word_length, word_max_length=self.word_length).upper()
