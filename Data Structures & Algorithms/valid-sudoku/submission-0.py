class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        output = True
        for i in range(len(board)):
            seen = set()
            for a in board[i]:
                if a == ".":
                    continue
                if a in seen:
                    output = False

                seen.add(a)

        for i in range(len(board)):
            seen = set()
            for a in board:
                if a[i] == ".":
                    continue

                if a[i] in seen:
                    output = False

                seen.add(a[i])

        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                seen = set()
                for row in range(box_row, box_row + 3):
                    for col in range(box_col, box_col + 3):
                        if board[row][col] == ".":
                            continue
                        if board[row][col] in seen:
                            output = False
                        seen.add(board[row][col])
        return output
