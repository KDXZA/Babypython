
import math
a=-3
b=0
A_C=0.000001
X_0=(a+b)/3
count=1
while(True):
    F_X_N=(2*X_0*(math.cos(2*X_0)))-((X_0+1)**2)
    
    D_F_X_N=(2*X_0*((-2)*math.sin(2*X_0)-1))+2*(math.cos(2*X_0)-1)
    
    X_1=X_0-(F_X_N/D_F_X_N)
    print("X_{} ={}".format(count-1,X_0))
    print("X_{} ={}".format(count,X_1))
    print("F_X_N ={}".format(F_X_N))
    print("---------------------------")
    if abs(X_1-X_0)< A_C:
        break
    count+=1
    X_0=X_1
    
print("\nApproximate solution:", X_1)
print("Iteration:", count)
print("Accuracy:", abs(X_1-X_0))

