# Author: Jaclyn Sabo
# Date: 3/8/2021
# Description: Portfolio Project - Janggi Game, a korean version of chess with a Pieces class that passes common properties to
# various Janggi pieces: General, Soldier, Cannon, Chariot, Horse, Elephant, Guard, and  a JanggiGame class that
# initializes the board and has methods to make moves, update the current state of the game, and check for checkmate


class Piece:
    """parent class that represents common properties and methods of pieces in janggi"""

    def __init__(self, curr_row, curr_column):
        """initializes pieces for janggi
        :param curr_row: current corresponding row of piece on board
        :param curr_column: current column of piece on board"""
        self._curr_row = curr_row
        self._curr_column = curr_column

    def check_move_legal(self, move_to_row, move_to_col, board):
        """method to check valid move properties that are common to all pieces by passing in values from the
        Janggi Class that correspond to a certain piece on the board
        :param move_to_row: is an index that represents the row to move to
        :param move_to_col: is an index that represents the column to move to
        :param board: passes in the current board prior to making move
        :returns False if there is a piece in the move_to space that is the same color, or
                if move_to space is out of bounds of the board,
                otherwise returns True,
                """
        move_to_space = board[move_to_row][move_to_col]
        current_space = board[self._curr_row][self._curr_column]

        # return True if current = move (indicates a pass)
        if self.get_current_location() == self.obtain_move_space(move_to_row, move_to_col):
            return True

        # check if move_to_space has piece of same color
        for key in current_space.keys():
            for move_key in move_to_space.keys():
                if key == "blue" and move_key == "blue":
                    return False
                if key == "red" and key in move_key == "red":
                    return False

        # check if out of bounds
        if move_to_row > 10 or move_to_row < 1:
            return False
        if move_to_col < "a" or move_to_col > "i":
            return False
        return True

    def obtain_color(self, board):
        """:returns the color of the current piece to be moved """
        current_space = board[self._curr_row][self._curr_column]
        for key in current_space.keys():
            piece_color = key
            return piece_color

    def red_fort(self):
        """:returns a list of the red fort's spaces"""
        red_fort = [(1, "d"), (1, "e"), (1, "f"), (2, "d"), (2, "e"), (2, "f"), (3, "d"), (3, "e"), (3, "f")]
        return red_fort

    def blue_fort(self):
        """:returns a list of the blue fort's spaces"""
        blue_fort = [(8, "d"), (8, "e"), (8, "f"), (9, "d"), (9, "e"), (9, "f"), (10, "d"), (10, "e"), (10, "f")]
        return blue_fort

    def obtain_move_space(self, move_to_row, move_to_col):
        """
        :param move_to_row: is a string that represents the row to move to
        :param move_to_col: is an index that represents the column to move to
        :returns move to space as a tuple"""
        return move_to_row, move_to_col

    def get_current_location(self):
        """:returns current location as a tuple"""
        return self._curr_row, self._curr_column

    def set_location(self, move_to_row, move_to_col):
        """sets location of a piece
        :param move_to_row: is a string that represents the row to move to
        :param move_to_col: is an index that represents the column to move to """
        self._curr_row = move_to_row
        self._curr_column = move_to_col


class Soldier(Piece):
    """represents a soldier piece and inherits from Pieces class"""

    def __init__(self, curr_row, curr_column):
        """initializes pieces for janggi
        :param curr_row: current corresponding row of piece on board
        :param curr_column: current column of piece on board"""
        super().__init__(curr_row, curr_column)

    def valid_move(self, move_to_row, move_to_col, board):
        """ first calls check_move_legal_legal from Pieces ( parent class) for initial check on moves that are common to all pieces,
        if check_move_legal returns True, valid_moves checks to see if a move is valid by passing in values from the
        make_move method in the Janggi Game class
        :param move_to_row: is a string that represents the row to move to
        :param move_to_col: is an index that represents the column to move to
        :param board: passes in the current board prior to making move
        :returns True if the piece has a valid move:
                - 1 space forward (can't move backwards)
                - 1 space on either side
                - if in fort, soldier can move along diagonal lines 1 space
                otherwise, returns False if invalid move"""

        initial_move_legal = super(Soldier, self).check_move_legal(move_to_row, move_to_col, board)
        color = super(Soldier, self).obtain_color(board)
        curr_location = super(Soldier, self).get_current_location()
        red_fort = super(Soldier, self).red_fort()
        blue_fort = super(Soldier, self).blue_fort()
        column_diff = abs(ord(self._curr_column) - ord(move_to_col))
        row_diff = abs(self._curr_row - move_to_row)

        # return True if current = move (indicates a pass)
        if self.get_current_location() == self.obtain_move_space(move_to_row, move_to_col):
            return True
        # validate common moves in Pieces
        if not initial_move_legal:
            return False

        # if in fort, space can move diagonal
        for loc in red_fort:
            if curr_location == loc:
                if column_diff > 1 or row_diff > 1:
                    return False
                else:
                    return True
        for loc in blue_fort:
            if curr_location == loc:
                if column_diff > 1 or row_diff > 1:
                    return False
                else:
                    return True

        # if not in Fort
        else:
            # moves diagonally
            if column_diff >= 1 and row_diff >= 1:
                return False
            if color == "blue":
                # moves backwards or more than one space forward
                if self._curr_row - move_to_row <= -1 or self._curr_row - move_to_row > 1:
                    return False
            elif color == "red":
                # moves backwards or moves more than one space forward
                if self._curr_row - move_to_row >= 1 or self._curr_row - move_to_row < -1:
                    return False
            return True


