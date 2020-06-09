from deck import Deck
from player import Player
from node import Node


class Game:

    def __init__(self):
        self.deck = Deck()
        self.deck.build_dev()

        self.players = [Player("Alice", 0), Player("Bob", 1), Player("Charlie", 2)]

        self.deck.deal(self.players)

        for p in self.players:
            p.show_name()
            p.show_hand()
            p.generate_possible_worlds()

    def player_announcement(self, player_id, card_val, action):

        current_player = self.players[player_id]

        if action == "PASS":
            pass
        elif action == "LIE":
            pass
        elif action == "TRUTH":
            pass

    def show_graph(self):

        node = Node(self.players)
        node.generate()


