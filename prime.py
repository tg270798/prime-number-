def series(N):
    a = 1
    b = 1
    lis =[1,1]
    for i in range(2,N):
        if(i%2 == 0):
            a = a*2
            lis.insert(i,a)
        elif(i%2 != 0):
            b = b*3
            lis.insert(i,b)
    
    #print(str(lis)[1:-1])
    print(','.join(map(str,lis)))
    


N = int(input())
if(N<=2):
    print(1,',',1)
else:
    series(N)
