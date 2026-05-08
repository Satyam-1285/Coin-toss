import random

def coin_toss_game():
    print("--- Welcome to the Python Coin Toss! ---")
    
    # Define the possible outcomes
    outcomes = ["Heads", "Tails"]
    
    while True:
        # Get user input
        user_choice = input("\nPick Heads or Tails (or type 'quit' to exit): ").strip().capitalize()
        
        if user_choice == 'Quit':
            print("Thanks for playing! Goodbye.")
            break
            
        if user_choice not in outcomes:
            print("Invalid choice. Please type 'Heads' or 'Tails'.")
            continue
        
        # The computer "flips" the coin
        result = random.choice(outcomes)
        print(f"The coin lands on... {result}!")
        
        # Determine the winner
        if user_choice == result:
            print("🎉 You win!")
        else:
            print("😔 Better luck next time.")

if __name__ == "__main__":
    coin_toss_game()
