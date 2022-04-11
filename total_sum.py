#!/usr/bin/env python3

# Created by: Andrew-Ten-Den
# Created on: April 2022
# This program adds the sum of consecutive integers


def main():
    # this function adds the sum of consecutive integers

    # this is to keep track of how many times you go through the loop
    loop_counter = 0
    total_sum = 0

    # input
    try:
        integer = int(input("Enter a number: "))

        # process & output
        print("\n", end="")
        while loop_counter <= integer:
            total_sum = total_sum + loop_counter
            loop_counter = loop_counter + 1
        print("The sum is {0}.".format(total_sum))
    except Exception:
        print("This was not an integer")
    finally:
        print("")
        print("Done")


if __name__ == "__main__":
    main()
