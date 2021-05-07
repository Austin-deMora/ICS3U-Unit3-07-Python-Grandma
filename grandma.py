#!/usr/bin/env python3
#
# Created by: Austin de Mora
# Created on: May 2021
# This program checks if a person reaches a certain set of parameters

import math


def main():
    # This function checks the persons age

    # Input

    participants_age = input("Enter your age: ")
    print("")

    # process
    try:
        if int(participants_age) >= 25 and int(participants_age) <= 40:
            # Output
            print("You are old enough")
        else:
            print("You are not old enough")
    except Exception:
        print("This was not an integer")


if __name__ == "__main__":
    main()
