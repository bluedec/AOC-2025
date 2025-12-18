
def day_1():
    file_name = 'days/day_1_input.txt'
    file_lines = None
    try:
        with open(file_name, 'r') as f:
            file_lines = f.readlines()
    except FileNotFoundError:
        print("No input file found, aborting.")

    if file_lines == None:
        print("Input file is empty, aborting.")
        return

    print("Day 1: Secret Entrance")

    file_lines[:] = [i.strip() for i in file_lines if i]
    offset = 50
    zeros_found = 0

    for rotation in file_lines:
        direction = rotation[0]
        size = int(rotation[1:])
        print(rotation)
        
        while(size > 0):
            if direction == "R":
                size -= 1
                offset += 1
                if offset == 100:
                    zeros_found += 1
                    offset = 0

            if direction == "L":
                size -= 1
                offset -= 1
                if offset == -1:
                    offset = 99
                if offset == 0:
                    zeros_found += 1

    print("Password:", zeros_found)