class Cannon(Piece):
    """ represents a cannon piece and inherits from Pieces class """

    def __init__(self, curr_row, curr_column):
        """initializes pieces for janggi
        :param curr_row: current corresponding row of piece on board
        :param curr_column: current column of piece on board"""
        super().__init__(curr_row, curr_column)

    def valid_move(self, move_to_row, move_to_col, board):
        """ first calls check_move_legal_legal from Pieces ( parent class) for initial check on moves that are common to all pieces,
        if check_move_legal returns True, valid_moves checks to see if a move is valid by passing in values from the
        make_move method in the Janggi Game class
        :param move_to_row: is a string that represents the row to move to
        :param move_to_col: is an index that represents the column to move to
        :param board: passes in the current board prior to making move
        :returns True if the piece has a valid move:
                - full range of movement horizontally or vertically (forward or backward) by jumping over a piece,
                must have exactly one piece to jump over in between current space and move_to space, piece on move_to
                does not count as one, this is piece that will be captured
                - can move or capture diagonally along the diagonal lines in the fort, provided there is an
                intervening piece in the centre, it can only happen if the cannon is at a corner of the fort
                - iterate spaces to check for valid jump piece
                Otherwise, False:
                - move not valid
                - if piece to jump over is another cannon, or if there is no jump piece
                - if cannon tries to occupy (capture) a space with another cannon"""
        initial_move_legal = super(Cannon, self).check_move_legal(move_to_row, move_to_col, board)
        empty_space = {"": ""}
        column_diff = abs(ord(self._curr_column) - ord(move_to_col))
        row_diff = abs(self._curr_row - move_to_row)
        move = board[move_to_row][move_to_col]
        count = 0

        # return True if current = move (indicates a pass)
        if self.get_current_location() == self.obtain_move_space(move_to_row, move_to_col):
            return True
        # validate common moves in Pieces
        if not initial_move_legal:
            return False
        # if trying to capture another cannon
        for value in move.values():
            if value == "can":
                return False

        # moves diagonally
        if column_diff >= 1 and row_diff >= 1:
            return False
        # move vertically
        if self._curr_column == move_to_col:
            if move_to_row < self._curr_row:  # bottom up
                for row in range(move_to_row + 1, self._curr_row):  # look in between rows
                    current_piece = board[row][self._curr_column]
                    # check for cannon in between spaces, cannon cannot jump another cannon
                    for value in current_piece.values():
                        if value == "can":
                            return False
                        elif current_piece == empty_space:
                            row += 1
                        elif current_piece != empty_space:
                            count += 1
                # cannon can jump if there is exactly one piece in between
                if count == 1:
                    return True
                elif count != 1:
                    return False
            elif move_to_row > self._curr_row:  # top down
                for row in range(self._curr_row + 1, move_to_row):  # look in between rows
                    current_piece = board[row][self._curr_column]
                    # check for cannon in between spaces, cannon cannot jump another cannon
                    for value in current_piece.values():
                        if value == "can":
                            return False
                        elif current_piece == empty_space:
                            row += 1
                        elif current_piece != empty_space:
                            count += 1
                # cannon can jump if there is exactly one piece in between
                if count == 1:
                    return True
                elif count != 1:
                    return False

        # move horizontally
        if self._curr_row == move_to_row:
            if ord(move_to_col) < ord(self._curr_column):  # move right to left
                for col in range(ord(move_to_col) + 1, ord(self._curr_column)):  # iterate in between columns
                    current_piece = board[self._curr_row][chr(col)]
                    # check for cannon in between spaces, cannon cannot jump another cannon
                    for value in current_piece.values():
                        if value == "can":
                            return False
                        elif current_piece == empty_space:
                            col += 1
                        elif current_piece != empty_space:
                            count += 1
                # cannon can jump if there is exactly one piece in between
                if count == 1:
                    return True
                elif count != 1:
                    return False
                return True
            elif ord(move_to_col) > ord(self._curr_column):  # move left to right
                for col in range(ord(self._curr_column) + 1, ord(move_to_col)):  # iterate in between columns
                    current_piece = board[self._curr_row][chr(col)]
                    # check for cannon in between spaces, cannon cannot jump another cannon
                    for value in current_piece.values():
                        if value == "can":
                            return False
                        elif current_piece == empty_space:
                            col += 1
                        elif current_piece != empty_space:
                            count += 1
                # cannon can jump if there is exactly one piece in between
                if count == 1:
                    return True
                elif count != 1:
                    return False


class Chariot(Piece):
    """represents a chariot piece and inherits from Pieces class """

    def __init__(self, curr_row, curr_column):
        """initializes pieces for janggi
        :param curr_row: current corresponding row of piece on board
        :param curr_column: current column of piece on board"""
        super().__init__(curr_row, curr_column)

    def valid_move(self, move_to_row, move_to_col, board):
        """ first calls check_move_legal_legal from Pieces (parent class) for initial check on moves that are common to all pieces,
        if check_move_legal_legal returns True, valid_moves checks to see if a move is valid by passing in values from the
        make_move method in the Janggi Game class
        :param move_to_row: is a string that represents the row to move to
        :param move_to_col: is an index that represents the column to move to
        :param board: passes in the current board prior to making move
        :returns True if the piece has a valid move:
                - full range of movement horizontal or vertical, forwards or backwards (like the rook in chess)
                - if in fort, chariot can move along diagonal lines within the fort boundaries
                Otherwise,  False:
                - move is invalid
                - piece is blocking Chariot"""
        initial_move_legal = super(Chariot, self).check_move_legal(move_to_row, move_to_col, board)
        empty_space = {"": ""}
        curr_location = super(Chariot, self).get_current_location()
        red_fort = super(Chariot, self).red_fort()
        blue_fort = super(Chariot, self).blue_fort()
        column_diff = abs(ord(self._curr_column) - ord(move_to_col))
        row_diff = abs(self._curr_row - move_to_row)

        # return True if current = move (indicates a pass)
        if self.get_current_location() == self.obtain_move_space(move_to_row, move_to_col):
            return True
        # validate common moves in Pieces
        if not initial_move_legal:
            return False

        # if in fort, chariot can move diagonal
        for loc in red_fort:
            if curr_location == loc:
                if column_diff > 2 or row_diff > 2:
                    return False
                else:
                    return True
        for loc in blue_fort:
            if curr_location == loc:
                if column_diff > 2 or row_diff > 2:
                    return False
                else:
                    return True

        # if not in fort
        else:
            # moves diagonally
            if column_diff >= 1 and row_diff >= 1:
                return False
            # move vertically
            if self._curr_column == move_to_col:
                if move_to_row < self._curr_row:  # bottom to top
                    for row in range(move_to_row + 1, self._curr_row):  # look in between rows
                        current_piece = board[row][self._curr_column]
                        if current_piece == empty_space:
                            row += 1
                        else:
                            return False
                    return True
                elif move_to_row > self._curr_row:  # top to bottom
                    for row in range(self._curr_row + 1, move_to_row):  # look in between rows
                        current_piece = board[row][self._curr_column]
                        if current_piece == empty_space:
                            row += 1
                        else:
                            return False
                    return True

            # move horizontally
            if self._curr_row == move_to_row:
                if ord(move_to_col) < ord(self._curr_column):  # move right to left
                    for col in range(ord(move_to_col) + 1, ord(self._curr_column)):  # iterate in between columns
                        current_piece = board[self._curr_row][chr(col)]
                        if current_piece == empty_space:
                            col += 1
                        else:
                            return False
                    return True
                elif ord(move_to_col) > ord(self._curr_column):  # move left to right
                    for col in range(ord(self._curr_column) + 1, ord(move_to_col)):  # iterate in between columns
                        current_piece = board[self._curr_row][chr(col)]
                        if current_piece == empty_space:
                            col += 1
                        else:
                            return False
                    return True


