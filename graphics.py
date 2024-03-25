import tkinter as tk
import random
from tkinter import messagebox
from tkinter import font as tkFont
from Huristic2 import *

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
    count = 0
    randomlist = []

    while count < 5:
        num = random.randint(20000, 30000)
        if num % 12 == 0:
            randomlist.append(num)
            count += 1
    return randomlist


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

def gameScreen(): # 2. screen 
  global chosenStarter, chosenNumber, chosenAlgorithm, humanPoints, aiPoints
  # Checks if all the buttons have been pressed for starting the game
  if chosenStarter and chosenNumber and chosenAlgorithm: 
      clearWidgets()  # Clear the window

      largeFont = tkFont.Font(size=24)  

      tk.Label(root, text=f"Algorithm: {chosenAlgorithm}", bg=bg_color, fg=fg_color).grid(row=0, column=0, columnspan=2, padx=5, pady=(20, 0), sticky='w')
      tk.Label(root, text=f"Starter: {chosenStarter}", bg=bg_color, fg=fg_color).grid(row=1, column=0, columnspan=2, padx=5, pady=(10, 20), sticky='w')

      # For the chosen number, ensure it's centered if desired by adjusting columnspan and sticky options
      number_label = tk.Label(root, text=f"{chosenNumber}", bg=bg_color, fg=fg_color, font=largeFont)
      number_label.grid(row=2, column=0, columnspan=2, padx=5, pady=20, sticky='w')

      tk.Label(root, text=f"User points: {humanPoints}", bg=bg_color, fg=fg_color).grid(row=3, column=0, columnspan=2, padx=5, pady=20, sticky='w')
      tk.Label(root, text=f"Computer points: {aiPoints}", bg=bg_color, fg=fg_color).grid(row=3, column=2, columnspan=2, padx=5, pady=20, sticky='w')

      # TODO: Display game state table moves of user and PC (Number, divider, player)

      def divide_number(divider):
        global chosenNumber, isPlayersTurn, humanPoints, aiPoints
        if chosenNumber % divider != 0:
            messagebox.showerror("Error", "Division result is not a whole number!")
        else:
            chosenNumber //= divider
            number_label.config(text=chosenNumber)

            isPlayersTurn = False  # Update the turn to AI's turn
        state = {'chosenNumber': chosenNumber, 'aiPoints': aiPoints, 'humanPoints': humanPoints}
        edges_visited = ai_make_move(state, number_label)
        edge_label.config(text=f"Edges visited by {chosenAlgorithm}: {edges_visited}")




            
      divider2 = tk.Button(root, text="2", bg=bg_color, fg=fg_color, command=lambda: divide_number(2))
      #divider2 = tk.Button(root, text="2", bg=bg_color, fg=fg_color, command=lambda: divide_number(2, edge_label))

      divider2.grid(row=4, column=0, columnspan=1, padx=5, pady=5)

      divider3 = tk.Button(root, text="3", bg=bg_color, fg=fg_color, command=lambda: divide_number(3))
      divider3.grid(row=4, column=1, columnspan=1, padx=5, pady=5)

      divider4 = tk.Button(root, text="4", bg=bg_color, fg=fg_color, command=lambda: divide_number(4))
      divider4.grid(row=4, column=2, columnspan=1, padx=5, pady=5)

      tk.Label(root, text=f"Games won User: ", bg=bg_color, fg=fg_color).grid(row=5, column=0, columnspan=2, padx=5, pady=20, sticky='w')
      tk.Label(root, text=f"Computer: ", bg=bg_color, fg=fg_color).grid(row=5, column=2, columnspan=2, padx=5, pady=20, sticky='w')

      edge_label = tk.Label(root, text=f"Computer visited edges: ", bg=bg_color, fg=fg_color)
      edge_label.grid(row=6, column=0, columnspan=2, padx=5, pady=20, sticky='w')

      tk.Label(root, text=f"Computer average turn time: ", bg=bg_color, fg=fg_color).grid(row=7, column=0, columnspan=2, padx=5, pady=20, sticky='w')

  else:
      messagebox.showinfo("Selection Incomplete", "Please make all selections before starting the game.")


def ai_make_move(state, number_label):
    global chosenNumber, isPlayersTurn, humanPoints, aiPoints
    # Example usage of the minimax function from Huristic2.py
    if chosenAlgorithm == "Minimax":
        score, best_move = minimax(state, 0, True)
        if best_move is not None:
            chosenNumber = best_move
            isPlayersTurn = True
            humanPoints += state['chosenNumber'] % chosenNumber  # Update human points based on the move
            state['humanPoints'] = humanPoints
            print(f"AI chooses {chosenNumber}")
            # Update the label displaying the chosen number
            number_label.config(text=chosenNumber)
            if gameOver():
                endGameScreen()
    else:
        print("Alpha Beta is not yet implemented")

def ai_make_move(state, number_label):
    global chosenNumber, isPlayersTurn, humanPoints, aiPoints, bestDivisor
    # Example usage of the minimax function from Huristic2.py
    if chosenAlgorithm == "Minimax":
        score, best_move, edges_visited, bestDivisor = minimax(state, 0, True)  # Modify minimax to return edges_visited and divisor
        if best_move is not None:
            chosenNumber = best_move
            isPlayersTurn = True
            humanPoints += state['chosenNumber'] % chosenNumber  # Update human points based on the move
            state['humanPoints'] = humanPoints
            print(f"AI chooses {chosenNumber} (divided by {bestDivisor})")  # Print the chosen number and divisor
            print(f"Number of edges visited: {edges_visited}")
            # Update the label displaying the chosen number
            number_label.config(text=chosenNumber)
            if gameOver():
                endGameScreen()
            return edges_visited  # Return the number of edges visited
    else:
        print("Alpha Beta is not yet implemented")



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
