import random

suits = ["Hearts","Diamonds","Spades","Clubs"]
ranks = ["Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King","Ace"]
values = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9,
          "Ten": 10, "Jack": 10, "Queen": 10, "King": 10, "Ace": 11, }
playing = True


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return "The deck has " + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()

# test_deck = Deck()
# print(test_deck)

class Hand():

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        ## card passed in
        ## from Deck.deal() -> single card(suit,rank)
        self.cards.append(card)
        self.value += values[card.rank]

        # track aces
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        # If the total value > 21 and still have a ace
        # then treat Ace to be 1 instead of 11
        # self.aces will return True when value is > 0
        if self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

# Test Code So Far
#test_deck = Deck()
#test_deck.shuffle()

# Player
#test_player = Hand()
# Deal 1 card from the deck Card(suit,rank)
#pulled_card = test_deck.deal()
#print(pulled_card)
#test_player.add_card(pulled_card)
#print(test_player.value)

# Add one more card
#test_player.add_card(test_deck.deal())
#print(test_player.value)

# remaining cards left in the deck
#print(len(test_deck.deck))

#print(test_player.value)


class Chips:

    def __init__(self,total=100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips):

    while True:

        try:
            chips.bet = int(input(" How may chips would you like to bet ? "))
        except:
            print("Sorry please provide a number")
        else:
            if chips.bet > chips.total:
                print("yo don't have enough chips! you have : {}".format(chips.total))
            else:
                break


def hit(deck, hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing  # to control an upcoming while loop

    while True:
        x = input(" Hit or Stand ? Enter h or s ? ")

        if x[0].lower() == 'h':
            hit(deck, hand)
        elif x[0].lower() == 's':
            print("Player stands, it's Dealer's Turn")
            playing = False
        else:
            print("Sorry, I did not understand that, please enter h or s")
            continue
        break



def show_some(player, dealer):
    print("DEALER's HAND")
    print("One card hidden")
    print(dealer.cards[1])
    print("\n")
    print("PLAYER's HAND")
    for card in player.cards:
        print(card)

def show_all(player, dealer):
    print("DEALER's HAND")
    for card in dealer.cards:
        print(card)
    print("\n")
    print("PLAYER's HAND")
    for card in player.cards:
        print(card)


def player_busts(player,dealer,chips):
    print("BUST PLAYER!!")
    chips.lose_bet()


def player_wins(player,dealer,chips):
    print("PLAYER WINS!!!")
    chips.win_bet()


def dealer_busts(player,dealer,chips):
    print("PLAYER WINS!!! DEALER BUSTED")
    chips.win_bet()


def dealer_wins(player,dealer,chips):
    print("DEALER WINS!!")
    chips.lose_bet()


def push(player,dealer):
    print("Player and dealer Tie!  PUSH")


#####################

while True:

    print ("Welcome to BLACKJACK !!!!")

# create and shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

# setup Player's chips
    player_chips = Chips()

#  prompt the player for the bet
    take_bet(player_chips)

# show cards ( but keep one dealer card hidden)
    show_some(player_hand, dealer_hand)

#   recall this flag from hit_or_stand function
#   this flag could also have been passed as a parameter to the function instead of a global variable
    while playing:
        # promopt for player to hit or stand
        hit_or_stand(deck, player_hand)

        # show cards (but keep one dealer card hidden)
        show_some(player_hand, dealer_hand)

        # If Player's hand exceeds 21, player Busted and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break

        # If player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.value <= 21:

        while dealer_hand.value < 17:
            hit(deck,dealer_hand)

        # show all cards
        show_all(player_hand,dealer_hand)

        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        else:
            push(player_hand,dealer_hand)

# Inform player of the remaining chips
    print("\n player's total chips are at {}".format(player_chips.total))

# Ask to Play again
    new_game = input("Do you want to play again - y or n ?")

    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("Thank you for playing!")
        break




