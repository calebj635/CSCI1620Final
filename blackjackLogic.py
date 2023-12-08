from PyQt6.QtWidgets import QMainWindow
from blackjackGui import *
from deck import *
from card import *

class BlackjackLogic(QMainWindow, Ui_MainWindow):
    '''
    Class to handle logic of BlackJack GUI
    '''
    def __init__(self):
        '''
        Function to initialize BlackjackLogic class
        '''
        super().__init__()
        self.setupUi(self)
        self.turn =1
        self.dealerCards = []
        self.playerCards = []
        self.dealCardVal = 0
        self.playCardVal = 0
        self.deck1 = Deck()

        self.label_Wins.setText('')
        self.pushButton_Hit.clicked.connect(self.hit)
        self.pushButton_OK.clicked.connect(self.OK)
        self.pushButton_Exit.clicked.connect(self.exit)

    def hit(self):
        '''
        function to instruct GUI what to display after pressing the 'Hit' button, at first will start the game and give the dealer a card, subsequent hits will give the player more cards.
        '''
        if self.turn == 1:
            self.dealerCards.append(self.deck1.drawCard())
            self.label_DCard1.setText(str(self.dealerCards[-1].return_num()))
            self.dealCardVal += self.dealerCards[-1].return_val()
            self.turn += 1
        elif 2 <= self.turn <= 7:
            self.playerCards.append(self.deck1.drawCard())
            next_label_name = f'label_PCard{self.turn - 1}'
            next_label = getattr(self, next_label_name)
            next_label.setText(str(self.playerCards[-1].return_num()))
            self.playCardVal += self.playerCards[-1].return_val()
            self.turn += 1
        elif self.turn > 7:
            self.label_Wins.setText('Max Card Limit!')


    def OK(self):
        '''
        function to intruct GUI what to display after pressing the 'OK' button, will stop the player from hitting and finish the dealer's cards
        '''
        self.label_Wins.setText('')
        while self.dealCardVal < 17:
            next_label_index = len(self.dealerCards) + 1
            next_label_name = f'label_DCard{next_label_index}'

            if hasattr(self, next_label_name):
                self.dealerCards.append(self.deck1.drawCard())
                self.dealCardVal += self.dealerCards[-1].return_val()

                next_label = getattr(self, next_label_name)
                next_label.setText(str(self.dealerCards[-1].return_num()))
            else:
                break


        if self.dealCardVal > 21 and self.playCardVal > 21:#Both Bust
            self.label_Wins.setText('Both Bust!')
        elif self.dealCardVal > 21 and self.playCardVal <= 21:#Dealer Busts
                self.label_Wins.setText('Player Wins!')
        elif self.dealCardVal <= 21 and self.playCardVal > 21:  # Player Busts
            self.label_Wins.setText('Dealer Wins!')
        elif self.dealCardVal <= 21 and self.playCardVal <= 21:
            if(self.dealCardVal > self.playCardVal):
                self.label_Wins.setText('Dealer Wins!')#Dealer Wins
            if(self.dealCardVal < self.playCardVal):
                self.label_Wins.setText('Player Wins!')#Player Wins
            else:
                self.label_Wins.setText('Tie, Dealer Wins')
        else:
            self.label_Wins.setText(f'{self.dealCardVal} - {self.playCardVal}')

    def exit(self):
        '''
        Function to exit the GUI
        '''
        sys.exit()








