import os


class Options:
  def __init__(self):
    self.wordle_word = None
    self.settings_adjusted = False

  def display_options(self):
    os.system('clear' if os.name == 'posix' else 'cls')
    while True:
      print("Available commands:")
      print("1. Adjust word length (e.g., 'length5')")
      print("2. Exit options menu with adjusted settings (type 'exit' or 'x')")

      choice = input("Type a command to change the setting: ")

      if choice.startswith("length"):
        # Adjust word length
        # Set self.wordle_word accordingly
        pass  # Implement this part
      elif choice.lower() == "exit" or choice.lower() == "x":
        print("Exiting the options menu.")
        self.settings_adjusted = True
        break
      else:
        print("Invalid command. Please choose a valid command from the list.")
