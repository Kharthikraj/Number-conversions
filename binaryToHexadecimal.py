class BinaryToHexadecimal:
    def __init__(self, x):
        self.final_result = ''
        self.str_x = str(x)
        self.result = list()
        self.lis = list()
        self.len_x = len(self.str_x)
        self.rem = self.len_x % 4

    def binary_to_hexadecimal(self):
        if self.rem != 0:
            self.len_x += 4 - self.rem
        self.str_x = f'{self.str_x:0>{self.len_x}}'
        for i in range(0, self.len_x, 4):
            self.lis.append(self.str_x[i:i+4])
        for a in self.lis:
            temp = 0
            for b in range(4):
                if b == 0:
                    temp += int(a[b]) * 8
                elif b == 1:
                    temp += int(a[b]) * 4
                elif b == 2:
                    temp += int(a[b]) * 2
                else:
                    temp += int(a[b]) * 1
            self.result.append(str(temp))

    def converter(self):
        self.binary_to_hexadecimal()
        for i in self.result:
            int_i = int(i)
            if int_i > 9:
                int_i += 55
                self.final_result += chr(int_i)
            else:
                self.final_result += i
        return self.final_result


if __name__ == "__main__":
    print(BinaryToHexadecimal(int(input("Enter the binary number: "))).converter())

