def binaryconverter(b):
    c = bin(b)
    c = c.replace("0b", "")
    c = (16 - len(c)) * '0' + c
    return c
if __name__ == '__main__':
    n=int(input("Enter the number"))
    c=binaryconverter(n)
    print("The binary of n is "+c)
    p = int(input("Enter the number to find bit position at"))
    print("The bit at the given position is(start from 1 from right to left) "+ c[-p])
