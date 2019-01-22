class Chips:
    '''
    The Chips class helps determine the amount of chips remaining after the bet
    '''
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0

    def win_bet(self):
        '''
        If won the bet gets added
        :return: None
        '''
        self.total += self.bet

    def lose_bet(self):
        '''
        If lost the bet gets deducted
        :return:
        '''
        self.total -= self.bet