from deck import Deck
from player import Player
from world import World


class Game:

    def __init__(self):

        # build deck with explicit cards
        self.deck = Deck()
        self.deck.build_dev()

        # we have 3 players initialized with player IDs
        self.players = [Player("Alice", 0), Player("Bob", 1), Player("Charlie", 2)]

        # deal the cards explicitly to players
        self.deck.deal(self.players)

        # build possible worlds at init
        self.world = World()
        self.world.assign_real_world(self.deck.dealt_cards)

    def player_announcement(self, player_id, card_val, action):

        current_player = self.players[player_id]

        if action == "PASS":
            pass
        elif action == "LIE":
            pass
        elif action == "TRUTH":
            for id, p in enumerate(self.players):
                if id != player_id:
                    p.update_possible_worlds(id, self.deck.dealt_cards[id], card_val, current_player)


    def show_world(self):
        self.world.show_kripke_model()

