from src.days.day_2 import hasRepeatingPattern

def testCheckForEqualSizedPatterns():
    assert hasRepeatingPattern("121212") == True
    assert hasRepeatingPattern("1231") == False
    assert hasRepeatingPattern("123123") == True
    assert hasRepeatingPattern("12341234") == True
    assert hasRepeatingPattern("11111") == True
    assert hasRepeatingPattern("1231234") == False
    assert hasRepeatingPattern("12123121231212312123") == True
    assert hasRepeatingPattern("1212312123121231212312123") == True
