literals = {'A': '10', 'B': '11', 'C': '12',
            'D': '13', 'E': '14', 'F': '15'}
anti_literals = {v: k for k, v in literals.items()}


def check(num, radix):
    for i in num:
        if i in literals:
            i = literals[i]
        if int(i) >= radix:
            return False
    else:
        return True


def convert_to_decimal(num, radix):
    if check(num, radix):
        length = len(num) - 1
        summation = 0
        for i in num:
            if i in literals:
                i = literals[i]
            summation = summation + radix**length * int(i)
            length = length-1
        return summation
    else:
        print("Check the Number and Radix")
        print(f'{num} and {radix}')
        exit()


def convert_to_base(decimal, convert):
    result = ""
    while(decimal > 0):
        remainder = decimal % convert
        if str(remainder) in anti_literals:
            remainder = anti_literals[str(remainder)]
        result = result + f"{remainder}"
        decimal = decimal // convert
    return result[::-1]


def base_result(num, radix, convert):

    # num = list(input("Enter the number: ").strip())
    # radix = int(input("Enter the base: "))
    # convert = int(input("Enter the base in which you have to convert: "))
    decimal = int(convert_to_decimal(num, radix))

    # print(convert_to_base(decimal, convert))

    return convert_to_base(decimal, convert)
