literals = {'A': '10', 'B': '11', 'C': '12',
            'D': '13', 'E': '14', 'F': '15'}
anti_literals = {v: k for k, v in literals.items()}


def checking(num, radix):
    for i in num:
        if i in literals:
            i = literals[i]
        if int(i) >= radix:
            return False
    else:
        return True


def check(num, radix):
    if '.' in num:
        a, b = map(list, num.split('.'))
        if checking(a, radix) and checking(b, radix):
            return True
        else:
            return False
    else:
        return checking(list(num), radix)


def convert_to_decimal(num, radix):
    if check(num, radix):
        if '.' in num:
            a, b = map(list, num.split('.'))
            length = len(a) - 1
            summation = 0
            for i in a:
                if i in literals:
                    i = literals[i]
                summation = summation + radix**length * int(i)
                length = length - 1
            power = -1
            sumup = 0
            for i in b:
                if i in literals:
                    i = literals[i]
                sumup = sumup + radix**power * int(i)
                power = power - 1
            return summation + sumup
        else:
            num = list(num)
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
    if '.' in decimal:
        a, b = decimal.split('.')
        a = int(a)
        while(a > 0):
            remainder = a % convert
            if str(remainder) in anti_literals:
                remainder = anti_literals[str(remainder)]
            result = result + f"{remainder}"
            a = a // convert
        result = result[::-1]
        b = float("0." + b)
        while True:
            b = b * convert
            print(b)
            if int(b) == b:
                return result + "." + str(convert_to_base(str(int(b)), convert))
        # return result + "." + str(int(b))

    else:
        decimal = int(decimal)
        while(decimal > 0):
            remainder = decimal % convert
            if str(remainder) in anti_literals:
                remainder = anti_literals[str(remainder)]
            result = result + f"{remainder}"
            decimal = decimal // convert
        return result[::-1]


def base_result(num, radix, convert):
    decimal = str(convert_to_decimal(num, radix))
    return convert_to_base(decimal, convert)


def base_calculator(num1, num2, radix, operator):

    result = ""

    num1 = convert_to_decimal(num1, radix)
    num2 = convert_to_decimal(num2, radix)
    print(num1, num2)
    # calculator
    if (operator == 'plus'):
        result = num1 + num2
    elif(operator == 'minus'):
        result = num1 - num2
    elif(operator == 'multiply'):
        result = num1 * num2
    elif(operator == 'divide'):
        result = num1 / num2

    return convert_to_base(str(result), radix)
