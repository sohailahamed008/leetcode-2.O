class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows=[set() for _ in range(9)]
        cols=[set() for _ in range(9)]
        boxs=[[set() for _ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                val=board[i][j]
                if val =='.':
                    continue
                if val in rows[i]:
                    return False
                rows[i].add(val)

                if val in cols[j]:
                    return False
                cols[j].add(val)

                rb=i//3
                cb=j//3

                if val in boxs[rb][cb]:
                    return False
                boxs[rb][cb].add(val)

        return True


