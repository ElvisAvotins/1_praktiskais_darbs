def get_children(state, isMaximizingPlayer):
    current_number = state['chosenNumber']
    possible_divisors = [2, 3, 4]

    # šajā sarakstā tiek glabāts šādi
    # {{'chosenNumber': XXXX, 'aiPoints': XXX, 'humanPonts': XXX},
    #  {'chosenNumber': XXXX, 'aiPoints': XXX, 'humanPonts': XXX}}
    children = [] # empty list

    # Aprēķinam kuri cipari var doties tālāk, un tiek ievitots jauns ieraksts ar new_number, aiPoints un humanPoints
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


# Pārbauda vai spele begsies vai ne un nosaka vai vinē vai  zaudē 
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
    # Atgriest None, ja nav sasniegts Terminal state
    return None





def minimax(state, depth, isMaximizingPlayer, edges_visited=0):
    #Pårbauda vai spele var turpinåties vai ir end of the game
    terminal_value = check_terminal(state)

    # Ja ir sasniegts 'Win' 'Lose' 'Draw' tad tiek izvadits
    # terminal_value -> '1' '-1' '0'
    # chosenNumber -> What number did the game end at
    # edges_visited -> Cik virsotnes tika apmekletas, to find the best path
    # First None -> What specific move is best
    # Second None -> Divisor used for path
    if terminal_value is not None:
        # Print the terminal value and the current chosen number at the terminal state
        print(f"Terminal Value: {terminal_value}, Chosen Number at Terminal: {state['chosenNumber']}")
        return terminal_value, None, edges_visited, None  # Return score, no move, edges visited, and None for divisor

    # Pie dziļuma 3 izsaukt huristic funkciju, lai aprēķinātu virsotņu labklājību
    # Returns aprēķināto virsotņu heiristisko vērtējumu
    # The best move is not returned
    # Edges visited for atskaite
    # Divisor None, because we are not divising yet
    if depth == 3:  
        heuristic_value = heuristic_evaluation(state)
        return heuristic_value, None, edges_visited, None  # Return heuristic score, no move, edges visited, and None for divisor


    # Ja ir Maximizing player (kas mūsu gadijumā ir AI)
    # sāk meklēšanu no -inf, sākot no mazākās automātiskoi nozīmē, ka katrs nākamais rezultāts būs labāks (Algorithm is ready to evaluate any posibilities)
    # bestMove sākam no null, jo nezinam kas mums būs priekšā
    # bestDevisor ari vel nav
    if isMaximizingPlayer:
        maxEval = float('-inf')
        bestMove = None
        bestDivisor = None  # Initialize the best divisor

        # šei pakāpeniski ejam cauri katram bērnam (pēctecim) no ieprieks uzrakstītā get_children funkcijas
        # eval -> svars katram bērnam(pēctecim)
        # _ -> ignored value, we dont need it at the moment
        # edges_visited -> cik virsotnes apmeklētas
        # divisor -> ar ko dalam
        for child in get_children(state, True):
            # Pārejam uz minimizējošā spēlētāja pēdām, lai varētu imitēt ping-pong gājienu
            # lai aprēķinātu, kāds būtu laākais atbildes gājiens no pretinieka
            eval, _, edges_visited, divisor = minimax(child, depth + 1, False, edges_visited + 1)

            # Gett to the best move
            # pārbaudam vai aprēķinātais svars eval ir lielāks par lielāko svaru bērnam (pēctecim)
            # Atceramies ka ieprieskš maxEval uzstādijām uz -Inf, kas nozīmē ka piemais pārbaudītais bērns būs lielāks
            # Ja ir True tad tiek updated maxeval
            if eval > maxEval:
                maxEval = eval
                # Šis pieliek labāko ceļu pie esošā bērna (Pēcteča)
                bestMove = child['chosenNumber']  
                # Šis noskaidro ar kuru dalītāju var nonākt pie svara
                bestDivisor = state['chosenNumber'] // child['chosenNumber']  # Update the best divisor
        # Returns labāko svaru, labāko ceļu, cik virsotnes apmeklētas, labāko dalītāju   
        return maxEval, bestMove, edges_visited, bestDivisor  
    else:

        # Taspats tiek darīts šeit, lai varētu imitēt min spēlētāja gājienus
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


def alphaBeta(state, depth, isMaximizingPlayer, edges_visited, alpha, beta):
    terminal_value = check_terminal(state)

    if terminal_value is not None:
        print(f"Terminal Value: {terminal_value}, Chosen Number at Terminal: {state['chosenNumber']}")
        return terminal_value, None, edges_visited, None

    if depth == 3:
        heuristic_value = heuristic_evaluation(state, depth)
        return heuristic_value, None, edges_visited, None

    if isMaximizingPlayer:
        maxEval = float('-inf')
        bestMove = None
        bestDivisor = None

        for child in get_children(state, True):
            eval, _, edges_visited, _ = alphaBeta(child, depth + 1,  False, edges_visited + 1, alpha, beta)
            maxEval = max(maxEval, eval)
            if maxEval >= beta:
                return maxEval, bestMove, edges_visited, bestDivisor
            if maxEval > alpha:
                alpha = maxEval
                bestMove = child['chosenNumber']
                bestDivisor = state['chosenNumber'] // child['chosenNumber']
        return maxEval, bestMove, edges_visited, bestDivisor
    else:
        minEval = float('inf')
        bestMove = None
        bestDivisor = None

        for child in get_children(state, False):
            eval, _, edges_visited, _ = alphaBeta(child, depth + 1,  True, edges_visited + 1, alpha, beta)
            minEval = min(minEval, eval)
            if minEval <= alpha:
                return minEval, bestMove, edges_visited, bestDivisor
            if minEval < beta:
                beta = minEval
                bestMove = child['chosenNumber']
                bestDivisor = state['chosenNumber'] // child['chosenNumber']
        return minEval, bestMove, edges_visited, bestDivisor

    
def heuristic_evaluation(state, depth=None):
    aiPoints = state.get('aiPoints', 0)
    humanPoints = state.get('humanPoints', 0)
    chosenNumber = state.get('chosenNumber', None)
    
    # Tākā ai punkti lai tas varētu maksimizēt savu gāājienu tas tiek reizināts ar lielāku skaitli
    score_diff = 10 * aiPoints - 1 * humanPoints  
    
    print(f"Debug: Depth {depth}, Number: {chosenNumber}, Heuristic Value: {score_diff}, AI Score: {aiPoints}, Human Score: {humanPoints}")
    
    return score_diff
    

