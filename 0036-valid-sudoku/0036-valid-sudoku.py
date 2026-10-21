class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows=[set () for row in range(9)]
        cols=[set() for col in range(9)]
        box=[[set() for i in range(3)]for j in range(3) ]

        for i in range(9):
            for j in range(9):
                val=board[i][j]
                if val=='.':
                    continue
                if val in rows[i]:
                    return False
                rows[i].add(val)

                if val in cols[j]:
                    return False
                cols[j].add(val)

                row=i//3
                col=j//3
                if  val in box[row][col]:
                    return False
                box[row][col].add(val)
        return True

        


