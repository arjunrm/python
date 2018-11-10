# Spades/Clubs/Hearts/Diamonds
SUITS = (int('2660', 16), int('2663', 16), int('2665', 16), int('2666', 16))
RANKS = ('2', '3', '4', '5', '6', '7', '8', '9', 
    'J', 'Q', 'K', 'A')
VALUES = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 
    'J':10, 'Q':10, 'K':10, 'A':11}
PLAYERS = ['DEALER', 'PLAYER1']

import os
import random

def clear_screen():
    # Store output into any var
    # _ is used here as python shell always
    # stores the last output into _
    if os.name == 'nt':
        _ = os.system('cls')
    # This is for linux and mac os.name = 'posix'
    else:
        _ = os.system('clear')

class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = VALUES[rank]
        self.open = False
    
    def __repr__(self):
        card = f"{chr(self.suit)}{self.rank}" if self.open else "--"
        return card

class Deck():
    def __init__(self):
        self.cards = []
        for i in SUITS:
            for j in RANKS:
                self.cards.append(Card(i, j))
        random.shuffle(self.cards)

    def __str__(self):
        for i in self.cards: i.open = True
        cards = str(self.cards)
        for i in self.cards: i.open = False
        return cards

class Chips():
    def __init__(self, amount):
        self.total = amount
        self.bet = 0

    def win_bet(self, bet):
        self.total += (self.bet + bet)
    
    def loose_bet(self):
        self.bet = 0

    def place_bet(self, bet):
        loop = True
        while loop:
            try:
                bet = int(input("Enter the chips to bet: "))
                if(self.total > bet):
                    self.bet = bet
                    self.total -= bet
                else:
                    print("NOT ENOUGH CHIPS TO PLACE A BET !!!")
                    print("Total chips available: {}".format(self.total))
            except TypeError:
                print("Please enter the correct chips! Only integer is accepted.")
                continue
            else:
                loop = False

class Hand():
    def __init__(self, name, close_first_card = False):
        if type(name) != type(str):
            assert("Invalid name! Aborting Game!!")
        self.name = name
        self.cards = []
        self.close_first_card = close_first_card

    def __repr__(self):
        hand = self.name + '\'s Cards:\n'
        for card in self.cards:
            hand += str(card) + ' '
        hand += '\n\n'
        return hand
    
    def add_card(self, card):
        # keep the first card closed if close_first_card is set
        if (len(self.cards) == 0) and self.close_first_card:
            self.cards.append(card)
        else:
            # open the card before adding
            card.open = True
            self.cards.append(card)
    
    def show_all_cards(self):
        # open first card if it was closed
        if (len(self.cards) > 0) and self.close_first_card:
            self.cards[0].open = True
        print(self.cards)

    
    def get_total(self):
        total = 0
        for card in self.cards:
            total += card.value
        return total

class Game_Play():
    def __init__(self):
        Game_Play.turn = 1
        self.deck = Deck()
        self.hand = {'DEALER':Hand('DEALER', True), 'PLAYER_ONE':Hand('PLAYER_ONE') }
        self.current_hand = 'PLAYER_ONE'
        print('Welcome to Black Jack')
    
    def start_the_game(self):
        loop = True
        while loop:
            try:
                start = input("Ready to start the game? Y/N: ").upper()
                if start in ['Y', 'N']:
                    loop = False
                else:
                    print("Please enter Y/N")
            except TypeError:
                print("Please enter Y/N")
        
        # add 2 cards to dealer and 2 cards to player_one
        if start == 'Y':
            self.hand['DEALER'].cards.append(self.deck.cards.pop())
            self.hand['PLAYER_ONE'].cards.append(self.deck.cards.pop())
            self.hand['PLAYER_ONE'].cards[-1].open = True
            self.hand['DEALER'].cards.append(self.deck.cards.pop())
            self.hand['DEALER'].cards[-1].open = True
            self.hand['PLAYER_ONE'].cards.append(self.deck.cards.pop())
            self.hand['PLAYER_ONE'].cards[-1].open = True
        return True if start == 'Y' else False

    def show_the_game(self):
        clear_screen()
        print(self.hand['DEALER'])
        print(self.hand['PLAYER_ONE'])

    def hit_or_stand(self):
        hit_or_stand_loop = True
        while hit_or_stand_loop:

            input_loop = True
            while input_loop:
                try:
                    h_or_s = input("{} Enter hit(H) or stand(S): ".format(self.current_hand)).upper()
                    if h_or_s in ['H', 'S']:
                        input_loop = False
                    else:
                        print("Incorrect input!")
                except TypeError:
                        print("Incorrect input!")
        
            if h_or_s == 'H':
                self.hand[self.current_hand].cards.append(self.deck.cards.pop())
                self.hand[self.current_hand].cards[-1].open = True
                self.show_the_game()
                break
            else:
                self.current_hand = 'DEALER' if self.current_hand == 'PLAYER_ONE' else 'PLAYER_ONE'
                self.show_the_game()
                break
    
    def check_win(self):
        result = {}
        for key in self.hand.keys():
            result[key] = 0
            for card in self.hand[key].cards:
                result[key] += card.value
        
        print(result)
        if(result['DEALER'] > result['PLAYER_ONE']) and (result['DEALER'] < 21):
            print("DEALER Won !!")
            return True
        elif(result['DEALER'] < result['PLAYER_ONE']) and (result['PLAYER_ONE'] < 21):
            print("PLAYER_ONE Won !!")
            return True
        return False
    
if __name__ == '__main__':
    game = Game_Play()
    game_on = True

    print(game.deck)

    if (game.start_the_game()):
        game.show_the_game()

        while game_on:
            game.hit_or_stand()
            game_on = not game.check_win()
