from octalToDecimal import octalToDecimal as o
from decimalToBinary import decimaltobinary as d


def octalToBinary(x):
    return d(o(x))


if __name__ == "__main__":
    print(octalToBinary(int(input("Enter the octal number: "))))
