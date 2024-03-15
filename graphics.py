import tkinter as tk
import random
from tkinter import messagebox
from tkinter import font as tkFont


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
isPlayersTurn = True


root = tk.Tk()
root.title("1. praktiskais darbs")
root.geometry("500x500")
root.config(bg=bg_color)
root.option_add("*background", bg_color)
root.option_add("*foreground", fg_color)


def randomNumbers():
    ## Generates 5 random numbers from 20K to 30K that devide by 12
    count = 0
    randomList = []

    while count < 5:
      ranNum = random.randint(20000, 30000)
      if ranNum % 12 == 0:
        randomList.append(ranNum)
        count += 1
    return randomList


def gameOver():
       #game ends when the selected number is bellow or the same as 10
       #game ends if there are no more legal moves left
    if chosenNumber <= 10:
        if isPlayersTurn:
            humanPoints += bankPoints
        else:
            aiPoints += aiPoints 
        return True 
    return False


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
    #Select either User or Computer to start the gameand  call update the list
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
    # Reset any game-related variables and start a new game
    # For example:
    global humanPoints, aiPoints, bankPoints, isPlayersTurn
    humanPoints = 0
    aiPoints = 0
    bankPoints = 0
    isPlayersTurn = True


def quitGame():
    root.destroy()


def startGameScreen(): # 1. screen Choose parameters for the game
    global starterButtons 
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

def gameScreen(): # 2. screen 
    global chosenStarter, chosenNumber, chosenAlgorithm, humanPoints, aiPoints
    # Checks if all the buttons have been pressed for starting the game
    if chosenStarter and chosenNumber and chosenAlgorithm: 
        clearWidgets()  # Clear the window

        largeFont = tkFont.Font(size=24)  

        tk.Label(root, text=f"Algorithm: {chosenAlgorithm}", bg=bg_color, fg=fg_color).grid(row=0, column=0, columnspan=2, padx=5, pady=(20, 0), sticky='w')
        tk.Label(root, text=f"Starter: {chosenStarter}", bg=bg_color, fg=fg_color).grid(row=1, column=0, columnspan=2, padx=5, pady=(10, 20), sticky='w')

        # For the chosen number, ensure it's centered if desired by adjusting columnspan and sticky options
        tk.Label(root, text=f"{chosenNumber}", bg=bg_color, fg=fg_color, font=largeFont).grid(row=2, column=0, columnspan=2, padx=5, pady=20, sticky='w')
        
        tk.Label(root, text=f"User points: {humanPoints}", bg=bg_color, fg=fg_color).grid(row=3, column=0, columnspan=2, padx=5, pady=20, sticky='w')
        tk.Label(root, text=f"Computer points: {aiPoints}", bg=bg_color, fg=fg_color).grid(row=3, column=2, columnspan=2, padx=5, pady=20, sticky='w')
        
        # TODO: Display game state table moves of user and PC (Number, divider, player)
        
        divider2 = tk.Button(root, text="2", bg=bg_color, fg=fg_color)
        divider2.grid(row=4, column=0, columnspan=1, padx=5, pady=5)

        divider3 = tk.Button(root, text="3", bg=bg_color, fg=fg_color)
        divider3.grid(row=4, column=1, columnspan=1, padx=5, pady=5)

        divider4 = tk.Button(root, text="4", bg=bg_color, fg=fg_color)
        divider4.grid(row=4, column=2, columnspan=1, padx=5, pady=5)

        tk.Label(root, text=f"Games won User: ", bg=bg_color, fg=fg_color).grid(row=5, column=0, columnspan=2, padx=5, pady=20, sticky='w')
        tk.Label(root, text=f"Computer: ", bg=bg_color, fg=fg_color).grid(row=5, column=2, columnspan=2, padx=5, pady=20, sticky='w')

        tk.Label(root, text=f"Computer visited edges: ", bg=bg_color, fg=fg_color).grid(row=6, column=0, columnspan=2, padx=5, pady=20, sticky='w')
        tk.Label(root, text=f"Computer average turn time: ", bg=bg_color, fg=fg_color).grid(row=7, column=0, columnspan=2, padx=5, pady=20, sticky='w')

    else:
        messagebox.showinfo("Selection Incomplete", "Please make all selections before starting the game.")


def endGameScreen(): # 3. screen <-- Call this after the game has ended
    clearWidgets()
    endLabel = tk.Label(root, text="Game Over!", bg=bg_color, fg=fg_color)
    endLabel.grid(row=0, column=0, columnspan=2, padx=5, pady=10)

    newGameButton = tk.Button(root, text="New Game", bg=bg_color, fg=fg_color, command=startNewGame)
    newGameButton.grid(row=1, column=0, padx=5, pady=5)

    quitButton = tk.Button(root, text="Quit", bg=bg_color, fg=fg_color, command=quitGame)
    quitButton.grid(row=1, column=1, padx=5, pady=5)



startGameScreen()

root.mainloop()
