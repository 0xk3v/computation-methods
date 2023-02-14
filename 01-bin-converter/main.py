from converter import NumberConverter


if __name__ == "__main__":
    # Object initiation
    number = NumberConverter.from_input()

    decimal = number.to_decimal()
    binary = number.to_binary()
    hexadecimal = number.to_hexadecimal()
    octal = number.to_octal()

    print(f"Original number: {number.value} (base {number.base})")
    print(f"Decimal: {decimal}")
    print(f"Binary: {binary}")
    print(f"Hexadecimal: {hexadecimal}")
    print(f"Octal: {octal}")
