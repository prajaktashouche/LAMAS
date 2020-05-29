from mlsolver.kripke import World, KripkeStructure
import itertools

import numpy as np
from collections import Counter


def kripke_model():

    deck = ['A', 'A', '2', '2', '3', '3']

    # A trial for generating all possible worlds (can be made more efficient)
    combinations = set(list(itertools.combinations(deck, 2)))
    possible = set(list(itertools.product(combinations, repeat=3)))

    # Currently, there are duplicates such as (2,3) and (3,2) are treated as different
    possible_worlds = []
    for p in possible:
        # Count the occurrence of each card in the combination
        count = [0, 0, 0]
        for i, card in enumerate(set(deck)):
            count[i] += Counter(j[0] for j in list(p))[card] + Counter(j[1] for j in list(p))[card]

        # Only keep the combinations were the total count of each card is exactly 2
        if not any(c != 2 for c in count):
            possible_worlds.append(p)

    possible_worlds = set(possible_worlds)

    # Make kripke model of the possible worlds

def main():
    kripke_model()


if __name__ == "__main__":
    main()
