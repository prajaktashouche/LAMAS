from operator import itemgetter
from itertools import combinations, permutations, groupby
import random

from deck import Deck
from player import Player
from node import Node


class World:

    def __init__(self, real_world):
        self.possible_worlds = {}
        self.relations = {}

        self.generate_worlds()
        self.assign_real_world(real_world)
        self.generate_relations()

    def get_node_key(self, value):

        for key, val in self.possible_worlds.items():
            check = True
            c = []
            for tup in value:
                c.append(list(permutations(tup)))

            for i in range(len(value)):
                if val[i] not in c[i]:
                    check = False
                    break

            if check:
                return key

    def get_node_value(self, node_id):
        for key, val in self.possible_worlds.items():
            if key == node_id:
                return val

    def generate_worlds(self):
        i = 0

        # generate deck with cards
        card_list = Deck()
        deck = card_list.list()

        # get all possible worlds for 6 cards, 2 hand and 3 players
        cards = set(deck)
        for first in combinations(cards, 2):
            for second in combinations(cards - set(first), 2):
                for third in combinations(cards - set(first) - set(second), 2):
                    self.possible_worlds[i] = [first, second, third]
                    i += 1

    def generate_relations(self):
        i = 0

        self.relations.clear()

        for world_id in self.possible_worlds:
            player_idx = 0
            for player_hand in self.possible_worlds[world_id]:
                player = Player(name=None, player_id=player_idx)
                player.set_hand(player_hand)
                player.generate_possible_worlds()

                for pos in player.possible_worlds:
                    to_node_id = self.get_node_key(pos)
                    if to_node_id is not None:
                        if world_id != to_node_id:  # remove relations to self, no reflexivity
                            self.relations[i] = [world_id, to_node_id, player.get_color(), player_idx]
                            i += 1
                player_idx += 1

    def assign_real_world(self, real_world):
        key_0 = 0
        value_0 = self.get_node_value(key_0)
        key_1 = self.get_node_key(real_world)

        # swap keys
        if value_0 is not None and key_1 is not None:
            self.possible_worlds[key_0] = real_world
            self.possible_worlds[key_1] = value_0

    def show_kripke_model(self, graph_name):
        node = Node(nodes=self.possible_worlds, edges=self.relations)
        node.show_kripke_model(graph_name)

    def remove_possible_worlds(self, player_id, value):
        keys_to_remove = []

        for key, hand in self.possible_worlds.items():
            player_hand = [x[0] for x in hand[player_id]]
            if value not in player_hand:
                keys_to_remove.append(key)

        # do NOT remove real world
        if 0 in keys_to_remove:
            keys_to_remove.remove(0)

        for k in keys_to_remove:
            self.possible_worlds.pop(k)

    def check_statement(self, player_id, value):
        call_bluff = False
        bluff_player_id = -1

        # get all to_nodes from real_world of other players
        # v 0: from_node, 1: to_node, 2: player_color, 3: player_id
        relations = [[v[3], v[1]] for k, v in self.relations.items() if v[0] == 0 and v[3] != player_id]
        relations.sort(key=itemgetter(0))

        checklist = {}

        # group by player_id and loop thru each to_node
        for player_idx, g in groupby(relations, lambda x: x[0]):
            for _, to_node_key in list(g):

                hand = self.get_node_value(to_node_key)
                player_hand = [x[0] for x in hand[player_id]]

                if player_idx in checklist:
                    checklist[player_idx].append(1 if value in player_hand else 0)
                else:
                    checklist[player_idx] = [1 if value in player_hand else 0]

        for player_idx, val in checklist.items():
            if 1 not in val:
                bluff_player_id = player_idx
                call_bluff = True
                break

        return call_bluff, bluff_player_id

    def update_action_pass(self, player_id, value):
        keys_to_remove = []

        for key, hand in self.possible_worlds.items():
            # for each world, check the player hand, if it matches remove from the world
            # essentially pass is when there is no world where the player has that hand
            # announcing you don't have the card also updates other players possible world
            player_hand = [x[0] for x in hand[player_id]]
            if value in player_hand:
                keys_to_remove.append(key)

        # do NOT remove real world
        if 0 in keys_to_remove:
            keys_to_remove.remove(0)

        for k in keys_to_remove:
            self.possible_worlds.pop(k)

    def update_action_place(self, player_id, value, truth):

        call_bluff, bluff_player_id = self.check_statement(player_id, value)

        # player announced true statement
        if truth:

            # bluff is called (not expected)
            # other player who called bluff loses
            # TODO: do nothing?
            if call_bluff:
                pass

            # no bluff is called (expected)
            # player: no update on possible worlds
            # other players: remove possible worlds where announced card does not exist
            else:
                self.remove_possible_worlds(player_id, value)

        # player announced false statement
        else:

            # bluff is called (expected)
            # player loses
            # TODO:
            if call_bluff:
                pass    # nothing to do here?

            # no bluff is called (not expected)
            # player hand: no update on possible worlds
            # other players: update possible worlds with wrongly announced card
            else:
                self.remove_possible_worlds(player_id, value)

        return call_bluff, bluff_player_id

    def update_worlds(self, player_id, value, action, truth):
        call_bluff = False
        bluff_player_id = -1

        if action == "PASS":
            # THINK: Do nothing?
            pass
            # self.update_action_pass(player_id, value)

        elif action == "PLACE":
            call_bluff, bluff_player_id = self.update_action_place(player_id, value, truth)

        self.generate_relations()

        return call_bluff, bluff_player_id
