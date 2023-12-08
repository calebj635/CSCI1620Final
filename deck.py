from card import *
import random

class Deck:
    '''
    Class to simulate a standard deck of 52 playing cards
    '''
    def __init__(self):
        '''
        Function to initialize Deck class, assigns 52 card objects their respective values and shuffles them
        It's noteworthy that Aces only count as 1 in this game
        '''
        self.card_categories = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.cards_list = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.deck = []

        for category in self.card_categories:
            for card_num in self.cards_list:
                self.deck.append(Card(category, card_num))

        random.shuffle(self.deck)

    def drawCard(self):
        '''
        function to return the card 'on top' of the deck and remove it from the deck, simulating 'drawing' a card
        :return: returns a single card object that was first in the list
        '''
        self.card1 = self.deck[0]
        del self.deck[0]
        return self.card1
