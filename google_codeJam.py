import string


def convert_to_num(x):
    for i in range(len(x)):
        x[i]=int(x[i])
    return x 

def Input():
    T=int(input())
    for i in range(T):
        x=str(input())
        x=x.split(" ")
        x=convert_to_num(x)
        y=str(input())
        y=x.split(" ")
        y=convert_to_num(x)


    
def sol(h,k):
    k=sorted(k)
    ans=0
    sum=0
    for i in range(len(k)):
        sum+=k[0]
        if sum>h[1]:
            break;  
        ans+=1
    return ans
Input()


