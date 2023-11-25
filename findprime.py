x=int(input())    
for i in range(1,x+1):
    for j in range(1,x+1):
        if i>1  and i*j==x and j>1 :
            print("i*j: ",i*j," i:",i," j:",j)
            