class Horse(Piece):
    """represents a horse piece and inherits from Pieces class """

    def __init__(self, curr_row, curr_column):
        """initializes pieces for janggi
        :param curr_row: current corresponding row of piece on board
        :param curr_column: current column of piece on board"""
        super().__init__(curr_row, curr_column)

    def valid_move(self, move_to_row, move_to_col, board):
        """ first calls check_move_legal_legal from Pieces ( parent class) for initial check on moves that are common to all pieces,
        if check_move_legal returns True, valid_moves checks to see if a move is valid by passing in values from the
        make_move method in the Janggi Game class
        :param move_to_row: is a string that represents the row to move to
        :param move_to_col: is an index that represents the column to move to
        :param board: passes in the current board prior to making move
        :returns True if the piece has a valid move:
                - 1 space forward or backward, 1 space diagonal
                - 1 space to either side, 1 space diagonal
                - can NOT jump over pieces like a knight (chess), thus check for block
                Otherwise, False:
                - move is invalid
                - other piece is blocking move"""

        initial_move_legal = super(Horse, self).check_move_legal(move_to_row, move_to_col, board)
        column_diff = abs(ord(self._curr_column) - ord(move_to_col))
        row_diff = abs(self._curr_row - move_to_row)
        empty_space = {"": ""}
        # return True if current = move (indicates a pass)
        if self.get_current_location() == self.obtain_move_space(move_to_row, move_to_col):
            return True
        # validate common moves in Pieces
        if not initial_move_legal:
            return False

        # space fwd only
        if column_diff == 0 and row_diff >= 1:
            return False
        # 1 space diagonal
        if column_diff == 1 and row_diff == 1:
            return False
        # move diagonal more than 1 space
        if column_diff >= 2 and row_diff >= 2:
            return False
        if column_diff == 1 and row_diff == 3:
            return False

        # move 1 space fwd or backwards and 1 space to the right or left
        if row_diff == 2 and column_diff == 1:
            if self._curr_row > move_to_row:  # bottom to top
                # check spaces along move are empty, piece cannot jump
                row_fwd = self._curr_row - 1
                move_fwd = board[row_fwd][self._curr_column]
                if move_fwd == empty_space:
                    return True
            elif self._curr_row < move_to_row:  # top to bottom
                # check spaces along move are empty, piece cannot jump
                row_fwd = self._curr_row + 1
                move_fwd = board[row_fwd][self._curr_column]
                if move_fwd == empty_space:
                    return True

        # move 1 space to the side and 1 space to the right or left diagonally
        if row_diff == 1 and column_diff == 2:
            if ord(self._curr_column) > ord(move_to_col):  # right to left
                # check spaces along move are empty, piece cannot jump
                column_side = ord(self._curr_column) - 1
                move_fwd = board[self._curr_row][chr(column_side)]
                if move_fwd == empty_space:
                    return True
            elif ord(self._curr_column) < ord(move_to_col):  # left to right
                # check spaces along move are empty, piece cannot jump
                column_side = ord(self._curr_column) + 1
                move_fwd = board[self._curr_row][chr(column_side)]
                if move_fwd == empty_space:
                    return True


class Elephant(Piece):
    """represents an elephant piece and inherits from Pieces class """

    def __init__(self, curr_row, curr_column):
        """initializes pieces for janggi
        :param curr_row: current corresponding row of piece on board
        :param curr_column: current column of piece on board"""
        super().__init__(curr_row, curr_column)

    def valid_move(self, move_to_row, move_to_col, board):
        """ first calls check_move_legal from Pieces (parent class) for initial check on moves that are common to all pieces,
        if check_move_legal returns True, valid_moves checks to see if a move is valid by passing in values from the
        make_move method in the Janggi Game class
        :param move_to_row: is a string that represents the row to move to
        :param move_to_col: is an index that represents the column to move to
        :param board: passes in the current board prior to making move
        :returns True if the piece has a valid move:
                - 1 space forward or backward, 2 spaces diagonal
                - 1 space either side, then 2 spaces diagonal
                - can NOT jump over pieces like a knight (chess), thus check for block
                Otherwise,  False:
                - move is invalid
                - piece is blocking elephant"""
        initial_move_legal = super(Elephant, self).check_move_legal(move_to_row, move_to_col, board)
        empty_space = {"": ""}
        column_diff = abs(ord(self._curr_column) - ord(move_to_col))
        row_diff = abs(self._curr_row - move_to_row)

        # return True if current = move (indicates a pass)
        if self.get_current_location() == self.obtain_move_space(move_to_row, move_to_col):
            return True
        # validate common moves in Pieces
        if not initial_move_legal:
            return False

        # moves only 1 or less space
        if column_diff < 2 and row_diff < 2:
            return False
        # moves too many spaces
        if column_diff > 3 and row_diff > 3:
            return False

        # move 1 space fwd or backwards and 2 space to the right or left diagonally
        if row_diff == 3 and column_diff == 2:
            if self._curr_row > move_to_row:  # bottom to top
                row_fwd = self._curr_row - 1  # gets 1 space forward or backward
                move_fwd = board[row_fwd][self._curr_column]
                if ord(self._curr_column) > ord(move_to_col):  # right to left
                    # check spaces along move are empty, piece cannot jump
                    diag_row = self._curr_row - 2
                    diag_col = ord(self._curr_column) - 1
                    move_diag = board[diag_row][chr(diag_col)]
                    if move_fwd == empty_space and move_diag == empty_space:
                        return True
                elif ord(self._curr_column) < ord(move_to_col):  # left to right
                    # check spaces along move are empty, piece cannot jump
                    diag_row = self._curr_row - 2
                    diag_col = ord(self._curr_column) + 1
                    move_diag = board[diag_row][chr(diag_col)]
                    if move_fwd == empty_space and move_diag == empty_space:
                        return True

            elif self._curr_row < move_to_row:  # top to bottom
                row_fwd = self._curr_row + 1  # gets 1 space forward or backward
                move_fwd = board[row_fwd][self._curr_column]
                if ord(self._curr_column) > ord(move_to_col):  # right to left
                    # check spaces along move are empty, piece cannot jump
                    diag_row = self._curr_row + 2
                    diag_col = ord(self._curr_column) - 1
                    move_diag = board[diag_row][chr(diag_col)]
                    if move_fwd == empty_space and move_diag == empty_space:
                        return True
                elif ord(self._curr_column) < ord(move_to_col):  # left to right
                    # check spaces along move are empty, piece cannot jump
                    diag_row = self._curr_row + 2
                    diag_col = ord(self._curr_column) + 1
                    move_diag = board[diag_row][chr(diag_col)]
                    if move_fwd == empty_space and move_diag == empty_space:
                        return True

        # move 1 space to the side and 2 space to the right or left diagonally
        if row_diff == 2 and column_diff == 3:
            if ord(self._curr_column) > ord(move_to_col):  # right to left
                column_side = ord(self._curr_column) - 1
                move_fwd = board[self._curr_row][chr(column_side)]
                if self._curr_row > move_to_row:  # bottom to top
                    # check spaces along move are empty, piece cannot jump
                    diag_row = self._curr_row - 1
                    diag_col = ord(self._curr_column) - 2
                    move_diag = board[diag_row][chr(diag_col)]
                    if move_fwd == empty_space and move_diag == empty_space:
                        return True
                elif self._curr_row < move_to_row:  # top to bottom
                    # check spaces along move are empty, piece cannot jump
                    diag_row = self._curr_row + 1
                    diag_col = ord(self._curr_column) - 2
                    move_diag = board[diag_row][chr(diag_col)]
                    if move_fwd == empty_space and move_diag == empty_space:
                        return True

            elif ord(self._curr_column) < ord(move_to_col):  # left to right
                # check spaces along move are empty, piece cannot jump
                column_side = ord(self._curr_column) + 1
                move_fwd = board[self._curr_row][chr(column_side)]
                if self._curr_row > move_to_row:  # bottom to top
                    diag_row = self._curr_row - 1
                    diag_col = ord(self._curr_column) + 2
                    move_diag = board[diag_row][chr(diag_col)]
                    if move_fwd == empty_space and move_diag == empty_space:
                        return True
                elif self._curr_row < move_to_row:  # top to bottom
                    # check spaces along move are empty, piece cannot jump
                    diag_row = self._curr_row + 1
                    diag_col = ord(self._curr_column) - 2
                    move_diag = board[diag_row][chr(diag_col)]
                    if move_fwd == empty_space and move_diag == empty_space:
                        return True


