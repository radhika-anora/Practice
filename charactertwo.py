if __name__ == '__main__':
    a=input("Enter a character ")
    b=ord(a)
    if(b<=125):
        b=b+2
        print(chr(b))
    else:
        print("ASCII out of bound")
