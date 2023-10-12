N=int(input("please enter a number: "))
if N>0:
    for i in range(1,N+1):
        if N%i==0:
            print(i,"is a divisor of",N)
else:
    print("please enter a positive number")
