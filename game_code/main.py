from game import Game


def play1(game):
    # Alice truthfully places 1
    print("---PLAYER ACTION---")
    game.player_announcement(0, '1', 'PLACE', True)
    game.show_player_hands()
    game.show_world("p1_turn1")

    # Bob truthfully places 2
    print("---PLAYER ACTION---")
    game.player_announcement(1, '2', 'PLACE', True)
    game.show_player_hands()
    game.show_world("p1_turn2")

    # Charlie dishonestly places 3
    print("---PLAYER ACTION---")
    game.player_announcement(2, '3', 'PLACE', False, '2')
    game.show_player_hands()
    game.show_world("p1_turn3")

    # Alice passes
    print("---PLAYER ACTION---")
    game.player_announcement(0, '1', 'PASS')
    game.show_player_hands()
    game.show_world("p1_turn4")

    # Bob passes
    print("---PLAYER ACTION---")
    game.player_announcement(1, '1', 'PASS')
    game.show_player_hands()
    game.show_world("p1_turn5")

    # Charlie truthfully places 1
    print("---PLAYER ACTION---")
    game.player_announcement(2, '1', 'PLACE', True)
    game.show_player_hands()
    game.show_world("p1_turn6_final_state")

    print("CHARLIE WINS")


def play2(game):
    # Alice truthfully places 1
    print("---PLAYER ACTION---")
    game.player_announcement(0, '1', 'PLACE', True)
    game.show_player_hands()
    game.show_world("p2_turn1")

    # Bob truthfully places 2
    print("---PLAYER ACTION---")
    game.player_announcement(1, '2', 'PLACE', True)
    game.show_player_hands()
    game.show_world("p2_turn2")

    # Charlie passes 3
    print("---PLAYER ACTION---")
    game.player_announcement(2, '3', 'PASS')
    game.show_player_hands()
    game.show_world("p2_turn3")

    # Alice truthfully places 3
    print("---PLAYER ACTION---")
    game.player_announcement(0, '3', 'PLACE', True)
    game.show_player_hands()
    game.show_world("p2_turn4_final_state")

    print("ALICE WINS")


def main():
    print('Main')
    game = Game()
    # game.show_world("main")

    # Player has to place cards in order of 1, 2, 3

    play1(game)
    # play2(game)


if __name__ == "__main__":
    main()