class Guard(Piece):
    """"represents an advisor and inherits from Pieces class"""

    def __init__(self, curr_row, curr_column):
        """initializes pieces for janggi
        :param curr_row: current corresponding row of piece on board
        :param curr_column: current column of piece on board"""
        super().__init__(curr_row, curr_column)

    def valid_move(self, move_to_row, move_to_col, board):
        """ first calls check_move_legal from Pieces (parent class) for initial check on moves that are common to all pieces,
        if check_move_legal returns True, valid_moves checks to see if a move is valid by passing in values from the
        make_move method in the Janggi Game class
        :param move_to_row: is a string that represents the row to move to
        :param move_to_col: is an index that represents the column to move to
        :param board: passes in the current board prior to making move
        :returns True if the piece has a valid move:
                - 1 space along the lines within the fort (forward, backward, diagonal)
                Otherwise,  False:
                - move is invalid
                - piece is out of bounds of the fort"""

        initial_move_legal = super(Guard, self).check_move_legal(move_to_row, move_to_col, board)
        color = super(Guard, self).obtain_color(board)
        curr_location = super(Guard, self).get_current_location()
        red_fort = super(Guard, self).red_fort()
        blue_fort = super(Guard, self).blue_fort()
        move_to = super(Guard, self).obtain_move_space(move_to_row, move_to_col)

        column_diff = abs(ord(self._curr_column) - ord(move_to_col))
        row_diff = abs(self._curr_row - move_to_row)

        # return True if current = move (indicates a pass)
        if self.get_current_location() == self.obtain_move_space(move_to_row, move_to_col):
            return True
        # validate common moves in Pieces
        if not initial_move_legal:
            return False

        # cannot move diagonal more than one space
        if column_diff > 1 or row_diff > 1:
            return False

        # check if Guard is in his Fort and if move space is within the bounds of the Fort
        if color == "red":
            if curr_location not in red_fort:
                return False
            if move_to not in red_fort:
                return False

        elif color == "blue":
            if curr_location not in blue_fort:
                return False
            if move_to not in blue_fort:
                return False
        return True


class General(Piece):
    """represents a general and inherits from Pieces class"""

    def __init__(self, curr_row, curr_column):
        """initializes pieces for janggi
        :param curr_row: current corresponding row of piece on board
        :param curr_column: current column of piece on board"""
        super().__init__(curr_row, curr_column)

    def valid_move(self, move_to_row, move_to_col, board):
        """ first calls check_move_legal from Pieces (parent class) for initial check on moves that are common to all pieces,
        if check_move_legal returns True, valid_moves checks to see if a move is valid by passing in values from the
        make_move method in the Janggi Game class
        :param move_to_row: is a string that represents the row to move to
        :param move_to_col: is an index that represents the column to move to
        :param board: passes in the current board prior to making move
        :returns True if the piece has a valid move:
                - 1 space along the lines within the fort (forward, backward, diagonal)
                Otherwise,  False:
                - move is invalid
                - move is out of bounds of the fort"""
        initial_move_legal = super(General, self).check_move_legal(move_to_row, move_to_col, board)
        color = super(General, self).obtain_color(board)
        curr_location = super(General, self).get_current_location()
        red_fort = super(General, self).red_fort()
        blue_fort = super(General, self).blue_fort()
        move_to = super(General, self).obtain_move_space(move_to_row, move_to_col)

        column_diff = abs(ord(self._curr_column) - ord(move_to_col))
        row_diff = abs(self._curr_row - move_to_row)

        # return True if current = move (indicates a pass)
        if self.get_current_location() == self.obtain_move_space(move_to_row, move_to_col):
            return True
        # validate common moves in Pieces
        if not initial_move_legal:
            return False

        # cannot move diagonal more than one space
        if column_diff > 1 or row_diff > 1:
            return False

        # check if General is in his Fort and if move space is within the bounds of the Fort
        if color == "red":
            if curr_location not in red_fort:
                return False
            if move_to not in red_fort:
                return False

        elif color == "blue":
            if curr_location not in blue_fort:
                return False
            if move_to not in blue_fort:
                return False
        return True


