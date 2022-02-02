from reverse import reverse as r


def decimaltobinary(x):
    rev_res = ''
    while x != 0:
        rev_res += str(x % 2)
        x = x // 2
        if x == 0:
            break
    else:
        rev_res = '0000'
    return r(rev_res)


if __name__ == '__main__':
    print(decimaltobinary(int(input('Enter the decimal number: '))))



