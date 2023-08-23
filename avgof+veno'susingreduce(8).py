from functools import reduce

list=[1,-6,5,3,-8,-4,9,6]
res = [x for x in list if x>0]
print(res)

def avg(list):
    return reduce(lambda a,b:a+b,list)/n

n=len(res)
avg=avg(res)

print("The average of +ve numbers in a list are : ",avg)
