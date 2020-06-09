from copy import deepcopy
from itertools import permutations
from deck import Deck
from card import Card


class Player:
    cardsList = [1, 2, 3, 4, 5, 6]
    colors = ['red', 'blue', 'green']
    player_ids = [0, 1, 2]

    def __init__(self, name, player_id):
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
        ret = [card.card for card in self.hand]
        print("({}, {})".format(*ret))

    def get_hand(self):
        ret_obj = [card.card for card in self.hand]
        return ret_obj

    def get_hand_str(self):
        ret_obj = [card.card for card in self.hand]
        return "({},{})".format(*ret_obj)

    def get_color(self):
        return self.colors[self.player_id]

    def get_all_paths(self):
        paths = []

        # generate deck with cards
        deck = Deck()
        card_list = deck.list()

        # remove own cards from card_list
        for n in self.get_hand():
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
        player_ids = [i for i in self.player_ids if i != self.player_id]

        paths = self.get_all_paths()

        for path in paths:
            deal1, deal2 = path

            other_player_1 = Player("", player_ids[0])
            other_player_1.set_hand(deal1)

            other_player_2 = Player("", player_ids[1])
            other_player_2.set_hand(deal2)

            self.possible_worlds.append([other_player_1, other_player_2])

    def update_possible_worlds(self):
        pass




