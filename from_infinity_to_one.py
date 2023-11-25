x=str(input())
y=list(x)
sum=0
for i in range(len(y)):
    sum+=int(y[i])  
while len(str(sum))!=1:
    z=list(str(sum))
    sum=0
    for k in range(len(z)):
        sum+=int(z[k])     
print(sum)