class JanggiGame:
    """represents Janggi - a Korean version of chess"""

    def __init__(self):
        """initializes private data members:
        board as a dictionary, player's turn, current state of the game, status of check for blue and red players,
        and calls set_up_board to place initial pieces
        """
        self._board = {
            1: {"a": {"": ""}, "b": {"": ""}, "c": {"": ""}, "d": {"": ""}, "e": {"": ""}, "f": {"": ""}, "g": {"": ""},
                "h": {"": ""}, "i": {"": ""}},
            2: {"a": {"": ""}, "b": {"": ""}, "c": {"": ""}, "d": {"": ""}, "e": {"": ""}, "f": {"": ""}, "g": {"": ""},
                "h": {"": ""}, "i": {"": ""}},
            3: {"a": {"": ""}, "b": {"": ""}, "c": {"": ""}, "d": {"": ""}, "e": {"": ""}, "f": {"": ""}, "g": {"": ""},
                "h": {"": ""}, "i": {"": ""}},
            4: {"a": {"": ""}, "b": {"": ""}, "c": {"": ""}, "d": {"": ""}, "e": {"": ""}, "f": {"": ""}, "g": {"": ""},
                "h": {"": ""}, "i": {"": ""}},
            5: {"a": {"": ""}, "b": {"": ""}, "c": {"": ""}, "d": {"": ""}, "e": {"": ""}, "f": {"": ""}, "g": {"": ""},
                "h": {"": ""}, "i": {"": ""}},
            6: {"a": {"": ""}, "b": {"": ""}, "c": {"": ""}, "d": {"": ""}, "e": {"": ""}, "f": {"": ""}, "g": {"": ""},
                "h": {"": ""}, "i": {"": ""}},
            7: {"a": {"": ""}, "b": {"": ""}, "c": {"": ""}, "d": {"": ""}, "e": {"": ""}, "f": {"": ""}, "g": {"": ""},
                "h": {"": ""}, "i": {"": ""}},
            8: {"a": {"": ""}, "b": {"": ""}, "c": {"": ""}, "d": {"": ""}, "e": {"": ""}, "f": {"": ""}, "g": {"": ""},
                "h": {"": ""}, "i": {"": ""}},
            9: {"a": {"": ""}, "b": {"": ""}, "c": {"": ""}, "d": {"": ""}, "e": {"": ""}, "f": {"": ""}, "g": {"": ""},
                "h": {"": ""}, "i": {"": ""}},
            10: {"a": {"": ""}, "b": {"": ""}, "c": {"": ""}, "d": {"": ""}, "e": {"": ""}, "f": {"": ""},
                 "g": {"": ""}, "h": {"": ""}, "i": {"": ""}}}
        self._current_state = "UNFINISHED"  # "RED_WON", "BLUE_WON", or "UNFINISHED"
        self._blue_in_check = False
        self._red_in_check = False
        self.set_up_board()
        self._turn = "blue"  # blue goes first
        self._captured = []  # list of pieces no longer in play
        self._red_gen_location = (
            2, "e")  # get piece with self._board[self._red_gen_location[0]][self._red_gen_location[1]]
        self._blue_gen_location = (
            9, "e")  # get piece with self._board[self._blue_gen_location[0]][self._blue_gen_location[1]]

    def set_up_board(self):
        """places pieces in their initial positions"""
        # red pieces
        self._board[2]["e"] = {"red": "gen"}
        self._board[1]["a"] = {"red": "char"}
        self._board[1]["b"] = {"red": "ele"}
        self._board[1]["c"] = {"red": "hor"}
        self._board[1]["d"] = {"red": "guard"}
        self._board[1]["f"] = {"red": "guard"}
        self._board[1]["g"] = {"red": "ele"}
        self._board[1]["h"] = {"red": "hor"}
        self._board[1]["i"] = {"red": "char"}
        self._board[3]["b"] = {"red": "can"}
        self._board[3]["h"] = {"red": "can"}
        self._board[4]["a"] = {"red": "sold"}
        self._board[4]["c"] = {"red": "sold"}
        self._board[4]["e"] = {"red": "sold"}
        self._board[4]["g"] = {"red": "sold"}
        self._board[4]["i"] = {"red": "sold"}
        # blue pieces
        self._board[9]["e"] = {"blue": "gen"}
        self._board[10]["a"] = {"blue": "char"}
        self._board[10]["b"] = {"blue": "ele"}
        self._board[10]["c"] = {"blue": "hor"}
        self._board[10]["d"] = {"blue": "guard"}
        self._board[10]["f"] = {"blue": "guard"}
        self._board[10]["g"] = {"blue": "ele"}
        self._board[10]["h"] = {"blue": "hor"}
        self._board[10]["i"] = {"blue": "char"}
        self._board[8]["b"] = {"blue": "can"}
        self._board[8]["h"] = {"blue": "can"}
        self._board[7]["a"] = {"blue": "sold"}
        self._board[7]["c"] = {"blue": "sold"}
        self._board[7]["e"] = {"blue": "sold"}
        self._board[7]["g"] = {"blue": "sold"}
        self._board[7]["i"] = {"blue": "sold"}

    def get_game_state(self):
        """ gets current state of the game
        :returns
        returns current state of the game as "RED_WON", "BLUE_WON", or "UNFINISHED"""
        return self._current_state

    def get_red_gen_loc(self):
        """ gets red general's location
        :returns
        returns board location of red general"""
        return self._red_gen_location

    def get_blue_gen_loc(self):
        """ gets blue general's location
        :returns
        returns board location of blue general"""
        return self._blue_gen_location

    def is_in_check(self, color):
        """checks if the current player's general is in check by iterating through valid moves that could capture the
        general"
        :param color is the general's color
        :returns
        Returns True if either player is in check, otherwise returns False.
        Sets the "color"_in_check to True if in check, otherwise it remains as False.
        """
        # checks if red general is in check
        if color == "red":
            # iterate through all blue players who may have a chance to capture the general
            for row in range(1, 11):
                for col in range(ord("a"), ord("j")):
                    blue_piece_at_play = self._board[row][chr(col)]
                    for key in blue_piece_at_play.keys():
                        if key == "blue" and blue_piece_at_play:
                            # get coordinates of the current blue piece in loop
                            piece = Piece(row, chr(col))
                            current_coordinates = piece.get_current_location()
                            # call can_capture_general, continue iterating if false (no check)
                            if not self.can_capture_general(blue_piece_at_play, current_coordinates):
                                col += 1
                            else:
                                return True
        # check if blue general is in check
        elif color == "blue":
            # iterate through all red players who may have a chance to capture the general
            for row in range(1, 11):
                for col in range(ord("a"), ord("j")):
                    red_piece_at_play = self._board[row][chr(col)]
                    for key in red_piece_at_play.keys():
                        if key == "red" and red_piece_at_play:
                            # get coordinates of the current red piece in loop
                            piece = Piece(row, chr(col))
                            current_coordinates = piece.get_current_location()
                            # call can_capture_general, continue iterating if false (no check)
                            if not self.can_capture_general(red_piece_at_play, current_coordinates):
                                col += 1
                            else:
                                return True
        return False

    def can_capture_general(self, piece, coord):
        """helper method called by is_in_check that determines if a piece has a valid move to capture the general
        :param piece: current piece at place (i.e, {"red": "char")
        :param coord: coordinates of the piece as a tuple
        :returns True if piece has a valid move to capture the general. Otherwise, returns False"""

        # see if red can capture blue general, calling valid moves checks current location of the general
        if piece == {"red": "char"}:
            chariot = Chariot(coord[0], coord[1])
            if chariot.valid_move(self._blue_gen_location[0], self._blue_gen_location[1], self._board):
                return True
        elif piece == {"red": "ele"}:
            elephant = Elephant(coord[0], coord[1])
            if elephant.valid_move(self._blue_gen_location[0], self._blue_gen_location[1], self._board):
                return True
        elif piece == {"red": "hor"}:
            horse = Horse(coord[0], coord[1])
            if horse.valid_move(self._blue_gen_location[0], self._blue_gen_location[1], self._board):
                return True
        elif piece == {"red": "guard"}:
            guard = Guard(coord[0], coord[1])
            if guard.valid_move(self._blue_gen_location[0], self._blue_gen_location[1], self._board):
                return True
        elif piece == {"red": "can"}:
            cannon = Cannon(coord[0], coord[1])
            if cannon.valid_move(self._blue_gen_location[0], self._blue_gen_location[1], self._board):
                return True
        elif piece == {"red": "sold"}:
            soldier = Soldier(coord[0], coord[1])
            if soldier.valid_move(self._blue_gen_location[0], self._blue_gen_location[1], self._board):
                return True

        # see if blue can capture red general, calling valid moves checks current location of the general
        elif piece == {"blue": "ele"}:
            elephant = Elephant(coord[0], coord[1])
            if elephant.valid_move(self._red_gen_location[0], self._red_gen_location[1], self._board):
                return True
        elif piece == {"blue": "hor"}:
            horse = Horse(coord[0], coord[1])
            if horse.valid_move(self._red_gen_location[0], self._red_gen_location[1], self._board):
                return True
        elif piece == {"blue": "guard"}:
            guard = Guard(coord[0], coord[1])
            if guard.valid_move(self._red_gen_location[0], self._red_gen_location[1], self._board):
                return True
        elif piece == {"blue": "can"}:
            cannon = Cannon(coord[0], coord[1])
            if cannon.valid_move(self._red_gen_location[0], self._red_gen_location[1], self._board):
                return True
        elif piece == {"blue": "sold"}:
            soldier = Soldier(coord[0], coord[1])
            if soldier.valid_move(self._red_gen_location[0], self._red_gen_location[1], self._board):
                return True

    def move_puts_general_in_check(self, current_place_dict, move_to_dict):
        """helper method called by make_move that determines if the move to be made by player will put it's
        own general in check
        :param current_place_dict: tuple of current position of the board
        :param move_to_dict: tuple of position to move to
        :returns True if the current's player's general will be in check if move is made. Otherwise, returns False."""

        # move piece to test if it will put it's own general in check
        piece = self._board[current_place_dict[0]][current_place_dict[1]]
        captured = self._board[move_to_dict[0]][move_to_dict[1]]
        self._board[move_to_dict[0]][move_to_dict[1]] = piece
        self._board[current_place_dict[0]][current_place_dict[1]] = {"": ""}

        # set piece to move location in order to test if the move will put the general in check
        # red pieces
        if piece == {"red": "gen"}:
            general = General(None, None)
            general.set_location(move_to_dict[0], move_to_dict[1])
        elif piece == {"red": "char"}:
            chariot = Chariot(None, None)
            chariot.set_location(move_to_dict[0], move_to_dict[1])
        elif piece == {"red": "ele"}:
            elephant = Elephant(None, None)
            elephant.set_location(move_to_dict[0], move_to_dict[1])
        elif piece == {"red": "hor"}:
            horse = Horse(None, None)
            horse.set_location(move_to_dict[0], move_to_dict[1])
        elif piece == {"red": "guard"}:
            guard = Guard(None, None)
            guard.set_location(move_to_dict[0], move_to_dict[1])
        elif piece == {"red": "can"}:
            cannon = Cannon(None, None)
            cannon.set_location(move_to_dict[0], move_to_dict[1])
        elif piece == {"red": "sold"}:
            soldier = Soldier(None, None)
            soldier.set_location(move_to_dict[0], move_to_dict[1])
        # blue pieces
        if piece == {"blue": "gen"}:
            general = General(None, None)
            general.set_location(move_to_dict[0], move_to_dict[1])
        elif piece == {"blue": "char"}:
            chariot = Chariot(None, None)
            chariot.set_location(move_to_dict[0], move_to_dict[1])
        elif piece == {"blue": "ele"}:
            elephant = Elephant(None, None)
            elephant.set_location(move_to_dict[0], move_to_dict[1])
        elif piece == {"blue": "hor"}:
            horse = Horse(None, None)
            horse.set_location(move_to_dict[0], move_to_dict[1])
        elif piece == {"blue": "guard"}:
            guard = Guard(None, None)
            guard.set_location(move_to_dict[0], move_to_dict[1])
        elif piece == {"blue": "can"}:
            cannon = Cannon(None, None)
            cannon.set_location(move_to_dict[0], move_to_dict[1])
        elif piece == {"blue": "sold"}:
            soldier = Soldier(None, None)
            soldier.set_location(move_to_dict[0], move_to_dict[1])

        # call is_in_check to see if the move puts the general in check
        puts_piece_in_check = self.is_in_check(self._turn)

        # reset pieces back to original positions
        if piece == {"red": "gen"}:
            general = General(None, None)
            general.set_location(current_place_dict[0], current_place_dict[1])
        elif piece == {"red": "char"}:
            chariot = Chariot(None, None)
            chariot.set_location(current_place_dict[0], current_place_dict[1])
        elif piece == {"red": "ele"}:
            elephant = Elephant(None, None)
            elephant.set_location(current_place_dict[0], current_place_dict[1])
        elif piece == {"red": "hor"}:
            horse = Horse(None, None)
            horse.set_location(current_place_dict[0], current_place_dict[1])
        elif piece == {"red": "guard"}:
            guard = Guard(None, None)
            guard.set_location(current_place_dict[0], current_place_dict[1])
        elif piece == {"red": "can"}:
            cannon = Cannon(None, None)
            cannon.set_location(current_place_dict[0], current_place_dict[1])
        elif piece == {"red": "sold"}:
            soldier = Soldier(None, None)
            soldier.set_location(current_place_dict[0], current_place_dict[1])
        if piece == {"blue": "gen"}:
            general = General(None, None)
            general.set_location(move_to_dict[0], move_to_dict[1])
        elif piece == {"blue": "char"}:
            chariot = Chariot(None, None)
            chariot.set_location(current_place_dict[0], current_place_dict[1])
        elif piece == {"blue": "ele"}:
            elephant = Elephant(None, None)
            elephant.set_location(current_place_dict[0], current_place_dict[1])
        elif piece == {"blue": "hor"}:
            horse = Horse(None, None)
            horse.set_location(current_place_dict[0], current_place_dict[1])
        elif piece == {"blue": "guard"}:
            guard = Guard(None, None)
            guard.set_location(current_place_dict[0], current_place_dict[1])
        elif piece == {"blue": "can"}:
            cannon = Cannon(None, None)
            cannon.set_location(current_place_dict[0], current_place_dict[1])
        elif piece == {"blue": "sold"}:
            soldier = Soldier(None, None)
            soldier.set_location(current_place_dict[0], current_place_dict[1])

        # set piece back to current position and return capture piece to the move_to position
        self._board[current_place_dict[0]][current_place_dict[1]] = piece
        self._board[move_to_dict[0]][move_to_dict[1]] = captured

        return puts_piece_in_check  # returns True or False

    def check_for_checkmate_and_update_game_state(self, color):
        """called by make move to determine if a checkmate has occurred by checking if the current player has any valid
        moves left
        :param color: color of current player's turn
        :returns False if player has a valid move left (gets them out of check), else calls update_game_state to
        set the winner and returns True"""

        list_of_red_coord = []  # stores the coordinates of red pieces currently on the board
        list_of_blue_coord = []  # stores the coordinates of red pieces currently on the board

        # check if red is in checkmate
        # get all of red player coordinates and append them to list by iterating through pieces on the board
        if color == "red":
            for row in range(1, 11):
                for col in range(ord("a"), ord("j")):
                    red_piece_at_play = self._board[row][chr(col)]
                    for key in red_piece_at_play.keys():
                        if key == "red":
                            piece = Piece(row, chr(col))
                            current_coordinates = piece.get_current_location()
                            list_of_red_coord.append(current_coordinates)

            # check each player from list for a valid move by iterating through every space to see if a move takes the
            # general out of check
            for index in list_of_red_coord:
                move_from = (index[0], index[1])
                for row in range(1, 11):
                    for col in range(ord("a"), ord("j")):
                        move_to = (row, chr(col))
                        # if a move is left that does not leave the general in check, return to make_move and keep
                        # state of game as unfinished, no checkmate
                        if not self.move_puts_general_in_check(move_from, move_to):
                            return False

            # if no available moves to get out of check, update to BLUE_WON and return True
            self.update_game_state()
            return True

        # check if blue is in checkmate
        # get all of blue player coordinates and append them to list by iterating through pieces on the board
        if color == "blue":
            for row in range(1, 11):
                for col in range(ord("a"), ord("j")):
                    blue_piece_at_play = self._board[row][chr(col)]
                    for key in blue_piece_at_play.keys():
                        if key == "blue":
                            piece = Piece(row, chr(col))
                            current_coordinates = piece.get_current_location()
                            list_of_blue_coord.append(current_coordinates)

            # check each player from list for a valid move by iterating through every space to see if a move takes the
            # general out of check
            for index in list_of_blue_coord:
                move_from = (index[0], index[1])
                for row in range(1, 11):
                    for col in range(ord("a"), ord("j")):
                        move_to = (row, chr(col))
                        # if a move is left that does not leave the general in check, return to make_move and keep
                        # state of game as unfinished, no checkmate
                        if not self.move_puts_general_in_check(move_from, move_to):
                            return False

            # if no available moves to get out of check, update to RED_WON and return True
            self.update_game_state()
            return True

    def update_game_state(self):
        """helper function called by check_for_checkmate_and_update_game_state;
        updates the current state of the game if checkmate is True"""
        if self._turn == "red":
            self._current_state = "BLUE_WON"
        elif self._turn == "blue":
            self._current_state = "RED_WON"

    def make_move(self, current_place, move_to):
        """
        :param current_place is a string that represents the square to move from
        :param move_to is a string that represents the square to move to

        :returns
        Returns False if the square being moved from does not contain a piece belonging to the player whose turn it is,
        if the move is illegal, or if the game is already won.
        Otherwise, it makes the move, removes any captured piece, updates the game state (if necessary),
        updates whose turn it is, and returns True.
        If the same string is passed for current_place and move_to, the player is passing their turn, and thus this also
        returns True.
        """

        if self._current_state != "UNFINISHED":
            return False

        # convert input to dictionary value
        current_place_dict = self.convert_to_row_column(current_place)
        move_to_dict = self.convert_to_row_column(move_to)

        # set current board position
        current_board_position = self._board[current_place_dict[0]][current_place_dict[1]]

        # no piece to move on current space
        if current_board_position == {"": ""}:
            return False

        # get value (piece name) from key (color)
        for key in current_board_position.keys():
            # check turn
            if key == "red" and key != self._turn:
                return False
            if key == "red" and self._turn == "red":
                # piece equals current piece (value) at key
                red_piece = current_board_position["red"]
                if red_piece == "gen":
                    # check for valid move
                    general = General(current_place_dict[0], current_place_dict[1])
                    if not general.valid_move(move_to_dict[0], move_to_dict[1], self._board):
                        return False
                    # if valid...
                    else:
                        # set general to move location
                        self._red_gen_location = move_to_dict[0], move_to_dict[1]
                        # check checkmate status, if in checkmate return True so player can't make move
                        if self.check_for_checkmate_and_update_game_state("red"):
                            return False
                        # check if move puts own general in check
                    if self.move_puts_general_in_check(current_place_dict, move_to_dict):
                        # if true, set general back to current position
                        self._red_gen_location = current_board_position
                        return False
                    else:
                        # move general
                        self.move_piece(current_place_dict, move_to_dict)
                        # set the new location of the general
                        self._red_gen_location = move_to_dict
                    self._turn = "blue"
                elif red_piece == "char":
                    chariot = Chariot(current_place_dict[0], current_place_dict[1])
                    # check for valid move
                    if not chariot.valid_move(move_to_dict[0], move_to_dict[1], self._board):
                        return False
                    # if valid...
                    # check for checkmate
                    elif self.check_for_checkmate_and_update_game_state("red"):
                        return False
                        # check if move puts own general in check
                    elif self.move_puts_general_in_check(current_place_dict, move_to_dict):
                        return False
                    else:
                        # move piece
                        self.move_piece(current_place_dict, move_to_dict)
                    self._turn = "blue"
                elif red_piece == "ele":
                    elephant = Elephant(current_place_dict[0], current_place_dict[1])
                    if not elephant.valid_move(move_to_dict[0], move_to_dict[1], self._board):
                        return False
                    elif self.check_for_checkmate_and_update_game_state("red"):
                        self.update_game_state()
                        return False
                    elif self.move_puts_general_in_check(current_place_dict, move_to_dict):
                        return False
                    else:
                        self.move_piece(current_place_dict, move_to_dict)
                    self._turn = "blue"
                elif red_piece == "hor":
                    horse = Horse(current_place_dict[0], current_place_dict[1])
                    if not horse.valid_move(move_to_dict[0], move_to_dict[1], self._board):
                        return False
                    elif self.check_for_checkmate_and_update_game_state("red"):
                        self.update_game_state()
                        return False
                    elif self.move_puts_general_in_check(current_place_dict, move_to_dict):
                        return False
                    else:
                        self.move_piece(current_place_dict, move_to_dict)
                    self._turn = "blue"
                elif red_piece == "guard":
                    guard = Guard(current_place_dict[0], current_place_dict[1])
                    if not guard.valid_move(move_to_dict[0], move_to_dict[1], self._board):
                        return False
                    elif self.check_for_checkmate_and_update_game_state("red"):
                        return False
                    elif self.move_puts_general_in_check(current_place_dict, move_to_dict):
                        return False
                    else:
                        self.move_piece(current_place_dict, move_to_dict)  # move piece
                    self._turn = "blue"
                elif red_piece == "can":
                    cannon = Cannon(current_place_dict[0], current_place_dict[1])
                    if not cannon.valid_move(move_to_dict[0], move_to_dict[1], self._board):
                        return False
                    elif self.check_for_checkmate_and_update_game_state("red"):
                        return False
                    elif self.move_puts_general_in_check(current_place_dict, move_to_dict):
                        return False
                    else:
                        self.move_piece(current_place_dict, move_to_dict)  # move piece
                    self._turn = "blue"
                elif red_piece == "sold":
                    soldier = Soldier(current_place_dict[0], current_place_dict[1])
                    if not soldier.valid_move(move_to_dict[0], move_to_dict[1], self._board):
                        return False
                    elif self.check_for_checkmate_and_update_game_state("red"):
                        return False
                    elif self.move_puts_general_in_check(current_place_dict, move_to_dict):
                        return False
                    else:
                        self.move_piece(current_place_dict, move_to_dict)  # move piece
                    self._turn = "blue"

            # blue's turn
            else:
                if key == "blue" and key != self._turn:
                    return False
                blue_piece = current_board_position["blue"]
                if blue_piece == "gen":
                    # check if move is valid
                    general = General(current_place_dict[0], current_place_dict[1])
                    if not general.valid_move(move_to_dict[0], move_to_dict[1], self._board):
                        return False
                    else:
                        # set general location to move location
                        self._blue_gen_location = move_to_dict[0], move_to_dict[1]
                        # check for checkmate
                        if self.check_for_checkmate_and_update_game_state("blue"):
                            return False
                        # check if move puts own general in check
                    if self.move_puts_general_in_check(current_place_dict, move_to_dict):
                        # if true, set back to current position
                        self._red_gen_location = current_board_position
                        return False
                    else:
                        # move piece
                        self.move_piece(current_place_dict, move_to_dict)
                        # set the new location of the general
                        self._blue_gen_location = move_to_dict
                    self._turn = "red"
                elif blue_piece == "char":
                    # check if move is valid
                    chariot = Chariot(current_place_dict[0], current_place_dict[1])
                    if not chariot.valid_move(move_to_dict[0], move_to_dict[1], self._board):
                        return False
                        # check for checkmate
                    elif self.check_for_checkmate_and_update_game_state("blue"):
                        return False
                        # check if move puts own general in check
                    elif self.move_puts_general_in_check(current_place_dict, move_to_dict):
                        return False
                    else:
                        # move piece
                        self.move_piece(current_place_dict, move_to_dict)
                    self._turn = "red"
                elif blue_piece == "ele":
                    elephant = Elephant(current_place_dict[0], current_place_dict[1])
                    if not elephant.valid_move(move_to_dict[0], move_to_dict[1], self._board):
                        return False
                    elif self.check_for_checkmate_and_update_game_state("blue"):
                        return False
                    elif self.move_puts_general_in_check(current_place_dict, move_to_dict):
                        return False
                    else:
                        self.move_piece(current_place_dict, move_to_dict)
                    self._turn = "red"
                elif blue_piece == "hor":
                    horse = Horse(current_place_dict[0], current_place_dict[1])
                    if not horse.valid_move(move_to_dict[0], move_to_dict[1], self._board):
                        return False
                    elif self.check_for_checkmate_and_update_game_state("blue"):
                        return False
                    elif self.move_puts_general_in_check(current_place_dict, move_to_dict):
                        return False
                    else:
                        self.move_piece(current_place_dict, move_to_dict)
                    self._turn = "red"
                elif blue_piece == "guard":
                    guard = Guard(current_place_dict[0], current_place_dict[1])
                    if not guard.valid_move(move_to_dict[0], move_to_dict[1], self._board):
                        return False
                    elif self.check_for_checkmate_and_update_game_state("blue"):
                        return False
                    elif self.move_puts_general_in_check(current_place_dict, move_to_dict):
                        return False
                    else:
                        self.move_piece(current_place_dict, move_to_dict)
                    self._turn = "red"
                elif blue_piece == "can":
                    cannon = Cannon(current_place_dict[0], current_place_dict[1])
                    if not cannon.valid_move(move_to_dict[0], move_to_dict[1], self._board):
                        return False
                    elif self.check_for_checkmate_and_update_game_state("blue"):
                        return False
                    elif self.move_puts_general_in_check(current_place_dict, move_to_dict):
                        return False
                    else:
                        self.move_piece(current_place_dict, move_to_dict)
                    self._turn = "red"
                elif blue_piece == "sold":
                    soldier = Soldier(current_place_dict[0], current_place_dict[1])
                    if not soldier.valid_move(move_to_dict[0], move_to_dict[1], self._board):
                        return False
                    elif self.check_for_checkmate_and_update_game_state("blue"):
                        return False
                    elif self.move_puts_general_in_check(current_place_dict, move_to_dict):
                        return False
                    else:
                        self.move_piece(current_place_dict, move_to_dict)
                    self._turn = "red"
            return True

    def move_piece(self, current_place_dict, move_to_dict):
        """helper method to move piece once move is validated in the make_move method,
        it also captures a piece and appends it to a captured list if the move to space contains an opponent's piece,
        and updates the current state of the game
        :param current_place_dict: tuple of current position of the board
        :param move_to_dict: tuple of position to move to"""
        clear_space = {"": ""}
        # set current board position of piece
        current_board_position = self._board[current_place_dict[0]][current_place_dict[1]]
        if self._board[move_to_dict[0]][move_to_dict[1]] != current_board_position:  # if move is not a "pass"
            # capture piece and move
            self._captured.append(self._board[move_to_dict[0]][move_to_dict[1]])
            # move and clear previous space
            self._board[move_to_dict[0]][move_to_dict[1]] = current_board_position
            self._board[current_place_dict[0]][current_place_dict[1]] = clear_space

    def convert_to_row_column(self, notation):
        """
        :param notation: algebraic notation such as "e2" that correlates to space on the board
        :returns row and column for indexing into the board
        :rtype: tuple
        """
        # example takes e2, and returns (2, "e") in order to index into dictionary
        return int(notation[1:]), notation[0]

    def print_board(self):
        """ prints the current board
        """
        for row_num, row in self._board.items():
            if row_num == 10:
                current_row = str(row_num)
            else:
                current_row = " " + str(row_num)
            for column in range(ord("a"), ord("j")):
                piece = row[chr(column)]
                current_row += " " + str(piece)
            print(current_row)
