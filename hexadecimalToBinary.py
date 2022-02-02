from hexadecimalToDecimal import hexadecimalToDecimal as h
from decimalToBinary import decimaltobinary as d


def hexadecimalToBinary(x):
    return d(h(x))


if __name__ == "__main__":
    print(hexadecimalToBinary(input("Enter the hexadecimal number: ")))