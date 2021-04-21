from graphics import *
from random import randint

def gameBackground(win, hangMan):
    # Title 
    title = Text(Point(300, 50),"HangMan")
    title.setStyle("bold")
    title.setSize(36)
    title.draw(win)
    hangMan.append(title)
        
    # Hanger
    triangle = Polygon(Point(274,133), Point(274,190), Point(320,133))
    triangle.setWidth(6)
    triangle.draw(win)
    hangMan.append(triangle)
    
    vline = Rectangle(Point(270,130), Point(276,418))
    vline.setFill("black")
    vline.draw(win)
    hangMan.append(vline)
    
    hline = Rectangle(Point(270,130), Point(380,136))
    hline.setFill("black")
    hline.draw(win)
    hangMan.append(hline)
    
    vline2 = Rectangle(Point(374,130), Point(380,160))
    vline2.setFill("black")
    vline2.draw(win)
    hangMan.append(vline2)
    
    base = Rectangle(Point(190,412), Point(350,418))
    base.setFill("black")
    base.draw(win)
    hangMan.append(base)

def hangmanParts(wrongGuessCounter, win, hangMan): 
    if (wrongGuessCounter >= 1):
        head = Circle(Point(376,185), 25)
        head.draw(win)
        hangMan.append(head)

        if (wrongGuessCounter >= 2):
            body= Line(Point(376,210), Point(376,310))
            body.draw(win)
            hangMan.append(body)
            
            if (wrongGuessCounter >= 3):
                arm1 = Line(Point(376,235), Point(426,185))
                arm1.draw(win)
                hangMan.append(arm1)

                if (wrongGuessCounter >= 4):
                    arm2 = Line(Point(376,235), Point(326,185))
                    arm2.draw(win)
                    hangMan.append(arm2)

                    if (wrongGuessCounter >= 5):
                        foot1 = Line(Point(376,310), Point(416,360))
                        foot1.draw(win)
                        hangMan.append(foot1)

                        if (wrongGuessCounter >= 6):
                            foot2 = Line(Point(376,310), Point(336,360))
                            foot2.draw(win)
                            hangMan.append(foot2)

                            if (wrongGuessCounter >= 7):
                                eye1 = Text(Point(368,178), "X")
                                eye1.setStyle("bold")
                                eye1.setSize(14)
                                eye1.draw(win)
                                hangMan.append(eye1)

                                eye2 = Text(Point(384,178), "X")
                                eye2.setStyle("bold")
                                eye2.setSize(14)
                                eye2.draw(win)
                                hangMan.append(eye2)

                                if (wrongGuessCounter == 8):
                                    mouth = Line(Point(366,198), Point(386,198))
                                    mouth.draw(win)
                                    hangMan.append(mouth)

def winningTrophy(win, trophy):
    stick = Rectangle(Point(290, 340), Point(310, 260))
    stick.setWidth(3)
    stick.setFill(color_rgb(255,231,129))
    stick.draw(win)
    trophy.append(stick)

    cup = Oval(Point(220, 280), Point(380, 60))
    cup.setWidth(3)
    cup.setFill(color_rgb(255,231,129))
    cup.draw(win)
    trophy.append(cup)
        
    cupCover = Rectangle(Point(0, 60), Point(600, 170))
    cupCover.setWidth(3)
    cupCover.setFill("white")
    cupCover.setOutline("white")
    cupCover.draw(win)
    trophy.append(cupCover)
        
    cupTop = Rectangle(Point(220, 170), Point(380, 173))
    cupTop.setFill("black")
    cupTop.setOutline("black")
    cupTop.draw(win)
    trophy.append(cupTop)
        
    circ = Circle(Point(300, 320), 25)
    circ.setWidth(3)
    circ.setFill(color_rgb(255,231,129))
    circ.draw(win)
    trophy.append(circ)

    base1 = Rectangle(Point(250,320), Point(350,370))
    base1.setWidth(3)
    base1.setFill(color_rgb(165,82,7))
    base1.draw(win)
    trophy.append(base1)
        
    base2 = Rectangle(Point(220,360), Point(380,380))
    base2.setWidth(3)
    base2.setFill(color_rgb(214,215,216))
    base2.draw(win)
    trophy.append(base2)
        
    title = Text(Point(300, 50),"HangMan")
    title.setStyle("bold")
    title.setSize(36)
    title.draw(win)
    trophy.append(title)
        
