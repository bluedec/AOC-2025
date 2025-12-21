

def day_4():
    print("Day 4 - Printing Department")
    with open("inputs/day_4_input.txt") as f:
        lines = f.readlines()
        grid = Grid(lines)

    accessable_rolls = 0
    print(grid.values)
    for row_id, row in enumerate(grid.values):
        for col_id, char in enumerate(row):
            if char == '@':
                rolls = grid.checkForRollsInAdjacentPositions(row_id, col_id)
                if rolls < 4:
                    accessable_rolls += 1


    print("Total accessable rolls:", accessable_rolls)


class Grid:
    values = list()
    length = 0
    height = 0
    def __init__(self, lines: list[str]):
        for line in lines:
            self.values.append(list(line.strip()))
        self.length = len(self.values)
        self.height = len(self.values[0])

    def checkForRollsInAdjacentPositions(self, row: int, column: int) -> int:
        # we expect the self.values to be set
        if (self.values[0] == None):
            raise Exception("The grid does not have an initial row (or an array at all) so it can't traverse it. Please assign one to Grid before continuing.")

        curr_line = self.values[row]

        rolls = 0
        check_left = column > 0
        check_right = column < self.length - 1

        check_up = row > 0
        check_down = row < self.height - 1
        print(row, self.height)

        # previous line
        if check_up:
            prev_line = self.values[row - 1]
            if (check_left):
                if prev_line[column - 1] == '@':
                    rolls += 1
            if (check_right):
                if prev_line[column + 1] == '@':
                    rolls += 1
            if prev_line[column] == '@':
                rolls += 1

        # next line
        if check_down:
            next_line = self.values[row + 1]
            if (check_left):
                if next_line[column - 1] == '@':
                    rolls += 1
            if (check_right):
                if next_line[column + 1] == '@':
                    rolls += 1
            if next_line[column] == '@':
                rolls += 1

        # current line
        if (check_left):
            if curr_line[column - 1] == '@':
                rolls += 1
        if (check_right):
            if curr_line[column + 1] == '@':
                rolls += 1

        return rolls

