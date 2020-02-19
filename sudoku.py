class Grid(object):    

    def _build_ptrs(self):
        self._box_ptrs = []
        self._box_ptrs.append([(1,1),(1,2),(1,3), (2,1),(2,2),(2,3), (3,1),(3,2),(3,3)])
        self._box_ptrs.append([(1,4),(1,5),(1,6), (2,4),(2,5),(2,6), (3,4),(3,5),(3,6)])
        self._box_ptrs.append([(1,7),(1,8),(1,9), (2,7),(2,8),(2,9), (3,7),(3,8),(3,9)])
        
        self._box_ptrs.append([(4,1),(4,2),(4,3), (5,1),(5,2),(5,3), (6,1),(6,2),(6,3)])
        self._box_ptrs.append([(4,4),(4,5),(4,6), (5,4),(5,5),(5,6), (6,4),(6,5),(6,6)])
        self._box_ptrs.append([(4,7),(4,8),(4,9), (5,7),(5,8),(5,9), (6,7),(6,8),(6,9)])

        self._box_ptrs.append([(7,1),(7,2),(7,3), (8,1),(8,2),(8,3), (9,1),(9,2),(9,3)])
        self._box_ptrs.append([(7,4),(7,5),(7,6), (8,4),(8,5),(8,6), (9,4),(9,5),(9,6)])
        self._box_ptrs.append([(7,7),(7,8),(7,9), (8,7),(8,8),(8,9), (9,7),(9,8),(9,9)])
    
    def _build_grid(self):
        self._grid = [[i for i in range(1,10)] for _ in range(1,10)]
        self._cellrotate(1,3)
        self._cellrotate(2,6)
        self._cellrotate(3,1)
        self._cellrotate(4,4)
        self._cellrotate(5,7)
        self._cellrotate(6,2)
        self._cellrotate(7,5)
        self._cellrotate(8,8)

    def __init__(self, cells = None):
        self._build_ptrs()        
        if cells is None:
            self._build_grid()
        else:
            self._grid = cells
        
    def _cellrotate(self, row, count):
        left = self._grid[row][:count]
        right = self._grid[row][count:]        
        self._grid[row] = right + left

    def get_row(self, row_number):
        return self._grid[row_number-1]

    def get_col(self, col_number):
        return [row[col_number-1] for row in self._grid]

    def get_cel(self, row, col):
        return self._grid[row-1][col-1]

    def get_box(self, box_number):
        box = []
        for row,col in self._box_ptrs[box_number-1]:
            box.append(self.get_cel(row,col))
        return box

    def __str__(self):
        _string = '-'*25 + '\n'
        for row, g in enumerate(self._grid):
            if row > 0 and row % 3 == 0:
                _string += '-'*25 + '\n'
            _string += f"| {g[0]} {g[1]} {g[2]} | {g[3]} {g[4]} {g[5]} | {g[6]} {g[7]} {g[8]} |\n"            
        _string += '-'*25
        return _string

    def _is_valid(cells):
        return sorted(cells) == [1,2,3,4,5,6,7,8,9]
        
    def is_valid(self):
        for i in range(1,10):
            if not Grid._is_valid(self.get_row(i)):
                print(f"row {i} is invalid: {self.get_row(i)}")
                return False
            if not Grid._is_valid(self.get_col(i)):
                print(f"col {i} is invalid: {self.get_col(i)}")
                return False
            if not Grid._is_valid(self.get_box(i)):
                print(f"box {i} is invalid: {self.get_box(i)}")
                return False
        print("grid is valid")
        return True

foo = Grid()
print(foo)

# print(foo.get_row(1))
# print(foo.get_row(9))
# print(foo.get_col(1))
# print(foo.get_col(9))
# print(foo.get_box(3))
# print(foo.get_box(7))

print(foo.is_valid())

foo._grid[4][3] = 1
foo._grid[4][5] = 8
print(foo)
print(foo.is_valid())


