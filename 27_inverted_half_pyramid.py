n = int(input("Enter size of pyramid: "))

for i in range(n,0,-1):
    for j in range(i):
        print("*",end=' ')
    
    print('\r')