import tkinter as tk
import random
from tkinter import messagebox
from tkinter import font as tkFont
from Algorithms import *


bg_color = "#1e1e1e"
fg_color = "grey"
selected_color = "white"
chosenNumber = None
chosenStarter = None
chosenAlgorithm = None
numberButtons = []
starterButtons = []
algorithmButtons = []
humanPoints = 0
aiPoints = 0
bankPoints = 0
isPlayersTurn = None
userWins = 0
computerWins = 0
winner = ""

root = tk.Tk()
root.title("1. praktiskais darbs")
root.geometry("500x500")
root.config(bg=bg_color)
root.option_add("*background", bg_color)
root.option_add("*foreground", fg_color)


def randomNumbers():
    count = 0
    randomlist = []

    while count < 5:
        num = random.randint(20000, 30000)
        if num % 12 == 0:
            randomlist.append(num)
            count += 1
    return randomlist

def scoreUpdateH(divisor):
    global humanPoints, aiPoints, bankPoints, isPlayersTurn, chosenNumber
    result = chosenNumber / divisor
    if isPlayersTurn:
        if result % 2 == 0:
            humanPoints -= 1
            print(f" Point goes away from : {isPlayersTurn}, human", {chosenNumber}, {divisor})
        else:
            humanPoints += 1
            print(f" Point goes to : {isPlayersTurn}, Human")
        if result % 5 == 0:
            bankPoints += 1
            print(f"Round Over! Point to the bank goes from: {isPlayersTurn}, Human")
    else:
        humanPoints +=1
        print(f" Point OMGGGGGGGGGG : {isPlayersTurn}, Human")     

def scoreUpdate(state, divisor):
    global humanPoints, aiPoints, bankPoints, isPlayersTurn, chosenNumber
    #terminal_value = check_terminal(state)
    #print(f"Terminal Value: {terminal_value}, Chosen Number at Terminal: {state['chosenNumber']}")
    Test = state['chosenNumber']/divisor
    print(f"Testa value: {Test}")
    if not isPlayersTurn:
        if Test % 2 == 0:
            aiPoints -= 1
            print(f" Point goes away from : {isPlayersTurn}, AI")
        else:
            aiPoints += 1
            print(f" Point goes to : {isPlayersTurn}, AI", {chosenNumber}, {divisor})
        if Test % 5 == 0:
            bankPoints += 1
            print(f"Round Over! Point to the bank goes from: {isPlayersTurn}, AI")
    else:
        aiPoints += 1
        print(f" Point WTFFFFFFFFFFFFFF : {isPlayersTurn}, Human")

    # Update the chosenNumber with the result of the division

def gameOver():
    global humanPoints, aiPoints, bankPoints, isPlayersTurn, chosenNumber
    # Game ends when the chosen number is below or the same as 10
    if chosenNumber <= 10:
        PointCount()
        return True

    # Game ends if there are no more legal moves left
    legal_moves = [chosenNumber % div == 0 for div in [2, 3, 4]]
    if not any(legal_moves):
        PointCount()
        return True
    
    return False

def PointCount():
    global humanPoints, aiPoints, isPlayersTurn, bankPoints
    if isPlayersTurn:
        aiPoints += bankPoints
        bankPoints = 0
    else:
        humanPoints += bankPoints
        bankPoints = 0

def WhoWins():
    if humanPoints > aiPoints:
        print(f"HUMAN WON {aiPoints}, {humanPoints}")
        return("User")  # Call the end game screen
    elif humanPoints < aiPoints:
        print(f"COMPUTER WON {aiPoints}, {humanPoints}")
        return("Computer")
    else:
        print(f"DRAWWWWWW {aiPoints}, {humanPoints}")
        return("Draw")


def updateButtonSelection(buttonsList, selectedButton):
    # Updates the button selection to know what you have pressed
    for btn in buttonsList:
        btn.config(bg=bg_color, fg=fg_color)  
    selectedButton.config(bg=selected_color, fg=bg_color)  


