from art import logo
import random



play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
print(logo)

if play == "y":

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    player_cards = [random.choice(cards), random.choice(cards)]
    computer_cards = [random.choice(cards), random.choice(cards)]

    player_score = sum(player_cards)
    computer_score = sum(computer_cards)

    print(f"Your cards: {player_cards}, current score: {player_score}")
    print(f"Computer's first card: {computer_cards[0]}")


    should_continue = True
    while should_continue:
        another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if another_card == "y":
            player_cards.append(random.choice(cards))
            player_score = sum(player_cards)


            if 11 in player_cards and player_score > 21:
                player_cards[player_cards.index(11)] = 1
                player_score = sum(player_cards)

            print(f"Your cards: {player_cards}, current score: {player_score}")

            if player_score > 21:
                should_continue = False
        else:
            should_continue = False


    while computer_score < 17:
        computer_cards.append(random.choice(cards))
        computer_score = sum(computer_cards)

        if 11 in computer_cards and computer_score > 21:
            computer_cards[computer_cards.index(11)] = 1
            computer_score = sum(computer_cards)


    print(f"\nYour final hand: {player_cards}, final score: {player_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")

    if player_score > 21:
        print("You went over. You lose 😭")
    elif computer_score > 21:
        print("Computer went over. You win 😁")
    elif player_score > computer_score:
        print("You win 😎")
    elif player_score < computer_score:
        print("You lose 😤")
    else:
        print("It's a draw 🙃")
else:
    print("Maybe next time!")
















