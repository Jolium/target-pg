#!/usr/bin/env python3

"""
Target Password Generator
Generates passwords with the target in mind!
"""

password_list = []
min_char = 8
max_char = 12
num_before = False
num_after = True
num_before_and_after = False
upper_and_lower = False
exp = 4


def header():
    print("\n11001010011101001100110010001100011010110011011000110101001110110")
    print("  00100010101011011100101100  TARGET-PG  01001101011011000101110110")
    print("    01110010000101110001100110101100111011011001000101010011101001101\n")


def y_or_n(boolean):
        if boolean:
            return "y"
        else:
            return "n"


def settings():
    print("\n\n=====================================================================")
    print("                              Settings")
    print("=====================================================================\n")
    print("[0] Exit settings")
    print("[1] Passwords minimum length (default = 8)                    [1]:%d" % min_char)
    print("[2] Passwords maximum length (default = 12)                   [2]:%d" % max_char)
    print("[3] Passwords with numbers before (default = n)               [3]:%s" % y_or_n(num_before))
    print("[4] Passwords with numbers after (default = y)                [4]:%s" % y_or_n(num_after))
    print("[5] Passwords with numbers before and after (default = n)     [5]:%s" % y_or_n(num_before_and_after))
    print("[6] Passwords with capital/small letters (default = n)        [6]:%s" % y_or_n(upper_and_lower))
    print("[7] Length of numbers (default = 4)                           [7]:%d" % exp)
    print("\n=====================================================================\n")

    user_settings = input("Choose settings number (0-7): ")

    try:
        int(user_settings)
    except ValueError:
        print("Invalid input! Please enter value from '0' to '7'.")
        settings()

    user_settings = int(user_settings)
    if user_settings < 0 or user_settings > 7:
        print("Invalid value! Please enter value from '0' to '7'.")
        settings()

    if 0 <= user_settings <= 7:
        user_settings_choice(user_settings)


def validation(input_value, user_numb):
    # make possible strings as input do not return errors
    try:
        int(input_value)
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        user_settings_choice(user_numb)


def user_settings_choice(user_settings):
    global min_char
    global max_char
    global num_before
    global num_after
    global num_before_and_after
    global upper_and_lower
    global exp

    if user_settings == 0:
        print("[0] Exit settings\n")
        return

    elif user_settings == 1:
        while True:
            print("\n" + "[1] Passwords minimum length (default = 8)")
            value1 = input("    Set the new value (1 - 12): ")
            validation(value1, user_settings)
            value1 = int(value1)
            if value1 > max_char:
                print("Invalid value! Minimum length cannot be higher than maximum length.")
            elif 1 <= value1 <= 12:
                min_char = value1
                settings()
                return
            else:
                print("Invalid value!")

    elif user_settings == 2:
        while True:
            print("\n" + "[2] Passwords maximum length (default = 12)")
            value2 = input("    Set the new value (8 - 18): ")
            validation(value2, user_settings)
            value2 = int(value2)
            if value2 < min_char:
                print("Invalid value! Maximum length cannot be lower than minimum length.")
            elif 8 <= value2 <= 18:
                max_char = value2
                settings()
                return
            else:
                print("Invalid value!")

    elif user_settings == 3:
        while True:
            print("\n" + "[3] Passwords with numbers before (default = n)")
            value3 = str(input("    Set to 'y' (yes) or 'n' (no): ").lower())
            if value3 == "y":
                num_before = True
                settings()
                return
            elif value3 == "n":
                num_before = False
                settings()
                return
            else:
                print("Invalid input!")

    elif user_settings == 4:
        while True:
            print("\n" + "[4] Passwords with numbers after (default = y)")
            value4 = str(input("    Set to 'y' (yes) or 'n' (no): ").lower())
            if value4 == "y":
                num_after = True
                settings()
                return
            elif value4 == "n":
                num_after = False
                settings()
                return
            else:
                print("Invalid input!")

    elif user_settings == 5:
        while True:
            print("\n" + "[5] Passwords with numbers before and after (default = n)")
            value5 = str(input("    Set to 'y' (yes) or 'n' (no): ").lower())
            if value5 == "y":
                num_before_and_after = True
                settings()
                return
            elif value5 == "n":
                num_before_and_after = False
                settings()
                return
            else:
                print("Invalid input!")

    elif user_settings == 6:
        while True:
            print("\n" + "[6] Passwords with capital/small letters (default = n)")
            value6 = str(input("    Set to 'y' (yes) or 'n' (no): ").lower())
            if value6 == "y":
                upper_and_lower = True
                settings()
                return
            elif value6 == "n":
                upper_and_lower = False
                settings()
                return
            else:
                print("Invalid input!")

    elif user_settings == 7:
        while True:
            print("\n" + "[7] Length of numbers (default = 4)")
            value7 = input("    Set the new value (0 - 8): ")
            validation(value7, user_settings)
            value7 = int(value7)
            if 0 <= value7 <= 8:
                exp = value7
                settings()
                return
            else:
                print("Invalid value!")


def user_choice():
    # choice between "d" and "c" (default/change)
    choice = ""

    while choice != "d" and choice != "c":
        choice = str(input("Press 'd' to default settings or 'c' to change settings: ").lower())
        if choice == "d":
            break
        elif choice == "c":
            settings()
        else:
            print("Invalid option!\n")


def make_passwords(password):
    # add passwords to list
    e = exp

    for x in range(4, 0, -1):
        r = 10 ** e
        e -= 1

        for num in range(r):
            if num_before:
                password_list.append(str(num).zfill(x) + str(password))
                if upper_and_lower:
                    password_list.append(str(num).zfill(x) + str(password.lower()))
                    password_list.append(str(num).zfill(x) + str(password.upper()))

            if num_after:
                password_list.append(str(password) + str(num).zfill(x))
                if upper_and_lower:
                    password_list.append(str(password.lower()) + str(num).zfill(x))
                    password_list.append(str(password.upper()) + str(num).zfill(x))

            if num_before_and_after:
                password_list.append(str(num).zfill(x) + str(password) + str(num).zfill(x))
                if upper_and_lower:
                    password_list.append(str(num).zfill(x) + str(password.lower()) + str(num).zfill(x))
                    password_list.append(str(num).zfill(x) + str(password.upper()) + str(num).zfill(x))

    print("'" + password + "' added to Passwords_list.txt")
    make_pass_list()
    enter_words()


def enter_words():
    user_input = str(input("\nEnter word ('//' to stop): "))

    if user_input == "//":
        print(">>>> target-pg closed <<<< ")
    elif user_input == "" or " " in user_input:
        print("No word entered!")
        enter_words()
    else:
        make_passwords(user_input)
        return user_input


def make_pass_list():
    global password_list
    password_list2 = []
    txt = password_list[:]

    for word in txt:
        if min_char <= len(word) <= max_char:
            password_list2.append(word)

    file = open("Passwords_list.txt", "a+")
    file.write("\n".join(map(str, password_list2)))
    password_list = []


header()
user_choice()
enter_words()

exit()