def clearWidgets():
    # Clears the initial UI window to make  space for new widgets
    for widget in root.winfo_children():
        widget.destroy()


def selectStarter(starter):
    #Select either User or Computer to start the game and call update the list
    global chosenStarter
    chosenStarter = starter
    updateButtonSelection(starterButtons, starterButtons[0] if starter == "User" else  starterButtons[1])
    print("The game is gona start: ", starter)


def selectAlgorithm(algorithm):
    # Choose the algorithm Minimax or Alpha-Beta and update the list
    global chosenAlgorithm
    chosenAlgorithm = algorithm
    updateButtonSelection(algorithmButtons, algorithmButtons[0] if algorithm == "Minimax" else algorithmButtons[1])
    print("You chose: ", algorithm)


def selectNumber(btn, number):
    # Choose one of the offered numbers
    global chosenNumber
    chosenNumber = number
    for button in numberButtons:  
        button.config(bg=bg_color, fg=fg_color)
    btn.config(bg=selected_color, fg=bg_color)  
    root.update_idletasks()  
    print("Selected number: ", number)


def startNewGame():
    global humanPoints, aiPoints, bankPoints, isPlayersTurn, chosenStarter, chosenNumber, chosenAlgorithm

    humanPoints = 0
    aiPoints = 0
    bankPoints = 0
    isPlayersTurn = None
    chosenStarter = None
    chosenNumber = None
    chosenAlgorithm = None

    clearWidgets()
    startGameScreen()


def quitGame():
    root.destroy()


