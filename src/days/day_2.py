def day_2():
    print("Day 2: Gift Shop")
    sum_of_wrong_ids = 0
    with open("inputs/day_2_input.txt") as f:
        intervals = [i.strip() for i in f.read().split(',')]

    for ival in intervals:
        first = int(ival.split('-')[0])
        last = int(ival.split('-')[1])

        for id_number in range(first - 1, last + 1):
            if hasRepeatingPattern(str(id_number)):
                sum_of_wrong_ids += id_number

    print(sum_of_wrong_ids)


def hasRepeatingPattern(number_str: str, divider: int = 2) -> bool:
    """Checks for repeating patterns on a number

    Example:
    number_str 121212 has a pattern when the divider is 3, that number is 12-12-12
    but there is none when the divider is 2 since 121-212 are not equal

    Another possible pattern is with number 111, where the only possible pattern
    is found at a divider of 3. The pattern is 1-1-1.
    
    This will increase the divider until the length of the number is reached; where it will
    conclude (or not) that no patterns where found. 

    Returns True if a pattern has found and False else.
    """
    number_length = len(number_str)

    if divider > number_length: 
        return False

    if number_length % divider != 0:
        return hasRepeatingPattern(number_str, divider + 1)
    
    step = int(number_length / divider)
    steps = [0]
    for _ in range(1, divider):
        steps.append(steps[-1] + step)

    for i in range(0, step):
        found_distinct = False
        current_digit = number_str[i]

        for stp in steps:
            if current_digit != number_str[stp + i]:
                found_distinct = True
                break

        if found_distinct:
            return hasRepeatingPattern(number_str, divider + 1)

    return True

