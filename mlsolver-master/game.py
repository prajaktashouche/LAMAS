import random


def deal_cards(players=3):
    # Keeping deck from Ace-3 for two suits
    deck = ['Ace', 'Ace', 'Two', 'Two', 'Three', 'Three']

    # Dictionary representing the dealt cards to each of the players
    cards = {}
    for i in range(1, players + 1):
        cards[str(i)] = []

    while deck:
        for k in cards.keys():
            c = random.choice(deck)
            cards[k].append(c)
            deck.remove(c)

    print(cards)


if __name__ == "__main__":
    deal_cards(3)


