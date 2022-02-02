from decimalToBinary import decimaltobinary as d
from binaryToOctal import binarytooctal as b


def decimalToOctal(x):
    return b(d(x))


if __name__ == "__main__":
    print(decimalToOctal(int(input("Enter the decimal number: "))))