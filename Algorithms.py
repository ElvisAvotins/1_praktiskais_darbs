def get_children(state, isMaximizingPlayer):
    current_number = state['chosenNumber']
    possible_divisors = [2, 3, 4]
    children = []

    for divisor in possible_divisors:
        if current_number % divisor == 0:
            new_number = current_number // divisor
            child_state = state.copy()
            child_state['chosenNumber'] = new_number
            
            # Determine if the result is even or odd to update scores accordingly
            score_change = -1 if new_number % 2 == 0 else 1

            if isMaximizingPlayer:  # AI's move
                child_state['aiPoints'] += score_change
            else:  # Human's move
                child_state['humanPoints'] += score_change

            children.append(child_state)

    return children


def check_terminal(state):
    chosenNumber = state.get('chosenNumber')
    aiPoints = state.get('aiPoints', 0)
    humanPoints = state.get('humanPoints', 0)
    bankPoints = state.get('bankPoints', 0)
    
    # If the number is <= 10 or cannot be divided by 2, 3, or 4
    if chosenNumber <= 10 or all(chosenNumber % d != 0 for d in [2, 3, 4]):
        # Distribute bank points to the last player who made a move
        finalAiPoints = aiPoints + (bankPoints if not state.get('isPlayersTurn') else 0)
        finalHumanPoints = humanPoints + (bankPoints if state.get('isPlayersTurn') else 0)

        # Determine the winner
        if finalAiPoints > finalHumanPoints:
            print(f"Game Over! AI Wins! Final Scores - AI: {finalAiPoints}, Human: {finalHumanPoints}")
            return 1
        elif finalHumanPoints > finalAiPoints:
            print(f"Game Over! Human Wins! Final Scores - AI: {finalAiPoints}, Human: {finalHumanPoints}")
            return -1
        else:
            print(f"Game Over! It's a Draw! Final Scores - AI: {finalAiPoints}, Human: {finalHumanPoints}")
            return 0
    return None






def minimax(state, depth, isMaximizingPlayer, edges_visited=0):
    terminal_value = check_terminal(state)
    if terminal_value is not None:
        # Print the terminal value and the current chosen number at the terminal state
        print(f"Terminal Value: {terminal_value}, Chosen Number at Terminal: {state['chosenNumber']}")
        return terminal_value, None, edges_visited, None  # Return score, no move, edges visited, and None for divisor
    
    if depth == float('inf'):  
        heuristic_value = heuristic_evaluation(state)
        return heuristic_value, None, edges_visited, None  # Return heuristic score, no move, edges visited, and None for divisor

    if isMaximizingPlayer:
        maxEval = float('-inf')
        bestMove = None
        bestDivisor = None  # Initialize the best divisor
        for child in get_children(state, True):
            eval, _, edges_visited, divisor = minimax(child, depth + 1, False, edges_visited + 1)
            if eval > maxEval:
                maxEval = eval
                bestMove = child['chosenNumber']  # Assuming this represents the move
                bestDivisor = state['chosenNumber'] // child['chosenNumber']  # Update the best divisor
        return maxEval, bestMove, edges_visited, bestDivisor  # Return the best divisor along with other values
    else:
        minEval = float('inf')
        bestMove = None
        bestDivisor = None  # Initialize the best divisor
        for child in get_children(state, False):
            eval, _, edges_visited, divisor = minimax(child, depth + 1, True, edges_visited + 1)
            if eval < minEval:
                minEval = eval
                bestMove = child['chosenNumber']  # Assuming this represents the move
                bestDivisor = state['chosenNumber'] // child['chosenNumber']  # Update the best divisor
        return minEval, bestMove, edges_visited, bestDivisor  # Return the best divisor along with other values



    
def heuristic_evaluation(state, depth=None):
    aiPoints = state.get('aiPoints', 0)
    humanPoints = state.get('humanPoints', 0)
    chosenNumber = state.get('chosenNumber', None)
    
    # Example scoring logic
    score_diff = 10 * aiPoints - 1 * humanPoints  

    # Ensure debugging output is shown for nodes at depth 3
    
    print(f"Debug: Depth {depth}, Number: {chosenNumber}, Heuristic Value: {score_diff}, AI Score: {aiPoints}, Human Score: {humanPoints}")
    
    return score_diff
    

