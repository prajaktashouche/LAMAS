from game import Game


def main():
    print('Main')
    game = Game()
    game.show_world()
    # Announcement: Bob makes a truthful announcement that Ace (of spades)
    game.player_announcement(1, '1H', 'TRUTH')


if __name__ == "__main__":
    main()
