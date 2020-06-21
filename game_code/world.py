from itertools import combinations, permutations
from deck import Deck
from player import Player
from node import Node


class World:

    def __init__(self):
        self.possible_worlds = {}
        self.relations = {}

        self.generate_worlds()
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
                        self.relations[i] = [world_id, to_node_id, player.get_color()]
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

    def check_statement(self, player_id, value):
        # TODO: check if bluff or not, currently pass false
        player = Player(name=None, player_id=player_id)
        flag = 0
        for key, h in self.possible_worlds.items():
            for rel_id, rel in self.relations.items():
                if key == rel[0] and player.get_color() != rel[2]:
                    for hand in self.possible_worlds[rel[1]]:
                        player_hand = hand[player_id]

                        if value in player_hand:
                            flag = 1
        if not flag:
            return True
        return False

    def update_action_pass(self, player_id, value):
        keys_to_remove = []

        for key, hand in self.possible_worlds.items():
            # for each world, check the player hand, if it matches remove from the world
            # essentially pass is when there is no world where the player has that hand
            # announcing you don't have the card also updates other players possible world
            player_hand = hand[player_id]
            if value in player_hand:
                keys_to_remove.append(key)

        for k in keys_to_remove:
            print("#DEBUG# Keys removed: ", k)
            self.possible_worlds.pop(k)

    def update_action_place(self, player_id, value):
        call_bluff = self.check_statement(player_id, value)

        # player announced a false statement
        if call_bluff:
            print(str(player_id) + ' Calling bluff')
            pass

        # player announced a true statement
        else:
            keys_to_remove = []

            # update worlds
            # worlds where the player has a different card as possible will be removed
            for key, hand in self.possible_worlds.items():
                player_hand = hand[player_id]
                if value not in player_hand:
                    keys_to_remove.append(key)

            for k in keys_to_remove:
                print("#DEBUG# Keys removed: ", k)
                self.possible_worlds.pop(k)

        return call_bluff

    def update_worlds(self, player_id, value, action):
        call_bluff = False

        if action == "PASS":
            self.update_action_pass(player_id, value)

        elif action == "PLACE":
            call_bluff = self.update_action_place(player_id, value)

        self.generate_relations()

        return call_bluff
