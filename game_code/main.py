from game import Game
from model import kripke_model


def main():
    print('Main')
    game = Game()
    kripke_model(game)

    # Announcement: Bob makes a truthful announcement that Ace (of hearts)
    game.player_announcement(1, '1H', 'TRUTH')
    kripke_model(game)
    game.show_world()


if __name__ == "__main__":
    main()
