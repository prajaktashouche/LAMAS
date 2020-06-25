from copy import deepcopy
from itertools import permutations
from deck import Deck
from card import Card

player_color = {0: 'red', 1: 'blue', 2: 'green'}

class Player:
    cardsList = [1, 2, 3, 4, 5, 6]
    colors = ['red', 'blue', 'green']
    player_ids = [0, 1, 2]

    def __init__(self, name=None, player_id=None):
        self.name = name
        self.player_id = player_id
        self.hand = []
        self.possible_worlds = []

    def draw(self, deck):
        self.hand.append(deck.draw_card())
        return self

    def set_hand(self, deal):
        for card in deal:
            self.hand.append(Card(card))

    def show_name(self):
        print(self.name)

    def show_hand(self):
        ret = [cObj.card for cObj in self.hand]
        print("({})".format(",".join(ret)))

    def get_hand(self, tup=True):
        if tup:
            ret_obj = tuple(card.card for card in self.hand)
        else:
            ret_obj = [card.card for card in self.hand]
        return ret_obj

    def get_hand_str(self):
        ret_obj = [card.card for card in self.hand]
        return "({},{})".format(*ret_obj)

    def get_color(self):
        return self.colors[self.player_id]

    def reorder_paths(self, paths):
        ret = []
        if self.player_id == 0:
            for path in paths:
                ret.append([self.get_hand(), path[0], path[1]])

        elif self.player_id == 1:
            for path in paths:
                ret.append([path[0], self.get_hand(), path[1]])

        elif self.player_id == 2:
            for path in paths:
                ret.append([path[0], path[1], self.get_hand()])

        return ret

    def get_all_paths(self):
        paths = []

        # generate deck with cards
        deck = Deck()
        card_list = deck.list()

        # remove own cards from card_list
        for n in self.get_hand(tup=False):
            card_list.remove(n)

        # combination of cards after removing own cards
        combos = tuple(permutations(card_list, 2))
        for combo in combos:

            n_card_list = deepcopy(card_list)
            for n in combo:  # [1], [4]
                n_card_list.remove(n)

            # combination of cards after removing combo
            n_combos = tuple(permutations(n_card_list, 2))
            for n_combo in n_combos:
                paths.append([combo, n_combo])

        return paths

    def generate_possible_worlds(self):
        paths = self.get_all_paths()
        self.possible_worlds = self.reorder_paths(paths)

    def update_hand(self, value):
        i = 0
        idx_to_remove = -1
        for cObj in self.hand:
            if cObj.card == value:
                idx_to_remove = i
            i += 1

        if idx_to_remove > -1:
            self.hand.pop(idx_to_remove)


