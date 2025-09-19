class Spreadsheet():
    def __init__(self, rows):
        self.rows = rows
        self.grid = [[0]*26 for _ in range(rows)]
    
    def _parse_cell(self, cell):
        col = ord(cell[0]) - ord('A')
        row = int(cell[1:]) - 1
        return row, col
    
    def setCell(self, cell, value):
        row, col = self._parse_cell(cell)
        self.grid[row][col] = value

    def resetCell(self, cell):
        row, col = self._parse_cell(cell)
        self.grid[row][col] = 0

    def _get_operand_value(self, operand):
        if operand[0].isalpha():
            row, col = self._parse_cell(operand)
            return self.grid[row][col]
        else:
            return int(operand)

    def getValue(self, formula):
        formula = formula[1:]
        left, right = formula.split('+')
        val1 = self._get_operand_value(left)
        val2 = self._get_operand_value(right)
        return val1+val2

spreadsheet = Spreadsheet(3)

print(spreadsheet.getValue("=5+7"))   
spreadsheet.setCell("A1", 10)
print(spreadsheet.getValue("=A1+6"))  
spreadsheet.setCell("B2", 15)
print(spreadsheet.getValue("=A1+B2")) 
spreadsheet.resetCell("A1")
print(spreadsheet.getValue("=A1+B2")) 
