from mlsolver.kripke import World, KripkeStructure
import itertools


def kripke_model():

    # Currently, a trial just for Aces:
    # Generate all possible combinations of dealing Aces amongst the three players
    value = [True, False]
    possibilities = list(itertools.product(value, repeat=3))

    worlds = []
    for i, p in enumerate(possibilities):
        if i != 1:  # Skip True, True, True since there are only two aces
            v1, v2, v3 = p
            worlds.append(World(str(i), {'Ace_1': v1, 'Ace_2': v2, 'Ace_3': v3}))

    print(worlds)


def main():
    kripke_model()


if __name__ == "__main__":
    main()
