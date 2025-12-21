
from src.days.day_3 import findBiggestJoltageFromBank, findBiggestTwoDigitInt
from src.days.day_4 import Grid

def testFindBiggestTwoDigitInt():
    assert findBiggestTwoDigitInt("123") == 23
    assert findBiggestTwoDigitInt("12") == 12
    assert findBiggestTwoDigitInt("22342") == 42
    assert findBiggestTwoDigitInt("211111111111111111111112") == 22

def testFindBiggestJoltageFromBank():
    assert findBiggestJoltageFromBank([ int(x) for x in "19118117126125242423" ], 2) == 98
    assert findBiggestJoltageFromBank([ int(x) for x in "19118117126125242423" ], 3) == 987
    assert findBiggestJoltageFromBank([ int(x) for x in "19118117126125242423" ], 5) == 98765
    assert findBiggestJoltageFromBank([ int(x) for x in "19118117126125242423" ], 7) == 9876544
    assert findBiggestJoltageFromBank([ int(x) for x in "818181911112111" ], 12) == 888911112111
                                                  
