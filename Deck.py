from Card import *
from deckofcards import *

import random

class Deck:
    '''
    Create a deck of cards.
    '''
    def __init__(self):
        '''
        :returns: None
        '''
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        '''
        :return: the deck of cards in a list.
        '''
        deck_comp = ''  # Start with an empty string
        for card in self.deck:
            deck_comp += '\n ' + card.__str__()
        return 'The deck has: ' + deck_comp

    def shuffle(self):
        '''
        shuffles the deck of cards
        :return:
        '''
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card

