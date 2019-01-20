
from deckofcards import *

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        '''
        add a new card to the hand
        :param card: an object <Deal>
        :return: None
        '''
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == "Ace":
            self.aces += 1

    def adjust_for_ace(self):
        '''
        helps adjust the ace card so that the value is under 21
        :return: None
        '''
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
