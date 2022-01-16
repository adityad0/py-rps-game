import random

# Rock > Scissors
# Paper > Rock
# Scissors > Paper

def make_choice():
    choice = random.randint(1, 3)
    return choice

def get_user_choice():
    users_choice = input("Enter 1 for Rock, 2 for Paper, 3 for Scissors: ")
    try:
        users_choice = int(users_choice)
    except ValueError:
        print("Your choice must be a number.")
        quit()
    if users_choice < 1 or users_choice > 3:
        print("Option must be between 1 and 3.")
        print()
        get_number_of_rounds()
    return users_choice

def get_number_of_rounds():
    num_rounds = input("Enter the number of rounds you wish to play: ")
    try:
        num_rounds = int(num_rounds)
    except ValueError:
        print("The number of rounds must be a number.")
        print("Default value of 5 rounds is set.")
        print()
        return 5
    if num_rounds < 1:
        print("Number of rounds must be more than 0.")
        print("Default value of 5 rounds is set.")
        print()
        return 5

def play_round(computers_choice, users_choice):
    if computers_choice == 1:
        c_choice = "Rock"
    elif computers_choice == 2:
        c_choice = "Paper"
    else:
        c_choice = "Scissors"
    if computers_choice == users_choice:
        round_winner = 'tie'
    else:
        if computers_choice == 1 and users_choice == 3:
            round_winner = 'comp'
        elif computers_choice == 2 and users_choice == 1:
            round_winner = 'comp'
        elif computers_choice == 3 and users_choice == 2:
            round_winner = 'comp'
        else:
            round_winner = 'user'
    return round_winner, c_choice


def main():
    print("Rock paper scissors game")
    print()

    num_rounds = get_number_of_rounds()
    print()

    user_score = 0
    comp_score = 0

    for rounds_count in range(0, num_rounds):
        computers_choice = make_choice()
        users_choice = get_user_choice()
        round_winner, c_choice = play_round(computers_choice, users_choice)
        if round_winner == 'comp':
            comp_score += 1
            print(f"Computer's choice: {c_choice}. Computer wins! Score: {user_score}-{comp_score}.")
            print()
        elif round_winner == 'user':
            user_score += 1
            print(f"Computer's choice: {c_choice}. You win! Score: {user_score}-{comp_score}.")
            print()
        else:
            print(f"Computer's choice is the same as the user's choice: {c_choice}. Score: {user_score}-{comp_score}.")
            print()
    
    if int(user_score) > int(comp_score):
        print(f"User wins! Score: {user_score}-{comp_score}")
    elif int(comp_score) > int(user_score):
        print(f"Computer wins! Score: {user_score}-{comp_score}")
    else:
        print(f"The result is a tie. Score: {user_score}-{comp_score}")

if __name__ == "__main__":
    main()