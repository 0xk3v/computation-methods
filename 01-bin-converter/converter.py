"""
Python Module to check a number given and return true or false
"""


class NumberConverter:
    # Class constructor
    def __init__(self, value, base=10):
        self.value = value
        self.base = base
        self.integer, self.fraction = self._split_fraction(value)

    def to_decimal(self):
        """Class Method to Convert given number to Decimal"""

        # Returning the same number is the base is 10
        if self.base == 10:
            return float(self.value)

        decimal = 0
        power = 0

        for digit in reversed(str(self.integer)):
            if self.base == 16:
                digit = int(digit, 16)
            else:
                digit = int(digit)
            decimal += digit * (self.base**power)
            power += 1

        if self.fraction:
            fraction = 0
            power = -1
            for digit in str(self.fraction):
                if self.base == 16:
                    digit = int(digit, 16)
                else:
                    digit = int(digit)
                fraction += digit * (self.base**power)
                power -= 1
            decimal += fraction

        return decimal

    def to_binary(self):
        decimal = self.to_decimal()
        integer_part = int(decimal)
        binary = ""

        while integer_part > 0:
            binary = str(integer_part % 2) + binary
            integer_part //= 2

        if decimal != int(decimal):
            binary += "."
            fraction_part = decimal - int(decimal)
            for i in range(20):
                fraction_part *= 2
                binary += str(int(fraction_part))
                fraction_part -= int(fraction_part)

        return binary

    def to_hexadecimal(self):
        decimal = self.to_decimal()
        integer_part = int(decimal)
        hexadecimal = ""

        while integer_part > 0:
            remainder = integer_part % 16
            if remainder < 10:
                hexadecimal = str(remainder) + hexadecimal
            else:
                hexadecimal = chr(remainder + 55) + hexadecimal
            integer_part //= 16

        if decimal != int(decimal):
            hexadecimal += "."
            fraction_part = decimal - int(decimal)
            for i in range(20):
                fraction_part *= 16
                digit = int(fraction_part)
                if digit < 10:
                    hexadecimal += str(digit)
                else:
                    hexadecimal += chr(digit + 55)
                fraction_part -= digit

        return hexadecimal

    def to_octal(self):
        decimal = self.to_decimal()
        integer_part = int(decimal)
        octal = ""

        while integer_part > 0:
            octal = str(integer_part % 8) + octal
            integer_part //= 8

        if decimal != int(decimal):
            octal += "."
            fraction_part = decimal - int(decimal)
            for i in range(20):
                fraction_part *= 8
                octal += str(int(fraction_part))
                fraction_part -= int(fraction_part)

        return octal

    def _split_fraction(self, value):
        integer, fraction = (value.split(".", 1) + [""])[:2]
        return integer, fraction

    @classmethod
    def from_input(cls):
        value = input("Enter a number: ")
        if value[:2].lower() == "0b":
            return cls(value[2:], 2)
        elif value[:2].lower() == "0x":
            return cls(value[2:], 16)
        elif value[:1] == "0":
            return cls(value[1:], 8)
        else:
            return cls(value, 10)
