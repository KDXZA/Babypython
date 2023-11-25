
import math
a=-3
b=0
A_C=0.000001
X_L=a;
X_R=b;
i=1
while(True):
    X_M=(X_L/2)+(X_R/2);
    F_X_L=(2*X_L*(math.cos(2*X_L)))-((X_L+1)**2);
    F_X_R=(2*X_R*(math.cos(2*X_R)))-((X_R+1)**2);
    F_X_M=(2*X_M*(math.cos(2*X_M)))-((X_M+1)**2);
    print("Iteration round {} F_X_L is {}".format(i,float(F_X_L)))
    print("Iteration round {} F_X_R is {}".format(i,float(F_X_R)))
    print("Iteration round {} F_X_M is {}".format(i,float(F_X_M)))
    print("Iteration round {} X_M is {}".format(i,float(X_M)))
    print("------------------------------")
    if F_X_M*F_X_R<0:
        X_L=X_M;
    else:
        X_R=X_M;
    i+=1
    if abs(F_X_M)< A_C:
        break

print("\nApproximate solution:", X_M)
print("Iteration:", i)
print("Accuracy:", abs(F_X_M))
