def summation(list):
    x=len(list)
    addition=0
    for i in range(0,x):
        addition += list[i]
        i+=1
    return addition

numlist=[8,2,3,0,7]
print(summation(numlist))

