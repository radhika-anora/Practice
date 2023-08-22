temperature = list(map(int, input("Enter the temperature values in celsius : ").split()))

Fahrenheit = [(lambda t: t * 1.8 + 32)(celsius) for celsius in temperature]

print("Fahrenheit values are : ", Fahrenheit)
