class Card:
    def __init__(self, card):
        self.card = card
        self.val = card[0]
        self.suit = card[1]

    def show_card(self):
        print(self.card)

