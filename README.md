# Connect4 Terminal Game

Terminal Connect4 is a Python implementation of the classic game Connect4, designed to be played in the terminal. This project allows you to enjoy the popular two-player game against a bot opponent, providing a challenging and interactive experience right from your command line.

You can find the live Demo here! - https://terminal-connect4.herokuapp.com/

- [Connect4 Terminal Game](#connect4-terminal-game)
  * [Features](#features)
    * [Existing Features](#existing-features)
  * [Testing](#testing)
    * [Validator Testing](#validator-testing)
  * [Deployment](#deployment)
  * [Development](#development)
    * [External Python Packages Used](#external-python-packages-used)
  * [Credits](#credits)
    * [Content](#content)

## Features

### Existing Features

  - Terminal User Interface
    - A terminal was used as a means to display the state of the game and allow users to interact with it.
    - To improve user experience the terminal app library [blessed](https://pypi.org/project/blessed/) was used which allowed for better visuals and easier input handling.
    - To allow for a easier and more modular way of displaying the state of a [Game](https://github.com/DebuggedMoon/terminal-connect4/blob/main/game.py), the [TerminalGame](https://github.com/DebuggedMoon/terminal-connect4/blob/main/terminalgame.py) class was written to handle everything Terminal and [blessed](https://pypi.org/project/blessed/) related.
    - The Terminal UI controls and switches between a number of screens to achieve more of a video game feeling:
      - The `Starting Screen` welcomes players and gives a short and hyped summary of the game.
        ![Starting Screen](docs/images/starting_screen.webp)
      - The `Tutorial Screen` gives the player information about the game and teaches them on how to play it.
        ![Tutorial Screen](docs/images/tutorial.webp)
      - The `Game Screen` displays the playfield of the game and gives the user feedback for his input.
        ![Game Screen](docs/images/game-screen.webp)

## Testing

### Validator Testing 
 - Pylint was used with for validating the python files. All python files were checked and no warnings were found!

## Installation & Usage

You can install and run it locally by following the steps below:

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Set Up a Virtual Environment (Optional but Recommended)

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
### 3. Install Dependencies

Install required packages using the provided requirements.txt file:

```bash
pip install -r requirements.txt
```
>💡 If you add new packages, update requirements.txt with:
>```bash
>pip freeze --local > requirements.txt
>```

### 4. Run the Game
Launch the game directly from your terminal
```bash
python run.py
```

## Development

### External Python Packages Used

 - [blessed](https://pypi.org/project/blessed/) was used to allow for easier creation of the application and input handling.

## Credits

### Content

 - The idea to use blessed was inspiried by [Eoin](https://github.com/eoinlarkin).