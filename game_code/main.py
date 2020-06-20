from game import Game


def main():
    print('Main')
    game = Game()
    game.show_world("main")

    # Player has to place cards in order of 1H, 2H, 3H, 1S, 2S, 3S

    # Alice passes as they dont have 1H
    print("---PLAYER ACTION---")
    game.player_announcement(0, '1H', 'PASS')
    game.show_player_hands()
    game.show_world("turn1")

    # Bob places 1H
    print("---PLAYER ACTION---")
    game.player_announcement(1, '1H', 'PLACE')
    game.show_player_hands()
    game.show_world("turn2")

    # Charlie pass 2H
    print("---PLAYER ACTION---")
    game.player_announcement(2, '2H', 'PASS')
    game.show_player_hands()
    game.show_world("turn3")

if __name__ == "__main__":
    main()
