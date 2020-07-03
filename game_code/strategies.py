from itertools import product
import random
import time
from game import Game


class Strategy:
    def __init__(self):

        self.announcement = [["PASS", None], ["PLACE", False]]
        self.player_ids = [0, 1, 2]
        self.cards_at_turn = ['1', '2', '3']

        self.strategies = {}
        self.get_strategies()

    def get_strategies(self):
        strategies = list(product(self.player_ids, self.announcement))
        for player_idx, strategy in strategies:
            if player_idx in self.strategies:
                self.strategies[player_idx].append(strategy)
            else:
                self.strategies[player_idx] = [strategy]

    def get_plays(self, game):
        turns = []
        players = game.players
        player_idx = 0
        card_at_turn_idx = 0
        card_to_place = self.cards_at_turn[card_at_turn_idx]
        in_play = True

        ret_player = -1

        while in_play:
            announcement = "PLACE"
            player_hand = players[player_idx].get_hand_values()
            if card_to_place in player_hand:
                game.player_announcement(player_idx, card_to_place, "PLACE", True)
                turns.append(["PLACE", True])
            else:
                random_strategy = random.choice(self.strategies[player_idx])
                [announcement, statement] = random_strategy

                random_card = random.choice(player_hand) if announcement == "PLACE" else None
                game.player_announcement(player_idx, card_to_place, announcement, statement, random_card)
                turns.append([announcement, statement])

            # reset player id
            player_idx += 1
            if player_idx > 2:
                player_idx = 0

            # reset card to place
            if announcement == "PLACE":
                card_at_turn_idx += 1
                if card_at_turn_idx > 2:
                    card_at_turn_idx = 0

            for p in players:
                if p.is_empty():
                    ret_player = p.player_id
                    in_play = False
                    break

            card_to_place = self.cards_at_turn[card_at_turn_idx]

        return ret_player, turns

    def simulate_multiple_plays(self, deal_type):
        runs = 20
        start = time.time()
        stats = {}
        for i in range(runs):
            game = Game(deal_type)
            player, play = self.get_plays(game)
            if player in stats:
                stats[player].append(play)
            else:
                stats[player] = [play]

        for key, val in stats.items():
            print(key, len(val))

        print('It took', time.time() - start, 'seconds.')


strat = Strategy()
strat.simulate_multiple_plays(1)
