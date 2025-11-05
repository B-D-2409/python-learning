import random
from art import logo, vs
from game_data import data


def compare_followers(A_PLAYER, B_PLAYER):
    choice = input("Who has more followers? Type 'A' or 'B': ").upper()
    if choice == "A":
        return A_PLAYER
    else:
        return B_PLAYER


def compare_famous(A_PLAYER, B_PLAYER, score):
    chosen_player = compare_followers(A_PLAYER, B_PLAYER)

    if chosen_player == A_PLAYER:
        other_player = B_PLAYER
    else:
        other_player = A_PLAYER

    if chosen_player["follower_count"] > other_player["follower_count"]:
        score += 1
        print(f" You're right! Current score: {score}.")
        # Continue the game: A becomes B, B becomes new random
        A_PLAYER = B_PLAYER
        B_PLAYER = random.choice(data)
        while B_PLAYER == A_PLAYER:
            B_PLAYER = random.choice(data)
        return A_PLAYER, B_PLAYER, score, True
    else:
        print(f" Sorry, that's wrong. Final score: {score}")
        return A_PLAYER, B_PLAYER, score, False


def game():
    print(logo)
    score = 0
    A_PLAYER = random.choice(data)
    B_PLAYER = random.choice(data)
    while A_PLAYER == B_PLAYER:
        B_PLAYER = random.choice(data)

    continue_game = True
    while continue_game:
        print(f"\nCompare A: {A_PLAYER['name']}, {A_PLAYER['description']}, from {A_PLAYER['country']}")
        print(vs)
        print(f"Against B: {B_PLAYER['name']}, {B_PLAYER['description']}, from {B_PLAYER['country']}")

        A_PLAYER, B_PLAYER, score, continue_game = compare_famous(A_PLAYER, B_PLAYER, score)


game()
