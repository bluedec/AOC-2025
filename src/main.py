import sys
import days

def main(args):
    if len(args) == 1:
        day = args[0]
        match day:
            case "1":
                days.day_1()
            case "2":
                days.day_2()
            case "3":
                days.day_3()
            case "4":
                days.day_4()
            case _:
                print("That day is not available.")


    elif len(args) > 1:
        print("Multiple arguments found, only the 'Day' argument is available.")
        print("Please specify only the Day.")
        return


if __name__ == "__main__":
    main(sys.argv[1:])
