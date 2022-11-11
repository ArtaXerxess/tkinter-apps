# Integer to Roman

def translate_int_To_Roman(num: int) -> str:
    convert = {
        'M' :1000,
        'CM':900,
        'D' :500,
        'CD':400,
        'C' :100,
        'XC':90,
        'L' :50,
        'XL':40,
        'X' :10,
        'IX':9,
        'V' :5,
        'IV':4,
        'I' :1,
    }
    answer = ""
    for symbol, value in convert.items():
        if num >= value:
            multiplier = num // value
            num -= (value * multiplier)
            answer += (symbol*multiplier)
        if num == 0:
            return answer

if __name__ == '__main__':
    integer = int(input("Enter the number: "))
    print(translate_int_To_Roman(num=integer))
