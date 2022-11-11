# roman to integer

def translate_rom_to_int(roman : str):

    roman = roman.upper()

    translations = {
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
    }

    roman = roman.replace("IV","IIII").replace("IX","VIIII")
    roman = roman.replace("XL","XXXX").replace("XC","LXXXX")
    roman = roman.replace("CD","CCCC").replace("CM","DCCCC")

    number = 0

    for char in roman:
        number += translations[char]

    return number

# testing
if __name__ == '__main__':
    roman = input("Enter the Roman Integer: ").upper()
    print(translate_rom_to_int(roman=roman))