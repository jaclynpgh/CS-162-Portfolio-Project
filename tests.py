from JanggiGame import JanggiGame

game = JanggiGame()


def checkmate():
    game.make_move('e7', 'e6')
    game.make_move('e2', 'e2')
    game.make_move('e6', 'e5')
    game.make_move('e2', 'e2')
    game.make_move('e5', 'e4')
    game.make_move('e2', 'e2')
    game.make_move('e4', 'd4')
    game.make_move('e2', 'e2')
    game.make_move('d4', 'c4')
    game.make_move('e2', 'e2')
    game.make_move('a10', 'a9')
    game.make_move('e2', 'e2')
    game.make_move('a9', 'd9')
    game.make_move('e2', 'e2')
    game.make_move('d9', 'd8')
    game.make_move('e2', 'e2')
    game.make_move('d8', 'd7')
    game.make_move('e2', 'e2')
    game.make_move('d7', 'd6')
    game.make_move('i1', 'i2')
    game.make_move('e9', 'e9')
    game.make_move('i2', 'g2')
    game.make_move('e9', 'e9')
    game.make_move('i4', 'h4')
    game.make_move('e9', 'e9')
    game.make_move('h3', 'h5')
    game.make_move('i10', 'i9')
    game.make_move('e2', 'e2')
    game.make_move('i9', 'g9')
    game.make_move('e2', 'e2')
    game.make_move('g9', 'g8')
    game.make_move('e2', 'e2')
    game.make_move('h8', 'f8')
    game.make_move('f1', 'e1')
    game.make_move('g7', 'f7')
    game.make_move('e2', 'e2')
    game.make_move('i7', 'i6')
    game.make_move('e2', 'e2')
    game.make_move('g10', 'i7')
    game.make_move('e2', 'e2')
    game.make_move('i7', 'f5')
    game.make_move('e2', 'e2')
    game.make_move('f5', 'd8')
    game.make_move('e2', 'e2')
    game.make_move('d8', 'b5')
    game.make_move('e2', 'e2')
    game.make_move('c4', 'd4')
    game.make_move('e2', 'e2')
    game.make_move('d4', 'e4')
    print(game.get_game_state())
    game.make_move('e2', 'e2')
    print(game.get_game_state())
    # checkmate
    print(game.make_move('e4', 'e3'))
    print(game.make_move("e2", "e3"))
    print(game.get_game_state())

def check_moves():
    print(game.make_move("c7", "c6"))
    print(game.make_move("c1", "d3"))
    print(game.make_move("b10", "d7"))
    print(game.make_move("b3", "e3"))
    print(game.make_move("c10", "d8"))
    print(game.make_move("h1", "g3"))
    print(game.make_move("e7", "e6"))
    print(game.make_move("e3", "e6"))
    print(game.make_move("h8", "c8"))
    print(game.make_move("d3", "e5"))
    print(game.make_move("c8", "c4"))
    print(game.make_move("e5", "c4"))
    print(game.make_move("i10", "i8"))
    print(game.make_move("g4", "f4"))
    print(game.make_move("i8", "f8"))
    print(game.make_move("g3", "h5"))
    print(game.make_move("h10", "g8"))
    print(game.get_game_state())
    print(game.make_move("e6", "e3"))
    print(game.get_game_state())
    print(game.is_in_check("blue"))
    print(game.make_move("e9", "d9"))
    print(game.is_in_check("blue"))
    print(game.get_game_state())
    print(game.is_in_check("blue"))

checkmate()
game.print_board()