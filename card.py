class Card:
    '''
    Class to represent on single playing card, with values of both face/number and category
    '''
    def __init__(self, category, number):
        '''
        function initializes Card class
        :param category: represents the sign of the card, either Spade, Club, Heart, or Diamond
        :param number: represents the face/value of the card, from Ace, 2-10, and Jack, Queen, and King
        '''
        self.card_category = category
        self.card_num = number

    def return_num(self):
        '''
        function to return the card's number in String format
        :return: the card's number/face in String format
        '''
        return self.card_num

    def return_val(self):
        '''
        returns the card's number value in int format
        :return: the card's number/face worth in int format
        '''
        if self.card_num == 'A':
            return 1
        elif self.card_num in {'K', 'Q', 'J'}:
            return 10
        else:
            try:
                return int(self.card_num)
            except ValueError:
                return 0

    def __str__(self):
        '''
        function overides the __str__ method, returning card_num and card_category as a String
        :return: returns card_num and card_category info as a single String
        '''
        return f'{self.card_num}, {self.card_category}'