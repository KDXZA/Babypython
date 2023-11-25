# zip_function 
# use to find answer of about matrix
L1=[1,2,3]
L2=[2,4,7]
res=zip(L1,L2)
L3=list(zip(L1,L2))
L4=[]
# List_comprehension_form !1
L5=[x1+x2 for (x1,x2) in L3]
for (x1,x2) in L3:
    L4.append(x1+x2)
print("L4=",L4)
print("L5=",L5)
print(res)
# List_comprehension_form !2
L1 = [1, 5, 2, 16, 32, 3, 54, 8, 100]
L2 = [1, 3, 10, 2, 42, 2, 3, 4, 3]
L3=[x1+x2 for (x1,x2) in list(zip(L1,L2)) if x1>10 and x2<5]
print(L3) 


