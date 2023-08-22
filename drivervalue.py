if __name__ == '__main__':
    b=input("Enter the register value")
    if(b=='00'):
        print("Medium")
    elif(b=='01'):
        print("Low")
    elif (b == '10'):
        print("High")
    elif (b == '11'):
        print("Off")
    else:
        print("Incorrect Value")
