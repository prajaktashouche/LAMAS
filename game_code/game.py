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

    def player_announcement(self, player_id, card_val, action, truth):
        call_bluff = self.world.update_worlds(player_id, card_val, action, truth)

        if action == "PLACE":
            # TODO: action to do if its a bluff
            if call_bluff:
                pass

            if not truth:
                # If the player is lying then remove one of the cards from their hand
                card = self.players[player_id].get_hand()[0]
                self.players[player_id].update_hand(card)

            # update player hand to remove the placed cards
            else:
                self.players[player_id].update_hand(card_val)

    def show_player_hands(self):
        for p in self.players:
            p.show_hand()

    def show_world(self, graph_name):
        self.world.show_kripke_model(graph_name)
