from mlsolver.kripke import KripkeStructure, World
# from mlsolver.model import add_reflexive_edges, add_symmetric_edges


def kripke_model(game):
    deck = game.deck.dealt_cards

    # Worlds
    worlds = []
    for w, p in game.world.possible_worlds.items():
        worlds.append(World(w, {str(0) + str(p[0]): True, str(1) + str(p[1]): True, str(2) + str(p[2]): True}))

    # Relations
    relations = {
        0: set([]),
        1: set([]),
        2: set([])
    }

    colors = game.players[0].colors
    for r_id, r in game.world.relations.items():
        relations[colors.index(r[2])].add((r[0], r[1]))

    # relations.update(add_reflexive_edges(worlds, relations))
    # relations.update(add_symmetric_edges(relations))

    # Make kripke model
    ks = KripkeStructure(worlds, relations)

    print(relations)




    # deck = ['A', 'A', '2', '2', '3', '3']

    # # A trial for generating all possible worlds (can be made more efficient)
    # combinations = set(list(itertools.combinations(deck, 2)))
    # possible = set(list(itertools.product(combinations, repeat=3)))
    #
    # # Currently, there are duplicates such as (2,3) and (3,2) are treated as different
    # possible_worlds = []
    # for p in possible:
    #     # Count the occurrence of each card in the combination
    #     count = [0, 0, 0]
    #     for i, card in enumerate(set(deck)):
    #         count[i] += Counter(j[0] for j in list(p))[card] + Counter(j[1] for j in list(p))[card]
    #
    #     # Only keep the combinations were the total count of each card is exactly 2
    #     if not any(c != 2 for c in count):
    #         possible_worlds.append(p)
    #
    # possible_worlds = set(possible_worlds)

    # Make kripke model of the possible worlds

def main():

    kripke_model()


if __name__ == "__main__":
    main()
