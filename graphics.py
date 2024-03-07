import tkinter as tk

# TODO: import functions from other files

bg_color = "#1e1e1e"
fg_color = "white"

root = tk.Tk()
root.title("1. praktiskais darbs")
root.geometry("500x500")
root.config(bg=bg_color)

root.option_add("*background", bg_color)
root.option_add("*foreground", fg_color)

def whoStarts():
    textWhoStarts = tk.Label(root, text="Choose who starts the game!")
    textWhoStarts.grid(row=0, column=0, columnspan=3, padx=5, pady=5)

    # TODO: Disable button when other is pressed
     
    user = tk.Button(root, text="User")
    user.grid(row=1, column=0, padx=5, pady=5)
    # TODO: add function to button

    computer = tk.Button(root, text="Computer")
    computer.grid(row=1, column=1, padx=5, pady=5)
    # TODO: add function to button

    # TODO: Disable buttons in further game state
whoStarts()

def algorhithmChoice():
    textAlgorithmChoice = tk.Label(root, text="Choose algorithm!")
    textAlgorithmChoice.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    # TODO: Disable button when other is pressed
     
    minimax = tk.Button(root, text="Minimax")
    minimax.grid(row=3, column=0, padx=5, pady=5)
    # TODO: add function to button

    alphaBeta = tk.Button(root, text="Alpha Beta")
    alphaBeta.grid(row=3, column=1, padx=5, pady=5)
    # TODO: add function to button

    # TODO: Disable buttons in further game state
algorhithmChoice()

    
def startingNumber():
    algorithmChoice = tk.Label(root, text="Choose algorithm!")

    # TODO: Add 5 generated starting number buttons
    pass

def displayGameState():
    # TODO: Display current game points user
    # TODO: Display current game points PC

    # TODO: Display game state table moves of user and PC (Number, divider, player)
    # TODO: Add 3 buttons with divisors (2, 3 or 4)
    # TODO: Update table after each divider press

    # TODO: Display games won by user
    # TODO: Display games won by PC

    # TODO: Display computers visited edges count
    # TODO: Computers avarage turn time
    pass

def endGame():
    # TODO: Displays the winner or draw
    # TODO: Add button New Game
    # TODO: Add button Quit game
    pass

root.mainloop()


