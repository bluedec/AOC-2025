
def day_3():
    print("Day 3: Lobby")
    total_joltage = 0

    with open("inputs/day_3_input.txt") as f:
        banks = [line.strip() for line in f.readlines()]

    for bank in banks:
        bank_as_ints = [int(b) for b in bank]
        print(bank_as_ints)
        bank_max_joltage = findBiggestJoltageFromBank(bank_as_ints, 12)
        total_joltage += bank_max_joltage
        print(bank_max_joltage)
    print(total_joltage)












def findBiggestJoltageFromBank(bank: list[int], resulting_bank_size: int) -> int:
    if resulting_bank_size < 1 or resulting_bank_size > len(bank):
        raise Exception(f"It's not possible to create a joltage of size {resulting_bank_size} from a bank of size: {len(bank)}")

    joltages = [0] * resulting_bank_size 
    joltages_left = resulting_bank_size
    latest_bank_id_saved = -1
    bank_length = len(bank)

    for joltage_index, _ in enumerate(joltages):
        max_lenght_traversable = bank_length - joltages_left
        print(f"cant go beyond {max_lenght_traversable}")

        for b_index, battery in enumerate(bank):

            if b_index > max_lenght_traversable: 
                print(f"{b_index} > {max_lenght_traversable}!")
                break

            if b_index <= latest_bank_id_saved: 
                print(f"{b_index} <= {latest_bank_id_saved}")
                continue

            if battery > joltages[joltage_index]:
                print(f"Saving {battery}:{b_index} at j[{joltage_index}]")
                joltages[joltage_index] = battery
                print("b:", bank)
                print(f"j: {joltages}")
                latest_bank_id_saved = b_index

        joltages_left -= 1

    joltages_as_ints = int("".join(map(str, joltages)))
    return joltages_as_ints


def findBiggestTwoDigitInt(bank: str) -> int:
    lj = 0
    idx_h = 0
    left_digit_idx = 0 
    for i in range(0, len(bank) - 1):
        battery_joltage = int(bank[i])
        if battery_joltage > lj:
            left_digit_idx += idx_h
            idx_h = 0
            lj = battery_joltage
        idx_h += 1

    rj = 0
    for i in range(left_digit_idx + 1, len(bank)):
        right_battery_joltage = int(bank[i])
        if right_battery_joltage > rj:
            rj = right_battery_joltage

    current_bank_max_joltage = str(lj) + str(rj)

    return int(current_bank_max_joltage)

        