def startGameScreen(): # 1. screen Choose parameters for the game
    global starterButtons, numberButtons

    numbers = randomNumbers()
    
    textWhoStarts = tk.Label(root, text="Choose who starts the game!")
    textWhoStarts.grid(row=0, column=0, columnspan=3, padx=5, pady=5)
    
    user = tk.Button(root, text="User", bg=bg_color, fg=fg_color, command=lambda: selectStarter("User"))
    user.grid(row=1, column=0, padx=5, pady=5)
    # Update list
    starterButtons.append(user)

    computer = tk.Button(root, text="Computer", bg=bg_color, fg=fg_color, command=lambda: selectStarter("Computer"))
    computer.grid(row=1, column=1, padx=5, pady=5)
    #Update list
    starterButtons.append(computer)

    global algorithmButtons
    textAlgorithmChoice = tk.Label(root, text="Choose algorithm!")
    textAlgorithmChoice.grid(row=2, column=0, columnspan=3, padx=5, pady=5)
     
    minimax = tk.Button(root, text="Minimax", bg=bg_color, fg=fg_color, command=lambda: selectAlgorithm("Minimax"))
    minimax.grid(row=3, column=0, padx=5, pady=5)
    #Update list
    algorithmButtons.append(minimax)

    alphaBeta = tk.Button(root, text="Alpha Beta", bg=bg_color, fg=fg_color, command=lambda: selectAlgorithm("Alpha Beta"))
    alphaBeta.grid(row=3, column=1, padx=5, pady=5)
    #Update list
    algorithmButtons.append(alphaBeta)

    global numberButtons
    numbers = randomNumbers()
    textStartingNumber = tk.Label(root, text="Choose a starting number:", bg=bg_color, fg=fg_color)
    textStartingNumber.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

    row_offset = 5
    for idx, number in enumerate(numbers):
        # Correctly define the lambda to capture both btn and num at the current loop iteration
        btn = tk.Button(root, text=str(number), bg=bg_color, fg=fg_color)
        btn['command'] = lambda b=btn, num=number: selectNumber(b, num)  # Use default arguments to capture current button and number
        btn.grid(row=row_offset + idx // 3, column=idx % 3, padx=5, pady=5)
        numberButtons.append(btn)

    startGameButton = tk.Button(root, text='Start Game', bg=bg_color, fg=fg_color, command=gameScreen)
    startGameButton.grid(row=10, column=0, columnspan=3, padx=5, pady=20)

def scoreLabel():
    global bankPoints, humanPoints, aiPoints
    tk.Label(root, text=f"----------Points----------", bg=bg_color, fg=fg_color).grid(row=2, column=0, columnspan=10, padx=5, pady=5, sticky='w')
    tk.Label(root, text=f"User: {humanPoints}", bg=bg_color, fg=fg_color).grid(row=3, column=0, columnspan=1, padx=5, pady=5, sticky='w')
    tk.Label(root, text=f"Computer: {aiPoints}", bg=bg_color, fg=fg_color).grid(row=3, column=1, columnspan=1, padx=5, pady=5, sticky='w')
    tk.Label(root, text=f"Bank: {bankPoints}", bg=bg_color, fg=fg_color).grid(row=3, column=2, columnspan=1, padx=5, pady=5, sticky='w')

def divide_number(divider, number_label, edgeLabel):
    global chosenNumber, isPlayersTurn, humanPoints, aiPoints

    if chosenNumber % divider != 0:
        messagebox.showerror("Error", "Division result is not a whole number!")
        return
    else:
        scoreUpdateH(divider)
        scoreLabel()
        chosenNumber //= divider
        number_label.config(text=chosenNumber)
        isPlayersTurn = False

    state = {'chosenNumber': chosenNumber, 'aiPoints': aiPoints, 'humanPoints': humanPoints}
    edges_visited = ai_make_move(state, number_label)
    edgeLabel.config(text=f"Edges visited by {chosenAlgorithm}: {edges_visited}")

def gameScreen(): # 2. screen 
    global chosenStarter, chosenNumber, chosenAlgorithm, humanPoints, aiPoints, isPlayersTurn

    if chosenStarter and chosenNumber and chosenAlgorithm: 
        clearWidgets()

        largeFont = tkFont.Font(size=24)  

        tk.Label(root, text=f"Algorithm: {chosenAlgorithm}", bg=bg_color, fg=fg_color).grid(row=0, column=0, columnspan=10, padx=5, pady=(20, 0), sticky='w')
        tk.Label(root, text=f"Starter: {chosenStarter}", bg=bg_color, fg=fg_color).grid(row=1, column=0, columnspan=10, padx=5, pady=(10, 20), sticky='w')

        scoreLabel()

        number_label = tk.Label(root, text=f"{chosenNumber}", bg=bg_color, fg=fg_color, font=largeFont)
        number_label.grid(row=4, column=0, columnspan=10, padx=5, pady=20, sticky='w')

        divider2 = tk.Button(root, text="2", bg=bg_color, fg=fg_color, font=tkFont.Font(size=15), command=lambda: divide_number(2, number_label, edgeLabel))
        divider2.grid(row=5, column=0, columnspan=1, padx=5, pady=5)

        divider3 = tk.Button(root, text="3", bg=bg_color, fg=fg_color, font=tkFont.Font(size=15), command=lambda: divide_number(3, number_label, edgeLabel))
        divider3.grid(row=5, column=1, columnspan=1, padx=5, pady=5)

        divider4 = tk.Button(root, text="4", bg=bg_color, fg=fg_color, font=tkFont.Font(size=15), command=lambda: divide_number(4, number_label, edgeLabel))
        divider4.grid(row=5, column=2, columnspan=1, padx=5, pady=5)

        edgeLabel = tk.Label(root, text=f"Computer visited edges: ", bg=bg_color, fg=fg_color)
        edgeLabel.grid(row=6, column=0, columnspan=10, padx=5, pady=20, sticky='w')

        tk.Label(root, text=f"Computer average turn time: ", bg=bg_color, fg=fg_color).grid(row=7, column=0, columnspan=10, padx=5, pady=20, sticky='w')

        if chosenStarter == "User":
            isPlayersTurn = True
        else:
            isPlayersTurn = False
        print(f"Is it the players start {isPlayersTurn}")
        if chosenStarter == "Computer" and isPlayersTurn == False:
            state = {'chosenNumber': chosenNumber, 'aiPoints': aiPoints, 'humanPoints': humanPoints}
            edges_visited = ai_make_move(state, number_label)
            edgeLabel.config(text=f"Edges visited by {chosenAlgorithm}: {edges_visited}")

    else:
        messagebox.showinfo("Selection Incomplete", "Please make all selections before starting the game.")


def ai_make_move(state, number_label):
    # Šeit tiek atzīmēti visi lielumi kas tiks izmantoti šajā funkcijā, un to vērtības ir iespējams mainīt globāli
    global chosenNumber, isPlayersTurn, humanPoints, aiPoints, bestDivisor
    if gameOver() == True:
        endGameScreen()
    # Example usage of the minimax function from Huristic2.py
    if chosenAlgorithm == "Minimax":
        # Expected to return vislabāko vērtējumu for AI, the move leading to that score, cik virsotnes apmeklētas, labākais dalītājs
        score, best_move, edges_visited, bestDivisor = minimax(state, 0, True)  # Current state, dziļums 0, is MaximizingPlayer
        if best_move is not None:
            # Update the variables based on the best possible
            chosenNumber = best_move
            scoreUpdate(state,bestDivisor)
            isPlayersTurn = True
            HumanNextPoints = humanPoints
            HumanNextPoints += state['chosenNumber'] % chosenNumber  
            state['humanPoints'] = HumanNextPoints
            print(f"AI chooses {chosenNumber} (divided by {bestDivisor})")  # Print the chosen number and divisor
            print(f"Number of edges visited: {edges_visited}")
            # Update the label displaying the chosen number
            number_label.config(text=chosenNumber)
            scoreLabel()
            if gameOver() == True:
                endGameScreen()
            return edges_visited  # Return the number of edges visited
    else:
        print("Alpha Beta is not yet implemented")
        #isPlayersTurn = True
        #scoreLabel()




def endGameScreen(): # Call this when game has ended add winner in function
    clearWidgets()
    winner = WhoWins()

    endLabel = tk.Label(root, text="Game Over!", bg=bg_color, fg=fg_color)
    endLabel.grid(row=0, column=0, columnspan=10, padx=5, pady=10, sticky='w')

    winnerLabel = tk.Label(root, text=f"Winner: {winner}", bg=bg_color, fg=fg_color)
    winnerLabel.grid(row=1, column=0, columnspan=10, padx=5, pady=10, sticky='w')

    global userWins, computerWins
    if winner == "User":
        userWins += 1
    if winner == "Computer":
        computerWins += 1
    
    scoreLabel()

    pointsLabel = tk.Label(root, text=f"-------Games won-------", bg=bg_color, fg=fg_color)
    pointsLabel.grid(row=4, column=0, columnspan=10, padx=5, pady=5, sticky='w')

    userWinsLabel = tk.Label(root, text=f"User: {userWins}", bg=bg_color, fg=fg_color)
    userWinsLabel.grid(row=5, column=0, columnspan=1, padx=5, pady=5, sticky='w')

    computerWinsLabel = tk.Label(root, text=f"Computer: {computerWins}", bg=bg_color, fg=fg_color)
    computerWinsLabel.grid(row=5, column=1, columnspan=1, padx=5, pady=5, sticky='w')

    newGameButton = tk.Button(root, text="New Game", bg=bg_color, fg=fg_color, command=startNewGame)
    newGameButton.grid(row=6, column=0, columnspan=2, padx=10, pady=5, sticky='w')

    quitButton = tk.Button(root, text="Quit", bg=bg_color, fg=fg_color, command=quitGame)
    quitButton.grid(row=6, column=2, columnspan=2, padx=5, pady=5, sticky='w')


startGameScreen()

root.mainloop()
