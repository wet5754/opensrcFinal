import math
def m(i):
    result = 0.0
    for j in range(i+1):
        result += (-1)**(j+1)/(2*j-1)
    result *= 4
    return result-4

print("i"+"\t"+"m(i)")
for i in range(1,1001,100):
    print(str(i)+'\t'+str(m(i)))