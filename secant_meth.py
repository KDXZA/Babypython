import math
a=-3
b=0
A_C=0.000001
X_0=(a+b)/3
X_1=(a+b)/2.5
count=1
while(True):
    F_X_N_1=(2*X_1*(math.cos(2*X_1)))-((X_1+1)**2)
    F_X_N_0=(2*X_0*(math.cos(2*X_0)))-((X_0+1)**2)
    D_F_X_N_1=(F_X_N_1-F_X_N_0)/(X_1-X_0)
    X_2=X_1-(F_X_N_1/D_F_X_N_1)
    print("X_{} ={}".format(count-1,X_0))
    print("X_{} ={}".format(count,X_1))
    print("X_{} ={}".format(count+1,X_2))
    print("F_X_N_{}={}".format(count+1,F_X_N_1))
    print("---------------------------")
    if abs(X_2-X_1)< A_C:
        break
    count+=1
    X_0=X_1
    X_1=X_2
print("\nApproximate solution:", X_2)
print("Iteration:", count)
print("Accuracy:", abs(X_2-X_1))    
    
