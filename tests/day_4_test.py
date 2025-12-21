
from src.days.day_4 import Grid

def testCheckForRollsInAdjacentPositions():
    grid = Grid([
        "@....@...@....@.......@",
        "@....@...@....@.......@",
        "....@@@..@....@.......@",
        "....@@@..@....@.......@",
        "@...@@@..@....@.......@",
        ".....@...@....@.......@",
        ])
    assert grid.checkForRollsInAdjacentPositions(0, 0) == 1
    assert grid.checkForRollsInAdjacentPositions(0, 1) == 2
    assert grid.checkForRollsInAdjacentPositions(4, 4) == 4
    assert grid.checkForRollsInAdjacentPositions(3, 5) == 8
    assert grid.checkForRollsInAdjacentPositions(0, 14) == 1
    assert grid.checkForRollsInAdjacentPositions(1, 14) == 2
    assert grid.checkForRollsInAdjacentPositions(2, 14) == 2
    assert grid.checkForRollsInAdjacentPositions(3, 14) == 2
    assert grid.checkForRollsInAdjacentPositions(4, 14) == 2
    assert grid.checkForRollsInAdjacentPositions(5, 14) == 1
