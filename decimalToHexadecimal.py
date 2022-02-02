from decimalToBinary import decimaltobinary as d
from binaryToHexadecimal import BinaryToHexadecimal as B


def decimalToHexadecimal(x):
    return B(d(x)).converter()


if __name__ == "__main__":
    print(decimalToHexadecimal(int(input("Enter the decimal number: "))))