# U.S. States Game  

This project is an interactive game built using Python and the Turtle graphics library, designed to help users learn and memorize the names and positions of all 50 U.S. states on a map.  
<br>


<p align='center'>
  <a>
    <img src='https://github.com/user-attachments/assets/324e8055-6b4d-45b1-8250-faf5f9dbceef' width=400>
  </a>
</p>


## How It Works  
- At the start of the game, a blank U.S. map is displayed.  
- The user is prompted to input the name of a U.S. state.  
- If the guessed state is correct, the state name is displayed on the map in its correct location.  
- The game tracks the number of correct guesses out of 50.  
- The game ends when the user either:  
  - Guesses all 50 states,  
  - Types `Exit`, or  
  - Cancels the input box.  
- When the game ends, a CSV file (`Missed States.csv`) is generated, listing the states that were not guessed.  

## Features  

- **Visual Map**: A graphical representation of the U.S. map.  
- **Score Tracking**: Displays the number of states correctly guessed.  
- **Missed States File**: Automatically saves a list of missed states to a CSV file for further study.  
- **Replayability**: Users can restart the game to practice and improve.  

## File Descriptions

- **`50_states.csv`**: Contains the state names and their respective x, y coordinates on the map.  
- **`blank_states_img.gif`**: A blank U.S. map image used as the background.  
- **`states.py`**: Contains the `States` class to manage the visualization of guessed states.  
- **`score_board.py`**: Contains the `ScoreBoard` class to manage the score and end-of-game messages.  
- **`main.py`**: The main file that controls the game logic and user interactions.  

## Prerequisites  

Ensure you have Python installed and the following libraries available:  
- `turtle` (built-in with Python)  
- `pandas`  

To install pandas, run:  
```bash  
pip install pandas
```

## How to Run the Game

1. Clone the repository:
   ```bash  
    git clone https://github.com/your-username/us-states-game.git  
    ```
   
2. Navigate to the project folder:
   ```bash  
    cd us-states-game  
    ```
   
3. Run the game:
   ```bash  
    python main.py  
    ```

## Game Controls

- Type the name of a U.S. State into the input box.
- Press ``Enter`` to submit your guess.
- Type ``Exit`` to quit the game and generate the missed states file.

## Learning Outcome

This game provides an engaging way to learn U.S. geography by associating state names with their locations on a map.
