class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_count=defaultdict()
        column_count=defaultdict() 
        square_count=defaultdict()
        #for each row: create an array of 9 digits and see if there are duplicates
        for i,row in enumerate(board):
            row_embedd=[0]*9
            for j,col in enumerate(row):
                if ord(col)-ord('0')>0:
                    row_embedd[ord(col)-ord('0')-1]+=1
            row_count[i]=row_embedd

        column_board=[list(row) for row in zip(*board)]
        for i,row in enumerate(column_board):
            col_embedd=[0]*9
            for j,col in enumerate(row):
                if ord(col)-ord('0')>0:
                    col_embedd[ord(col)-ord('0')-1]+=1 
            column_count[i]=col_embedd
        
        for i in range(9):
            square_count[i]=[]
        sqaure_board=[['']*9]*9
        for i,row in enumerate(board):
            for j,col in enumerate(row):
                square_number=(int(i/3)*3)+int(j/3)
                square_count[square_number].append(col)
        
        square_board=list(square_count.values())
        for i,row in enumerate(square_board):
            sqaure_embedd=[0]*9
            for j,col in enumerate(row):
                if ord(col)-ord('0')>0:
                    sqaure_embedd[ord(col)-ord('0')-1]+=1
            square_count[i]=sqaure_embedd 

        sudoku=True
        row_counter=list(row_count.values())
        for i in row_counter:
            for j in i:
                if j>1:
                    sudoku=False
        col_counter=list(column_count.values())
        for i in col_counter:
            for j in i:
                if j>1:
                    sudoku=False
        sq_counter=list(square_count.values())
        for i in sq_counter:
            for j in i:
                if j>1:
                    sudoku=False
        return(sudoku)
         
         
            
       




        #for each column: create an array of 9 digits iand find duplicates
        
        #for each square get the associated digit



        