import random

card_suit = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
cards_list = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
deck = [(card, suit) for card in cards_list for suit in card_suit]
money = 5000

def card_value(card):
    face = card[0]

    if face in ['Jack', 'Queen', 'King']:
        return 10
    elif face == 'Ace':
        return 11
    else:
        return int(face)

def hand_total(hand):
    total = 0
    aces = 0

    for card in hand:
        val = card_value(card)
        total += val
        if card[0] == 'Ace':
            aces += 1

    # Ajuster la valeur des As si total dépasse 21
    while total > 21 and aces:
        total -= 10  # convertit un As de 11 à 1
        aces -= 1

    return total

def bet(money):
    bet_options = {
        1: 1000,
        2: 2500,
        3: 5000,
        4: 10000,
        5: money  # All in
    }

    print("""
    BETS
    (1) Bet 1000
    (2) Bet 2500
    (3) Bet 5000
    (4) Bet 10000
    (5) All in!
    """)

    while True:
        try:
            bet_choice = int(input("Enter the amount of bet you want: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            continue

        if bet_choice not in bet_options:
            print("Invalid choice. Please select 1-5.")
            continue

        selected_bet = bet_options[bet_choice]

        if selected_bet > money:
            print("You don't have enough money for that bet!")
        else:
            return selected_bet



def play_blackjack(money, deck):
    #player bet
    print("Welcome to Blackjack!\n How much do you want to bet? ")
    player_bet = bet(money)
    print("Your bet is: ", player_bet)

    #game setup
    random.shuffle(deck)
    player_card = [deck.pop(), deck.pop()]
    dealer_card = [deck.pop(), deck.pop()]
    original_player_card = [player_card[0], player_card[1]]

    # blackjack
    first = original_player_card[0][0]
    second = original_player_card[1][0]
    if (first == 'Ace' and second in ['10', 'Jack', 'Queen', 'King']) or \
            (second == 'Ace' and first in ['10', 'Jack', 'Queen', 'King']):
        print("Cards Player Has:", player_card)
        print("Score Of The Player: 21")
        print("Player Wins, BlackJack!")
        money += (player_bet * 1.5)
        print("Your funds are at: ", money)
        return money

    while True:
        player_score = hand_total(player_card)
        dealer_score = hand_total(dealer_card)
        print("Cards Player Has:", player_card)
        print("Score Of The Player:", player_score)
        print("\n")
        dealer_first_card = dealer_card[0]
        print("The dealer starts with a ", dealer_first_card)
        print("\n")
        choice = input("What are you doing, player? [hit] to request another card, [stand] to stop, [double] to double your bet amount: ").strip().lower()
        if choice == 'hit' or choice == 'h':
            player_card.append(deck.pop())
        elif choice == 'stand' or choice == 's':
            break
        elif choice == 'double' or choice == 'd':
            if money >= player_bet * 2:
                player_bet *= 2
                player_card.append(deck.pop())
                break
            else:
                print("Not enough funds to double.")
                continue
        else:
            print("Invalid choice")
            continue

        # bust player
        if hand_total(player_card) > 21:
            print(f"Player Cards {player_card} with a score of {player_score}")
            print(f"Dealer Cards {dealer_card} with a score of {dealer_score}")
            print("Dealer wins - Player Busted!")

            money -= player_bet
            print("Your funds are at: ", money)
            return money

    if hand_total(player_card) <= 21:
        # blackjack
        if dealer_score == 21:
            print("Dealer wins - Blackjack!")
            # if choice == 'double' or choice == 'd':
            #     money -= (player_bet * 2)
            #     print("Your funds are at: ", money)
            #     return money
            money -= player_bet
            print("Your funds are at: ", money)
            return money

        while (dealer_score < 17):
            dealer_card.append(deck.pop())
            dealer_score = hand_total(dealer_card)

        print("Cards Dealer Has:", dealer_card)
        print("Score Of The Dealer:", dealer_score)
        print("\n")

        print(f"Player Cards {player_card} with a score of {player_score}")
        print(f"Dealer Cards {dealer_card} with a score of {dealer_score}")
        if dealer_score > 21:
            print("Dealer Bust! \t Player Wins!")
            # if choice == 'double' or choice == 'd':
            #     money += (player_bet * 2)
            #     return money
            money += player_bet

        elif player_score > dealer_score:
            print("Player Wins!")
            # if choice == 'double' or choice == 'd':
            #     money += (player_bet * 2)
            #     return money
            money += player_bet

        elif dealer_score > player_score:
            print("Dealer Wins!")
            # if choice == 'double' or choice == 'd':
            #     money -= (player_bet * 2)
            #     return money
            money -= player_bet

        else:
            print("Push!")

        print("Your funds are at: ", money)
        return money
    else:

        money -= player_bet
        return money

while True:
    money = play_blackjack(money, deck)
    print(f"You have {money}$")

    if money <= 0:
        print("You're out of money! Game over.")
        break
    again = input("Play again? (yes/no): ").strip().lower()
    if again != 'yes':
        print("Thanks for playing!")
        break