def main():
    # Create the variable that holds the HangMan parts
    hangMan = []
    
    # Create the graphics window and set the background
    win = GraphWin("HangMan",600,700)
    win.setBackground("white")
    gameBackground(win, hangMan)
    
    # Create a word bank and get a random word from it
    wordBank = ["abandoned", "accompany", "ability", "abdomen", "backup", "balance", "beautiful", "believable", "calendar", "capacity", "calculation", "championship", "damage", "decrease", "departure", "development", "ecosystem", "economics", "earnings", "employment", "filmmaker", "financing", "flexible", "forecast", "generosity", "giant", "golden", "guarantee", "happen", "handsome", "historical", "hobby", "illegal", "imagine", "import", "ideal", "jacket", "journal", "junior", "journey", "kitchen", "knuckle", "knock", "kickoff", "ladder", "laugh", "leave", "library", "machine", "measure", "mineral", "mostly", "nature", "negative", "night", "nobody", "objection", "ocean", "offense", "operate", "painting", "parade", "peace", "photograph", "quantity", "quarterly", "quote", "racial", "reaction", "runway", "rhyme", "satisfy", "search", "scientist", "shadow", "tactful", "teacher", "theme", "technical", "ticket", "under", "union", "universal", "usually", "unable", "victory", "vacation", "vegetable", "volume", "waiter", "weakness", "whistle", "worship", "yellow", "yesterday", "yourself", "youth", "zapped", "zebra", "zipper"]
    word = wordBank[randint(0, len(wordBank) - 1)].upper()   
    wlen = len(word)
     
    # Create empty spaces for each letter of the random word and draw them
    guessedWord = "__"
    for i in range(wlen - 1):
        guessedWord = guessedWord + " __"
    
    space = Text(Point(300, 540), guessedWord)
    space.draw(win)

    # Create instructions message 
    instructions = Text(Point(300, 465), "Guess a letter to see if it is in the hidden word.")
    instructions.setSize(14)
    instructions.setStyle("bold")
    instructions.draw(win)
    
    # Create letter instructions and input box
    letterInstructions = Text(Point(285, 595), "Type a letter:")
    letterInstructions.setSize(14)
    letterInstructions.setStyle("bold")
    letterInstructions.draw(win)
    
    letterBox = Entry(Point(360, 593), 2)
    letterBox.draw(win)
    letterBox.setText("")
    
    # Create a guess button 
    guessButton = Rectangle(Point(509, 655), Point(585, 685))
    guessButton.setWidth(3)
    guessButton.draw(win)
    
    guessButtonLabel = Text(Point(547, 670), "GUESS")
    guessButtonLabel.setStyle("bold")
    guessButtonLabel.draw(win)

    # Create a Message Ad that will tell you what to do once you submit the letter
    messageAd = Text(Point(300, 485), "")
    messageAd.setStyle("bold")
    messageAd.draw(win)
    
    wrongGuessCounter = 0
    guessedLetters = []
    won = False
    
    # Create a while loop that will keep taking guesses of letters until the player 
    # reaches 8 wrong guesses or until the player wins the game
    while wrongGuessCounter < 8 and won == False:
        
        # We use the mouse click to proceed, if the player does not click the guess
        # button we continue the loop until he does
        mLoc = win.getMouse()
        if mLoc.getX() < 509 or mLoc.getX() > 585 or mLoc.getY() < 655 or mLoc.getY() > 685:
            continue

        # Create a variable with the input letter in upper case
        guess = letterBox.getText().upper()
        letterBox.setText("")
        
        # Verify that the guess is valid, if it isn't we continue the loop until it is
        if guess == "" or guess == " " or len(guess) != 1:
            messageAd.setText("The input '" + guess.upper() +"' is invalid. Try again!")
            continue
            
        # If the guessed letter is in the word (and hasn't been guessed yet by the player) we 
        # put this letter in the according empty spaces 
        if guess in word.upper() and not(guess in guessedLetters):
            guessedLetters.append(guess)
            guessedWord = word
            
            for letter in word:
                if (not (letter.upper() in word) or not(letter.upper() in guessedLetters)) and letter != " ":
                    guessedWord = guessedWord.replace(letter, " __ ")
                
                space.setText(guessedWord)

            if guessedWord == word:
                won = True
            
            else:
                messageAd.setText(guess.upper() + " is in the word.")
        
        
        # If the letter has already been guessed, notify the player and wait for another guess
        elif guess in guessedLetters:
            messageAd.setText("You have already guessed " + guess.upper() + ". Try again!")
        
        # If it was a wrong guess Wrong guess! Add one to the counter and draw a new part of the HangMan 
        else:
            wrongGuessCounter = wrongGuessCounter + 1
            hangmanParts(wrongGuessCounter, win, hangMan)
            guessedLetters.append(guess)
            messageAd.setText(guess.upper() + " is a wrong guess. Try again!")



    # Undraw the instructions, ads and guess button
    instructions.undraw() 
    letterInstructions.undraw()
    letterBox.undraw()
    guessButton.undraw()
    guessButtonLabel.undraw()
    messageAd.undraw()
    
    # Display the word that was randomly chosen
    space.setText(word.upper())
    space.move(0,+ 20)
    space.setStyle("bold")
    space.setSize(16)
    
    # Display a win or loss message
    if won == True:
        message = Text(Point(300, 485), "You Won!")
        message.setSize(36)
        message.draw(win)
        
        for hM in hangMan:
            hM.undraw()
            
        hangMan = []
        trophy = []
        
        winningTrophy(win, trophy)  
        
    else:
        message = Text(Point(300, 485),"You Lost!")
        message.setSize(36)
        message.draw(win)

    # Play again button
    playAgain = Rectangle(Point(475, 655), Point(585, 685))
    playAgain.setWidth(3)
    playAgain.draw(win)
    
    playAgainLabel = Text(Point(530, 670), "PLAY AGAIN")
    playAgainLabel.setStyle("bold")
    playAgainLabel.draw(win)

    # Quit game button
    quitGame = Rectangle(Point(15, 655), Point(65, 685))
    quitGame.setWidth(3)
    quitGame.draw(win)
    
    quitGameLabel = Text(Point(40, 670), "QUIT")
    quitGameLabel.setStyle("bold")
    quitGameLabel.draw(win)

    # We use the mouse click to proceed, if the player choses to play again the 
    # page will close and another gamw will start and if he chooses to quit the 
    # window will close
    mLoc = win.getMouse()
    if mLoc.getX() >= 475 and mLoc.getX() <= 585 and mLoc.getY() >= 655 and mLoc.getY() <= 685:
        win.close()
        main()

    if mLoc.getX() >= 15 and mLoc.getX() <= 65 and mLoc.getY() >= 655 and mLoc.getY() <= 685:
        win.close()

main()     
