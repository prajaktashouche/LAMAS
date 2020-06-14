from game import Game


def main():
    print('Main')
    game = Game()
    # Announcement: Bob makes a truthful announcement that Ace (of hearts)
    game.player_announcement(1, '1H', 'TRUTH')
    game.show_world()


if __name__ == "__main__":
    main()
