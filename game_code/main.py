from game import Game


def main():
    print('Main')
    game = Game()
    game.show_world("main")

    # Player has to place cards in order of 1H, 2H, 3H, 1S, 2S, 3S

    # Alice passes as they dont have 1H
    print("---PLAYER ACTION---")
    game.player_announcement(0, '1S', 'PLACE', True)
    game.show_player_hands()
    game.show_world("turn1")

    # Bob pass 1S
    print("---PLAYER ACTION---")
    game.player_announcement(1, '1S', 'PASS', True)
    game.show_player_hands()
    game.show_world("turn2")

    # Bob pass 1S
    print("---PLAYER ACTION---")
    game.player_announcement(2, '1S', 'PASS', True)
    game.show_player_hands()
    game.show_world("turn3")

    # Bob places 3S LYING it is a 2
    print("---PLAYER ACTION---")
    game.player_announcement(1, '2H', 'PLACE', False)
    game.show_player_hands()
    game.show_world("turn4")
    #
    # # Charlie pass 2H
    # print("---PLAYER ACTION---")
    # game.player_announcement(2, '2H', 'PASS', None)
    # game.show_player_hands()
    # game.show_world("turn3")
    #
    # print("---PLAYER ACTION---")
    # game.player_announcement(0, '2H', 'PLACE', None)
    # game.show_player_hands()
    # game.show_world("turn1")


if __name__ == "__main__":
    main()
