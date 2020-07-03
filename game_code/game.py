from deck import Deck
from player import Player
from world import World


class Game:

    def __init__(self, deal_type):

        # build deck with explicit cards
        self.deck = Deck()
        self.deck.build_dev(deal_type)

        # we have 3 players initialized with player IDs
        self.players = [Player("Alice", 0), Player("Bob", 1), Player("Charlie", 2)]

        # deal the cards explicitly to players
        self.deck.deal(self.players)

        # build possible worlds at init
        self.world = World(self.deck.dealt_cards)

    def player_announcement(self, player_id, card_val, action, truth=None, placed_card_val=None):

        call_bluff, bluff_player_id = self.world.update_worlds(player_id, card_val, action, truth)

        if action == "PLACE":

            # player announced true statement
            if truth:

                # bluff is called (not expected)
                # other player who called bluff loses
                if call_bluff:
                    self.players[bluff_player_id].lose_hand()
                    print("Player:{} LOST!".format(self.players[bluff_player_id].name))

                # no bluff is called (expected)
                # player hand: remove announced card
                else:
                    self.players[player_id].update_hand(card_val)

            # player announced false statement
            else:

                # bluff is called (expected)
                # player loses
                if call_bluff:
                    self.players[player_id].lose_hand()
                    print("Player:{} LOST!".format(self.players[player_id].name))

                # no bluff is called (not expected)
                # player hand: remove placed card
                else:
                    self.players[player_id].update_hand(placed_card_val)

        elif action == "PASS":
            pass    # do nothing

        return call_bluff

    def show_player_hands(self):
        for p in self.players:
            p.show_hand()

    def show_world(self, graph_name):
        self.world.show_kripke_model(graph_name)
