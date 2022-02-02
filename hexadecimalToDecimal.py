def hexadecimalToDecimal(x):
    result = 0
    lis_x = list(x)
    lis_one = list()
    for i in lis_x:
        if ord(i) in range(48, 58):
            lis_one.append(i)
            continue
        else:
            i = str(ord(i.upper()) - 55)
        lis_one.append(i)
    lis_one.reverse()
    for i in range(len(lis_one)):
        result += int(lis_one[i]) * (16**i)
    return result


if __name__ == "__main__":
    print(hexadecimalToDecimal(input("Enter the hexadecimal number: ")))