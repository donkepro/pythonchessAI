'''
if self.whiteToMove:
    if self.board[r - 1][c] == '--':
        if not piecePinned or pinDirection == (-1, 0):
            moves.append(Move((r, c), (r - 1, c), self.board))
            if r == 6 and self.board[r - 2][c] == '--':
                moves.append(Move((r, c), (r - 2, c), self.board))

    if c - 1 >= 0:
        if self.board[r - 1][c - 1][0] == 'b':
            if not piecePinned or pinDirection == (-1, -1):
                moves.append(Move((r, c), (r - 1, c - 1), self.board))
    if c + 1 <= 7:
        if self.board[r - 1][c + 1][0] == 'b':
            if not piecePinned or pinDirection == (-1, 1):
                moves.append(Move((r, c), (r - 1, c + 1), self.board))
else:
    if self.board[r + 1][c] == '--':
        if not piecePinned or pinDirection == (1, 0):
            moves.append(Move((r, c), (r + 1, c), self.board))
            if r == 1 and self.board[r + 2][c] == '--':
                moves.append(Move((r, c), (r + 2, c), self.board))

    if c - 1 >= 0:
        if self.board[r + 1][c - 1][0] == 'b':
            if not piecePinned or pinDirection == (1, -1):
                moves.append(Move((r, c), (r + 1, c - 1), self.board))
    if c + 1 <= 7:
        if self.board[r + 1][c + 1][0] == 'b':
            if not piecePinned or pinDirection == (1, 1):
                moves.append(Move((r, c), (r + 1, c + 1), self.board))
'''