import os
from wonderwords import RandomWord
from rich import print
from rich.console import Console

console = Console(width=65)


class Options:
    def __init__(self):
        # Default settings
        self.word_length = 5
        self.display_keyboard = True

    def clear_screen(self):
        os.system('clear' if os.name == 'posix' else 'cls')

    def display_options(self):
        self.clear_screen()
        while True:
            print('\n[bold cyan]OPTIONS MENU[/bold cyan]\n\n')
            print('Available commands:')
            print('1. [bold magenta]length<number>[/]'
                ' - Adjust word length between 3-7 '
                'to increase or decrease difficulty, '
                'default is set to 5 (e.g., "length4")')
            print(
            '2. [bold magenta]keyboard[/] or [bold magenta]k[/] - Toggle keyboard display on/off')
            print(
                '3. [bold magenta]start[/] or [bold magenta]s[/]'
                ' - Start the game with updated settings')

            choice = input('\nType a command to change the setting: ')

            if choice.startswith('length'):
                try:
                    length = int(choice[6:])
                    if 3 <= length <= 7:
                        # Adjust the word length
                        self.set_word_length(length)
                        self.clear_screen()
                        print(f'[green4]Word length set to {
                            length}[/green4].\n')
                    else:
                        self.clear_screen()
                        print(
                            '[bold red]Invalid word length.[/bold red]'
                            'Please enter a number between 3 and 7.')
                except ValueError:
                    self.clear_screen()
                    print(
                        '[bold red]Invalid command format.[/bold red]'
                        'Use [bold]length[/bold] followed by a number'
                        '(e.g., "[bold]length5[/bold]").')

            elif choice.lower() == 'start' or choice.lower() == 's':
                return True  # Settings were adjusted, start game

            elif choice.lower() == 'keyboard' or choice.lower() == 'k':
                self.toggle_keyboard_display()
                self.clear_screen()
                keyboard_status = '[green4]ON[/]' if self.display_keyboard else '[red3]OFF[/]'
                print(f'Keyboard display toggled: {keyboard_status}')

            else:
                self.clear_screen()
                print(
                    '[bold red]Invalid command.[/bold red] '
                    'Please choose a valid command from the list.')

    def set_word_length(self, length):
        self.word_length = length

    def generate_wordle_word(self):
        return RandomWord().word(
            word_min_length=self.word_length, word_max_length=self.word_length
            ).upper()

    def toggle_keyboard_display(self):
        self.display_keyboard = not self.display_keyboard
