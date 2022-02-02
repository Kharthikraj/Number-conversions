from octalToBinary import octalToBinary as o
from binaryToHexadecimal import BinaryToHexadecimal as B


def octalToHexadecimal(x):
    return B(o(x)).converter()


if __name__ == '__main__':
    print(octalToHexadecimal(int(input("Enter the octal number: "))))