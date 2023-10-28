# Wordle by Jym 

******

### Installation and Gameplay
1. **Check Python Install Status**: Wordle requires Python 3 or higher to run.

    To check if Python is installed and verify its current version, open a new terminal window and enter the following command:
    ```bash
    python3 --version
    ```
    This should return a message with the Python version, such as:
    ```
    Python 3.10.1
    ```
    If Python is not installed or the version is lower than 3.0, please visit the official [Python download page](https://www.python.org/downloads/) for installation instructions.

2. **Download and Install Wordle**: 
    - Visit the [Wordle Terminal App GitHub Repository](https://github.com/jymbocala/wordle-terminal-app).
    - In the repository, click on the "Code" tab, and select "Download ZIP" to download the Wordle files.

        

3. **Play Wordle**: 
    Open a new terminal window and navigate to the directory where you've placed the Wordle repository. The navigation command may look like this:
    ```bash
    cd path/to/wordle
    ```
    From within the `wordle` directory, execute the Wordle script by running the following command:
    ```bash
    bash wordle_script.sh
    ```
    This script will activate a virtual environment, install the required dependencies, and run the game in Python.

    *Note: If you encounter permissions errors, you may need to allow execution. Run the following commands from the `src` directory in the terminal window:
    ```bash
    chmod +x ./wordle_script.sh
    ```

4. **Playing Wordle**: 
    - To play Wordle, guess the secret five-letter word.
    - After each guess, you'll receive feedback using color indicators:
      - Green: Correct letter in the right position.
      - Orange: Correct letter in the wrong position.
      - Grey: Incorrect letter.
    - Try to guess the word within six attempts to win!

Have fun playing Wordle!

******

### Required Dependencies:
```
astroid==3.0.1
beautifulsoup4==4.12.2
bs4==0.0.1
certifi==2023.7.22
charset-normalizer==3.3.0
click==8.1.7
dill==0.3.7
futures==3.0.5
goslate==1.5.4
idna==3.4
isort==5.12.0
markdown-it-py==3.0.0
mccabe==0.7.0
mdurl==0.1.2
pep8==1.7.1
platformdirs==3.11.0
pycodestyle==2.11.1
PyDictionary==2.0.1
Pygments==2.16.1
pylint==3.0.2
requests==2.31.0
rich==13.6.0
soupsieve==2.5
tomlkit==0.12.1
urllib3==2.0.7
wonderwords==2.2.0
```