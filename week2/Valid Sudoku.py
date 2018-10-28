class Solution:
    def listValid(self,l):
        basic=[i for i in range(1,10,1)]
        for i in l:
            if i.isdigit():
                if int(i) not in basic:
                    #print(i)
                    return False
                basic.remove(int(i))
        return True
    def rowValid(self,board):
        for row in board:
            if not self.listValid(row):
                return False
        return True
    def colValid(self,board):
        for col in range(len(board[0])):
            colList=[]
            for row in board:
                colList+=row[col]
            if not self.listValid(colList):
                return False
        return True
    def cellValid(self,board):
        for r in range(0,len(board),3):
            for c in range(0,len(board[0]),3):
                cellList=[]
                for i in range(3):
                    for j in range(3):
                        cellList+=board[r+i][c+j]
                if not self.listValid(cellList):
                    return False
        return True
    def isValidSudoku(self, board):


        return self.rowValid(board) and self.colValid(board) and self.cellValid(board)
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
