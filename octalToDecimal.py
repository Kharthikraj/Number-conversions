from reverse import reverse as r


def octalToDecimal(x):
    result = 0
    rev_str = r(str(x))
    for i in range(len(rev_str)):
        result += int(rev_str[i]) * (8**i)
    return result


if __name__ == "__main__":
    print(octalToDecimal(int(input("Enter the octal number: "))))
