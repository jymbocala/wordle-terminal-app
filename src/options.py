import os
from wonderwords import RandomWord
from rich import print
from rich.console import Console
console = Console(width=65)


class Options:
    def __init__(self):
        self.word_length = 5  # default word length

    def display_options(self):
        os.system('clear' if os.name == 'posix' else 'cls')
        while True:
            print('\n[bold cyan]OPTIONS MENU[/bold cyan]\n\n')
            print('Available commands:')
            print('1. [bold magenta]length<number>[/]'
                  ' - Adjust word length between 3-7 '
                  'to increase or decrease difficulty, '
                  'default is set to 5 (e.g., "length4")')
            print(
                '2. [bold magenta]start[/] or [bold magenta]s[/]'
                ' - Start the game with updated settings')

            choice = input('\nType a command to change the setting: ')

            if choice.startswith('length'):
                try:
                    length = int(choice[6:])
                    if 3 <= length <= 7:
                        # Adjust the word length
                        self.set_word_length(length)
                        os.system('clear' if os.name == 'posix' else 'cls')
                        print(f'[green4]Word length set to {
                              length}[/green4].\n')
                    else:
                        os.system('clear' if os.name == 'posix' else 'cls')
                        print(
                            '[bold red]Invalid word length.[/bold red]'
                            'Please enter a number between 3 and 7.')
                except ValueError:
                    os.system('clear' if os.name == 'posix' else 'cls')
                    print(
                        '[bold red]Invalid command format.[/bold red]'
                        'Use [bold]length[/bold] followed by a number'
                        '(e.g., "[bold]length5[/bold]").')

            elif choice.lower() == 'start' or choice.lower() == 's':
                return True  # Settings were adjusted, start game

            else:
                print(
                    '[bold red]Invalid command.[/bold red] '
                    'Please choose a valid command from the list.')

    def set_word_length(self, length):
        self.word_length = length

    def generate_wordle_word(self):
        return RandomWord().word(
            word_min_length=self.word_length, word_max_length=self.word_length
            ).upper()
