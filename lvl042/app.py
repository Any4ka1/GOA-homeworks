def rps(p1, p2):
    choices = ["rock", "paper", "scissors"]
    if p1 not in choices or p2 not in choices:
        return "Invalid input! Choose 'rock', 'paper', or 'scissors'."
    
    if p1 == p2:
        return "It's a tie!"
    elif (p1 == "rock" and p2 == "scissors") or \
         (p1 == "paper" and p2 == "rock") or \
         (p1 == "scissors" and p2 == "paper"):
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"