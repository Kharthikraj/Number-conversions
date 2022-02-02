from reverse import reverse as r


def binarytodecimal(x):
    result = 0
    num = r(str(x))
    for i in range(len(num)):
        result += int(num[i]) * (2**i)
    return result


if __name__ == "__main__":
    print(binarytodecimal(int(input('Enter the binary number: '))))
