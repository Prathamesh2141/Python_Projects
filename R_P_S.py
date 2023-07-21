from random import randint


def get_computer_move():
    moves = ["👊", "📃", "✂️"]
    return moves[randint(0, 2)]


def determine_winner(player_move, computer_move):
    if player_move == computer_move:
        return "Tie"
    elif player_move == "👊":
        return "Player" if computer_move == "✂️" else "Computer"
    elif player_move == "📃":
        return "Player" if computer_move == "👊" else "Computer"
    elif player_move == "✂️":
        return "Player" if computer_move == "📃" else "Computer"


def print_results(player_move, computer_move, result):
    print(f"Player chose {player_move}.")
    print(f"Computer chose {computer_move}.")
    if result == "Tie":
        print("It's a Tie!")
    else:
        print(f"{result} wins!")


def print_emojis():
    print("Choose your move:")
    print("👊 for Rock")
    print("📃 for Paper")
    print("✂️ for Scissors")


def main():
    print("Welcome to Rock, Paper, Scissors Game!")
    print("Enter 'exit' to quit the game.")

    chances = 5
    current_chance = 1
    player_wins = 0
    computer_wins = 0

    while current_chance <= chances:
        print_emojis()
        player_move = input(f"\nChance {current_chance}/{chances}. Your move: ")

        if player_move == "exit":
            print("Game Over. Exiting...")
            break

        if player_move not in ["👊", "📃", "✂️"]:
            print("Invalid input. Please enter a valid emoji.")
            continue

        computer_move = get_computer_move()
        result = determine_winner(player_move, computer_move)

        print_results(player_move, computer_move, result)

        if result == "Player":
            player_wins += 1
        elif result == "Computer":
            computer_wins += 1

        current_chance += 1

    print("\nGame Summary:")
    print(f"Player wins: {player_wins}")
    print(f"Computer wins: {computer_wins}")
    print("Thanks for playing!")


if __name__ == "__main__":
    main()
