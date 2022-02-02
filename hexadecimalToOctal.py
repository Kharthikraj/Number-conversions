from hexadecimalToBinary import hexadecimalToBinary as h
from binaryToOctal import binarytooctal as b


def hexadecimalToOctal(x):
    return b(int(h(x)))


if __name__ == "__main__":
    print(hexadecimalToOctal(input("Enter the hexadecimal number: ")))