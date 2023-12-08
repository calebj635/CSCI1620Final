from PyQt6.QtWidgets import QApplication
from blackjackLogic import BlackjackLogic

def main():
    '''
    main function, pulls up the BlackJack GUI
    Notable House Rules:
    In this game it's notable that Aces only count for 1 (not 11 as well), and that you may continue drawing cards after a bust (redundant drawing)
    To save space on the GUI, only 6 cards max may be drawn
    '''
    application = QApplication([])
    window = BlackjackLogic()
    window.show()
    application.exec()

if __name__ == '__main__':
    main()