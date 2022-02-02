def binarytooctal(x):
    result = list()
    lis = list()
    str_x = str(x)
    len_x = len(str_x)
    rem = len_x % 3
    if rem != 0:
        len_x += 3 - rem
    str_x = f'{str_x:0>{len_x}}'
    for i in range(0, len_x, 3):
        lis.append(str_x[i:i+3])
    for a in lis:
        temp = 0
        for b in range(3):
            if b == 0:
                temp += int(a[b]) * 4
            elif b == 1:
                temp += int(a[b]) * 2
            else:
                temp += int(a[b]) * 1
        result.append(str(temp))
    final_result = ''.join(result)
    return final_result


if __name__ == "__main__":
    print(binarytooctal(int(input("Enter binary number: "))))