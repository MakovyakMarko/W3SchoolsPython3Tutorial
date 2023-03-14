def decimal_to_binary(number):
    return bin(int(number))[2:]
def decimal_to_octal(number):
    return oct(int(number))[2:]
def decimal_to_hexadecimal(number):
    return hex(int(number))[2:]
def from_binary_to_octal(number):
    decimal_number = int(number, 2)
    return oct(decimal_number)[2:]
def from_binary_to_decimal(number):
    decimal = 0
    for digit in number:
        decimal = decimal * 2 + int(digit)
    return decimal
def from_binary_to_hexadecimal(number):
    decimal_number = int(number, 2)
    return hex(decimal_number)[2:]

def from_octal_to_decimal(number):
    decimal = 0
    for digit in number:
        decimal = decimal * 8 + int(digit)
    return decimal
def from_octal_to_binary(number):
    decimal_number = from_octal_to_decimal(number)
    binary = decimal_to_binary(decimal_number)
    return binary
def from_octal_to_hexadecimal(number):
    decimal_number = int(number, 8)
    return hex(decimal_number)[2:]
def from_hex_to_binary(number):
    decimal_number = int(number, 16)
    return bin(decimal_number)[2:]
def from_hex_to_octal(number):
    decimal_number = int(number, 16)
    return oct(decimal_number)[2:]
def from_hex_to_decimal(number):
    hex_digits = "0123456789ABCDEF"
    decimal_number = 0
    for digit in number:
        decimal_number = decimal_number * 16 + hex_digits.index(digit)
    return decimal_number
def convert_number():
    number = input("Введіть число, яке ви хочете перевести: ")
    base_from = int(input("Введіть систему числення числа (2,8,10,16): "))
    base_to = int(input("Введіть систему числення, в яку хочете перевести число (2,8,10,16): "))
    # перевірка на валідність вхідних даних
    #if not(2<= base_from <= 16 ) or not(2 <= base_to <= 16):
    #   print("Неправильно введена система числення")
    #   return
    try:
        # переведення числа з десяткової системи числення в задану
        if base_from == 10 and base_to == 2:
            converted_number = decimal_to_binary(number)
        elif base_from == 10 and base_to == 8:
            converted_number = decimal_to_octal(number)
        elif base_from == 10 and base_to == 10:
            converted_number = str(number)
        elif base_from == 10 and base_to == 16:
            converted_number = decimal_to_hexadecimal(number)
        elif base_from == 2 and base_to == 2:
            converted_number = str(number)
        elif base_from == 2 and base_to == 8:
            converted_number = from_binary_to_octal(number)
        elif base_from == 2 and base_to == 10:
            converted_number = from_binary_to_decimal(number)
        elif base_from == 2 and base_to == 16:
            converted_number = from_binary_to_hexadecimal(number)
        elif base_from == 8 and base_to ==2:
            converted_number = from_octal_to_binary(number)
        elif base_from == 8 and base_to == 8:
            converted_number = str(number)
        elif base_from == 8 and base_to == 10:
            converted_number = from_octal_to_decimal(number)
        elif base_from == 8 and base_to == 16:
            converted_number = from_octal_to_hexadecimal(number)
        elif base_from == 16 and base_to == 2:
            converted_number = from_hex_to_binary(number)
        elif base_from == 16 and base_to == 8:
            converted_number = from_hex_to_octal(number)
        elif base_from == 16 and base_to == 10:
            converted_number = from_hex_to_decimal(number)
        elif base_from == 16 and base_to == 16:
            converted_number = str(number)
        else:
            print("Система числення повинна бути 2, 8, 10, 16.")
        print(f"Число {number} у системі числення {base_from} дорівнює {converted_number} у системі числення {base_to}")
    except ValueError:
        print("Неправильно введене число")

convert_number()