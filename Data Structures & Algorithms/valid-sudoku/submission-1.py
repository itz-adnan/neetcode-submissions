class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows
        for row in board:
            seen = set()
            for i in row:
                if i in seen:
                    return False
                if i != ".":
                    seen.add(i)
        
        #check columns [0 to 8]
        for col in range(9):
            seen = set()
            for row in board:
                val = row[col]
                if val in seen:
                    return False
                if val != ".":
                    seen.add(val)
        
        #check boxes [0 to 8]
        for row_set in range(3):
            for col_set in range(3):
                seen = set()
                for i in range(3*row_set,3*row_set+3):
                    for j in range(3*col_set, 3*col_set+3):
                        if board[i][j] in seen:
                            return False
                        if board[i][j] != '.':
                            seen.add(board[i][j])
        
        return True #if it doesnt violate any rules, return True by default
        