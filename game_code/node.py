from pyvis.network import Network
from itertools import combinations


class Node:

    def __init__(self, players):
        self.net = Network()
        self.players = players

    def generate(self):

        player_ids = [0, 1, 2]

        # create root nodes and edges
        for player in self.players:
            self.net.add_node(player.player_id, label=player.get_hand_str(), color=player.get_color(), shape='ellipse')

        root_combos = list(combinations(player_ids, 2))
        for pair in root_combos:
            self.net.add_edge(pair[0], pair[1], color='black')

        # create child nodes for each player
        node_id = len(self.players)

        for player in self.players:
            for player1, player2 in player.possible_worlds:
                world_node = "{}, {}".format(player1.get_hand_str(), player2.get_hand_str())
                self.net.add_node(node_id, label=world_node)
                self.net.add_edge(player.player_id, node_id, color=player.get_color())
                node_id += 1

        self.net.show('graph.html')