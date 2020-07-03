from itertools import product
import random
import time
import os
from game import Game


class Strategy:
    def __init__(self):

        self.announcement = [["PASS", None], ["PLACE", False]]
        self.player_ids = [0, 1, 2]
        self.cards_at_turn = ['1', '2', '3']

        self.strategies = {}
        self.get_strategies()

        self.stats = {}

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
                call_bluff = game.player_announcement(player_idx, card_to_place, "PLACE", True)
                turns.append([player_idx, "PLACE", True, call_bluff])
            else:
                random_strategy = random.choice(self.strategies[player_idx])
                [announcement, statement] = random_strategy

                random_card = random.choice(player_hand) if announcement == "PLACE" else None
                call_bluff = game.player_announcement(player_idx, card_to_place, announcement, statement, random_card)
                turns.append([player_idx, announcement, statement, call_bluff])

            # reset player id
            player_idx += 1
            if player_idx > 2:
                player_idx = 0

            # reset card to place
            if announcement == "PLACE":
                card_at_turn_idx += 1
                if card_at_turn_idx > 2:
                    card_at_turn_idx = 0
            card_to_place = self.cards_at_turn[card_at_turn_idx]

            for p in players:
                if p.is_empty():
                    ret_player = p.player_id
                    in_play = False
                    break

        return ret_player, turns

    @staticmethod
    def write_to_file(plays):
        filename = "./strategies.txt"

        if os.path.exists(filename):
            os.remove(filename)

        with open(filename, 'a+') as file:
            for key, val in plays.items():
                file.write("\n")
                file.write("------PLAYER: {}".format(key))
                for item in val:
                    file.write("\n")
                    file.write("{}".format(item))

    @staticmethod
    def print_time():
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        print(current_time)

    def simulate_multiple_plays(self, deal_type):
        runs = 100
        start = time.time()
        self.print_time()

        self.stats = {}
        for i in range(runs):
            game = Game(deal_type)
            player, play = self.get_plays(game)
            if player in self.stats:
                self.stats[player].append(play)
            else:
                self.stats[player] = [play]

        self.write_to_file(self.stats)

        self.print_time()
        print('It took', time.time() - start, 'seconds.')

        self.get_stats()

    def get_stats(self):

        # get stats for getting called on bluff
        bluff_called_stats = {}
        for key, val in self.stats.items():
            counter = 0
            for play in val:
                # check last play was called a bluff - loses game
                strat = play[-1]
                if strat[2] is False and strat[3] is True:
                    counter += 1
            bluff_called_stats[key] = counter / len(val)

        # get stats for getting away with bluff
        bluff_stats = {}
        for key, val in self.stats.items():
            counter = 0
            for play in val:
                # check last play
                strat = play[-1]
                if strat[3] is False:
                    player_play = [x for x in play if x[0] == key and x[2] is False]
                    if len(player_play) > 0:
                        counter += 1

            bluff_stats[key] = counter / len(val)

        print("Winner ratio---")
        for key, val in self.stats.items():
            print(key, len(val))

        print("Getting away with bluffing---")
        for key, val in bluff_stats.items():
            print(key, val * 100)

        print("Getting called on their bluff---")
        for key, val in bluff_called_stats.items():
            print(key, val * 100)

strat = Strategy()
strat.simulate_multiple_plays(2)
