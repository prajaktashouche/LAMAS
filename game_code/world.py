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

        for world_id in self.possible_worlds:
            player_idx = 0
            for player_hand in self.possible_worlds[world_id]:
                player = Player(name=None, player_id=player_idx)
                player.set_hand(player_hand)
                player.generate_possible_worlds()

                for pos in player.possible_worlds:
                    to_node_id = self.get_node_key(pos)
                    self.relations[i] = [world_id, to_node_id, player.get_color()]
                    i += 1
                player_idx += 1

    def update_worlds(self):
        remove = []
        for world_id, p in self.possible_worlds.items():
            flag = 0
            for rel in self.relations.values():
                if world_id in rel:
                    flag = 1
            if flag == 0:
                remove.append(world_id)

        for k in remove:
            self.possible_worlds.pop(k)

        print(self.possible_worlds)

    def update_relations(self, player):
        remove = []
        for key, val in self.relations.items():
            if player.get_color() in val:
                remove.append(key)

        for k in remove:
            self.relations.pop(k)

        i = len(self.relations) + 1
        for world_id, p in player.possible_worlds.items():
            for w, pos in player.possible_worlds.items():
                to_node_id = self.get_node_key(pos)
                # print(world_id, to_node_id)
                self.relations[i] = [world_id, to_node_id, player.get_color()]
                i += 1


    def assign_real_world(self, real_world):
        key_0 = 0
        value_0 = self.get_node_value(key_0)
        key_1 = self.get_node_key(real_world)

        # swap keys
        if value_0 is not None and key_1 is not None:
            self.possible_worlds[key_0] = real_world
            self.possible_worlds[key_1] = value_0

    def show_kripke_model(self):
        node = Node(nodes=self.possible_worlds, edges=self.relations)
        node.show_kripke_model()
