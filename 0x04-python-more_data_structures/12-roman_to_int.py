#!/usr/bin/python3

def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0

    str_rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    int_rom = 0

    for m in range(len(roman_string)):
        if m > 0 and str_rom[roman_string[m]] > str_rom[roman_string[m - 1]]:
            int_rom += str_rom[roman_string[m]] - 2 * \
                        str_rom[roman_string[m - 1]]

        else:
            int_rom += str_rom[roman_string[m]]

    return int_rom
