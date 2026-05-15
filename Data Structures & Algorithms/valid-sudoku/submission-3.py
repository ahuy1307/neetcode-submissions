class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[i][j] in seen:
                    return False

                if board[i][j] != ".":
                    seen.add(board[i][j])

        for i in range(9):
            seen = set()
            for j in range(9):
                if board[j][i] in seen:
                    return False

                if board[j][i] != ".":
                    seen.add(board[j][i])

        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    col = (square % 3) * 3 + j
                    row = (square // 3) * 3 + i

                    if board[col][row] in seen:
                        return False

                    if board[col][row] != ".":
                        seen.add(board[col][row])

        return True