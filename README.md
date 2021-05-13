# HangMan

## Introduction
HangMan is a guessing game were the computer chooses a random word from a word bank and you have to guess it by submitting letters within a range of 8 guesses.

## Libraries
The libraries used during this project where `graphics.py` and `random.py`

## Code Explanation
  - We started by importing * from the graphics library and randint from the random library. Then, we created the graphics window and set up the backgroung color, hanger and title. Also, we created a word bank and created a varieble that will hold a random word from the word bank. With the length of the word we created empty spaces for each letter of the random word and drew them
  - After we had all that we created and dres the instructions, entry box, a guess button and a message Ad.
  - For the core of the game we used a while loop that will keep taking guesses of letters until the player reaches 8 wrong guesses or until the player wins the game. Inside of this while loop we verified that the input was valid. Also, we checked if the letter had already been guessed notify the player and wait for another guess; if the guessed letter is in the word and hasn't been guessed yet by the player, we put this letter in the according empty spaces; and if it was a wrong guess we added one to the counter and draw a new part of the HangMan.
  - Once the game is finished we undraw the instructions, ads and guess button. Then, display the word that was randomly chosen and a win or loss message.
  - At last, we ask the player if he wants to play again or quit, if the player choses to play again the page will close and another game will start and if he chooses to quit the  window will close

##References:
https://github.com/Tom25/Hangman
