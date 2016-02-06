class sudokuSolver:
    def __init__(self, sudoku):
        self.itt = 0

        self.load(sudoku)

        while not self.solved():
            self.solve()
        self.show()


    def solve(self):
        self.removeInvalidPosibilities()
        self.onePosibility()

    def removeInvalidPosibilities(self):
        for rowId, row in enumerate(self.sudoku):
            for columnId, field in enumerate(row):
                self.checkPosibilities(rowId, columnId)

    def checkPosibilities(self, rowId, columnId):
        values = []
        row = self.sudoku[rowId]
        for field in row:
            values.append(field['val'])

        for row in self.sudoku:
            values.append(row[columnId]['val'])

        # column and row number of 3 by 3 block
        blockRowId      = int(rowId/3)
        blockColumnId   = int(columnId/3)

        for row in self.sudoku[blockRowId*3:blockRowId*3+3]:
            for field in row[blockColumnId*3:blockColumnId*3+3]:
                values.append(field['val'])

        posibilities = self.sudoku[rowId][columnId]['posibilities']
        posibilities = [x for x in posibilities if x not in values]
        self.sudoku[rowId][columnId]['posibilities'] = posibilities
        return posibilities

    def onePosibility(self):
        for row in self.sudoku:
            for field in row:
                if field['val'] == None and len(field['posibilities']) == 1:
                    field['val'] = field['posibilities'][0]


    def load(self, sudoku):
        sudokuObj = []
        for row in sudoku:
            rowObj = []
            for field in row:
                rowObj.append({
                    'val':field,
                    'posibilities': [1,2,3,4,5,6,7,8,9]
                })
            sudokuObj.append(rowObj)
        self.sudoku = sudokuObj

    def solved(self):
        self.itt += 1
        return self.itt > 5000

    def show(self):
        for row in self.sudoku:
            string = ''
            for field in row:
                if(not field['val'] == None):
                    string += str(field['val']) + ' '
                else:
                    string += '  '
            print(string)




sudoku = [
    [None,9,5,8,None,None,None,None,None],
    [4,None,None,None,None,6,9,8,None],
    [None,None,None,None,None,1,5,None,None],
    [None,None,7,None,None,None,None,5,None],
    [None,2,None,5,None,9,None,7,None],
    [None,5,None,None,None,None,8,None,None],
    [None,None,1,2,None,None,None,None,None],
    [None,8,4,6,None,None,None,None,9],
    [None,None,None,None,None,7,3,4,None]
]


# sudoku = [
#     [5,None,None,None,None,None,1,2,4],
#     [None,None,None,5,None,None,None,None,9],
#     [1,None,None,3,None,None,None,8,None],
#     [3,1,None,8,None,None,None,None,None],
#     [None,8,None,6,2,None,None,None,None],
#     [None,None,None,None,None,5,None,None,6],
#     [7,None,None,None,None,8,None,4,None],
#     [None,None,None,9,4,None,None,None,5],
#     [None,None,None,None,None,None,9,None,None],
# ]

solver = sudokuSolver(sudoku)
