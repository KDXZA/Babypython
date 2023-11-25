# x=int(input())
# y=int(input())
# count=0
# for i in range(x,y+1):
#     z=list(str(i))
#     for j in range(len(z)):
#         if z[j]=='9':
#             count+=1
# print(count) 
# how many nine in range           
# x=str(input())
# y=list(x)
# sum=0
# for i in range(len(y)):
#     if y[i]=='1':
#         k=2**len(y)/2**i
#         k2=2
#         y[i]=str(int(k/k2))
# for j in range(len(y)):
#     sum+=int(y[j])
# print(sum)
# ฐาน2ไปฐาน10
# ---------------------------
# x=int(input())
# z=[]
# sum=0
# sum+=x
# for i in range(1,x+1):
#     if i%3==0:
#         sum+=1
#         z.append(i)
# # print(z)
# # print(sum)
# a=len(z)//3
# sum+=a
# print(sum)
# inp=str(input())
# x=list(inp)
# sum=0
# a=0
# z=[]
# y=['1','2','3','4','5','6','7','8','9','0']
# for i in range(len(x)):
#     while x[i+1] in y and x[i] in y:
#         z.append(x[i])
#         z.append(x[i+1])
#         break
# print(z)
# l1=list(input())
# l2=list(input())
# l3=['1']
# a=[]
# for i in range(len(l1)):
#     l3[0]=l1[i]
#     l1[i]=l1[len(l1)-i-1]
#     l1[len(l1)-i-1]=l3[0]
#     if i==len(l1)//2:
#         break;       
#     print(l1)
        
# ''.join(l1)            
# for j in range(len(l2)):
#     l3[0]=l2[j]
#     l2[j]=l2[len(l1)-j-1]
#     l2[len(l2)-j-1]=l3[0]
# ''.join(l2)                    
# print(l2)           
#   two sum 
# x=int(input())
# y=int(input())
# z=[]
# for i in range(y):
#     buffer=str(input())
#     buffer.split(' ')
#     z.append(buffer)
# print(z) 


# nums1=list(input()) 
# nums2=list(input()) 
# z=[]
# for i  in range(len(num1)):
#     z.append(num1[i])      
# for j in range(len(num2)):
#     z.append(num2[j])
# ans=sorted(z)
# sum=0
# for k in range(len(ans)):
#     sum+=int(ans[k])
# print(float(sum/len(ans)))
# --------------------------------   
# x=str(input())
# y=['1','2','3','4','5','6','7','8','9','0']
# z=[]
# sum=0
# for i in range(len(x)):
#     while x[i] in y :
#         z.append(x[i])    
#     "".join(z)
#     sum+=int(z)
#     z.clear()
# print(sum)
#----------------------------------
# x=int(input())
# for i in range(0,x):
#     sum=0
#     for j in range(1,3+i+i+1,2):
#         a=" "*(x-sum)
#         sum+=1
#         print(a,"*"*j)
# y=x-1        
# print(" "*y,"|")
# print("{}{}{}{}" .format(" ","="*x,"V","="*x))
#-----------------------
# x=int(input())
# z=[1,3]

# for i in range(1,x-1): 
#     a=3**i
#     for j in range(3):
#         if j==0:
            
#             z.append(a*3)
#         if j==1:
            
#             z.append(a/3*11)
#         if j==2:
            
#             z.append(a/3*19)
# sorted(z)            
# print(z)      
#--------------------------------
# x=str(input())
# a=x.split("+")
# k=len(a)
# a2=sorted(a)
# b=[]
# i=0
# while k>0:
#     b.append(a2[i])
#     b.append("+")
#     i+=1
#     k-=1
# print("".join(b[:-1]))
#--------------------------------
# x=int(input("Number: "))
# a=x
# z=[]
# z2=[]
# while a>0:
#     y=int(input())
#     z.append(y)
#     a-=1
# for i in range(len(z)):
#     z2.append(z[i])
#     z2_sort=sorted(z2)
#     print("Row {} : {}".format(i+1,z2_sort))
#----------------------------------------
# x=str(input())
# ticket=0
# tray=0
# x=x.split(" ")
# x[0]=int(x[0])
# x[1]=int(x[1])
# donut=x[0]//x[1]
# ticket+=donut
# tray+=donut
# while True: 
#     add_donut=ticket//2
#     add_donut+=tray//4
#     if add_donut>0:
#         ticket+=add_donut
#         tray+=add_donut
#         donut+=add_donut
#         ticket-=add_donut*2
#     tray+=add_donut
#     tray-=add_donut*4   
#     if ticket<2 and tray<4:
#         break
# ยังไม่เสร็จ
# ----------------------
# x=str(input())
# x=x.upper()
# x=x.split('')
# A_Z=[ chr(j) for j in range(65,91)]
# for i in range(len(x)):
# print(x)  
# x= list(input())
# ans=[]
# buffer=[]
# b="a e i o u A E I O U"
# b=b.split(" ")
# for i in range(len(x)):
#     if x[i] in b:
#         buffer.append(0)
#     else:
#         ans.append(x[i])

# print("".join(ans))
# ตัดสระภาษาอังกฤษ
# ----------------------
# def is_prime(n):
#     for i in range(2,n):
#         if n%i==0:
#             return False
#     return True
# เป็นจำนวนเฉพาะไหม
# ---------------------------    
# def replace(k,c):
#     a=[]
#     for i in range(c):
#         a.append("#")
#     if 1==1:
#         a[k]="*"    
#     arr="".join(a)
#     print(arr) 

# y=str(input())
# y=y.strip("()")
# y=y.split(",")
# x=int(input())
# if int(y[0])<=x and int(y[1])<=x:
#     for i in range(x):
#             print("#"*x)
#             if i==x-int(y[1])-1 :
#                 replace(int(y[0]),x)                  
# else:
#     print("That position is not loaded.")
# --------------------------------------------
# x=str(input())
# x=x.strip("[]")
# x=x.split(",")
# for k in range(len(x)):
#     x[k]=int(x[k])
# same=0
# for i in range(len(x)):
#     sum=0
#     for l in range(len(x)):
#         sum+=x[l]
#     sum=sum-x[i]-x[i]
#     if sum>0:
#         same+=1     
# if same==len(x):
#     print("True")
# else:
#     print("False")            
# number triangle in array
# ------------------------------------------------
# def is_prime(n):
#       for i in range(2,n):
#           if n%i==0:
#               return 0
#       return 1 
# x=int(input())
# a=[]
# buffer=[]
# for i in range(1,x+1):
#     if i==1:
#         buffer.append(i)
#     elif x%i==0: 
#         a.append(i)     
# for k in range(len(a)):
#     if  is_prime(a[k])==1:
#         print(a[k])
#     else:
#         buffer.append(a[k])
# ยังไม่เสร็จ
# ---------------------------------------- 
# import math
# l1=list(input())
# l2=list(input())
# for i in range(len(l1)):
#     if i<math.ceil(float(len(l1)/2)):
#         a=l1[i]
#         l1[i]=l1[len(l1)-1-i]
#         l1[len(l1)-1-i]=a    
#     else:
#         break;
# print(l1)
# x="".join(l1)
# y="".join(l2)
# ----------------------------------------
# x=int(input())
# y=str(x)
# z=0
# for i in range(len(y)):
#     if y[i]==y[len(y)-1-i]:
#         z+=1
#     if i==len(y)-len(y)//2-1:
#         break
# if z==len(y)-len(y)//2:
#     print("True") 
# else:
#     print("False")
    # palindrome_check

# -------------------------------------
# z1=[chr(j) for j in range(33,48)]
# z2=[chr(k) for k in range(58,125)]
# y=[]
# x=str(input())
# for i in range(len(x)):
#     if x[i] in z1 or x[i] in z2:
#         x=x.replace(x[i],"+")
# x=x.split("+")
# sum=0
# for j in range(len(x)):
#     if x[j]!='':
#         sum+=int(x[j])     
# ans="{}".format(str(sum))
# for k in range(len(ans)):
#     y.append(ans[k])
# while len(y)<4:
#     y.insert(0,"0")
# print("".join(y))
# รหัสบัตร ATM บวกกัน
# -----------------------------------------------------
# x=str(input())
# x=x.split(" ")
# for k in range(len(x)):
#     x[k]=int(x[k])
# d=x[1]
# d2=1
# for i in range(x[0]):
#     if i>=0 and i<d:
#         print("{}{}{}".format("-"*x[1],"*"*(x[0]-x[1]-x[1]),"-"*x[1]))        
#         x[1]-=1 
#     elif i>d-1 and i<x[0]-d:
#         print("*"*x[0])
#     elif i>=x[0]-d:
#         print("{}{}{}".format("-"*d2,"*"*(x[0]-d2-d2),"-"*d2))        
#         d2+=1 
# 8 2  
# --****--
# -******-
# ********
# ********
# ********
# ********
# -******-
# --****--
# ---------------------------------------------------
# x=int(input())
# z=1
# x2=x-1
# x3=x*2-1
# for i in range(1,x3+1):
#     if i>=1 and i<x:
#         print("{}{}{}".format(" "*x2,"*"*(x3-x2-x2)," "*x2))
#         x2-=1
#     elif i==x:
#         print("*"*x3)
#     elif i>x and i<=x3:
#         print("{}{}{}".format(" "*z,"*"*(x3-z-z)," "*z))
#         z+=1
# 4
#    *   
#   ***  
#  ***** 
# *******
#  ***** 
#   ***
#    *
# ------------------------------------------
# x=list(input())
# sum=0
# ans_dem=0
# for i in range(len(x)):
#     x[i]=ord(x[i])
#     x[i]=x[i]**(len(x))
#     sum+=x[i]
# sum_str=str(sum)
# b=[]
# for j in range(len(sum_str)):
#     b.append(int(sum_str[j]))
#     ans_dem+=b[j]
# ans_dem2=str(ans_dem)
# ans_dem3=str(ans_dem)
# while len(ans_dem2)>1:
#     ans_dem3=0
#     for j in range(len(ans_dem2)):
#         ans_dem3+=int(ans_dem2[j])
#     ans_dem2=str(ans_dem3)
# print(ans_dem2)
# รับค่าเป็นตัวอักษร จากนั้นทำการแปลงเป็น ตัวเลข
# เช่น a = 97 ,b= 98
# แล้วนำตัวเลขที่แปลงจากแต่ละตัวมาทำการยกกำลังด้วย จำนวนอักษรทั้งหมด เช่น abc
# แปลง a=97,b=98,c=99 แล้วมายกกำลังด้วยจำนวนตัวอักษรทั้งหมด คือ 3 (abc = 3 จำนวน)
# 97**3 =912673
# 98**3=941192
# 99**3=970299
# นำตัวเลขทั้งหมดมาบวกรวมกัน ได้ 2824164
# จากนั้นนำเลขทุกตัวมาบวกกันเรื่อยๆ จนเหลือ แค่ตัวเดียว
# ยกตัวอย่าง 
# 2+8+2+4+1+6+4= 27 => 2+7 =9
# -----------------------------------------------------------
# T=int(input())
# a=[]
# while T>0:
#     N=str(input())
#     N=N.split(" ")
#     a.append(N[0])
#     a.append(N[1])
#     T-=1
# for i in range(len(a)):

# for i in range(1,T+1):
#     print("Case #{}:{}".format(i,))
# -------------------------------------------------
# x=list(input())
# order=1
# for i in range(len(x)):
#     x[i]=ord(x[i])
#     x[i]-=order
#     x[i]=chr(x[i])
#     order+=1
# print(x)

# for  j in range(len(x)):
#     x[j]=ord(x[j])
#     if x[j]<91:
#         x[j]=x[j]+32
#         x[j]=chr(x[j])
#     elif x[j]>91:
#         x[j]=x[j]-32
#         x[j]=chr(x[j])
# print("".join(x))

# x=str(input())
# x=x.split(" ")
# ans=1
# Slim_Chub=int(x[0])
# Slim_Reg=0
# cage=int(x[0])
# while Slim_Chub>=0:
#     Slim_Chub-=int(x[1])
#     Slim_Reg+=int(x[1])
#     ans+=1
#     ans+=Slim_Chub




# def check_prime(x):
#     for i in range(2,x):
#         if x%i==0:
#             return 0;
#     return 1
# def sep(z):
#     a={}
#     for i in range(2,z+1):
#         if z%i==0 :
#             if i*i!=z:
#                 k=z//i
#                 i_bool=check_prime(i)
#                 k_bool=check_prime(k)
#                 a[i]=i_bool
#                 a[k]=k_bool
               
#                 for j in a:
#                     if a[j]==1:
#                         print(j)
#                     else:
#                         return sep(j);
#                 break
#             else:
#                 print(i)
#                 print(i)
#                 break
#     return ""       

# x=int(input())
# a=sep(x)
# print(a)
# แยกตปก
# def convert_to_number(x):
#     for i in range(len(x)):
#         x[i]=int(x[i])
#     return x
# price=int(input())
# pay=int(input())
# money_dict={}
# residue={}
# z=pay-price
# for i in range(6):
#     money=str(input())
#     money=money.split(" ")
#     money=convert_to_number(money)
#     money_dict[money[0]]=money[1]
# print("change: {}".format(z))
# for j in money_dict:
#     if j>z or money_dict[j]==0:
#         pass
#     else:
#         amount
# not finished yet
# def add_zero(x):
#     if len(str(x))==1:
#         z="00",str(x)
#         return z
#     if len(str(x))==2:
#         z="0",str(x)
#         return z
#     else:
#         z=str(x)
#         return z
# x=int(input())
# x=x**0.5
# sum=1
# for i in range(int(x)):
#     if i!=int(x)-2:
#         print("".join(add_zero(sum)))
#         sum+=1
#     if i==int(x)-1:
#         space="".join(add_zero(sum))," "
#         print("".join(space*int(x)))

# 001 008 007 
# 002 009 006 
# 003 004 005 



import math


a = -3
b = 0
accuracy = 1.0E-6


def func(x):
    return 2*x*math.cos(2*x) - (x+1)**2


def false_position_method(func, a, b, accuracy= 1.0E-6):
    iterations = 0
    while True:
        # print(a)
        # print(b)
        
        c = (a*func(b) - b*func(a)) / (func(b) - func(a))
        # print(c)
        # print("_______________")
       
        iterations += 1
        new_func(func, a, b, iterations, c)
       
        if func(c) == 0:
            # print("a")
            return c
            break
       
        if func(c) * func(a) < 0:
            b = c
        else:
            # print("H")
            a = c
            
        # print(a)
        # print(b)
        # print(c)
        if iterations>14:
            break
    return c


def new_func(func, a, b, iterations, c):
    print(f"Iteration {iterations}: a = {a:.8f}, b = {b:.8f}, c = {c:.8f}, f(c) = {func(c):.8f}")
a = -3
b = 0
accuracy = 1.0E-6

solution = false_position_method(func, a, b, accuracy)
print("\nApproximate solution:", solution)
print("Value of the equation at the approximate solution:", func(solution))
# Iteration round 1 F_X_R is -1.0
# Iteration round 1 F_X_L is -9.761021719902196
# Iteration round 1 F_X_M is -1.2716806404886092
# Iteration round 1 X_M is 0.34242581469521693
# Iteration round 1 X_L is -3.0
# Iteration round 1 X_R is 0.0
# Iteration round 2 F_X_R is -1.2716806404886092
# Iteration round 2 F_X_L is -9.761021719902196
# Iteration round 2 F_X_M is -3.591268890497056
# Iteration round 2 X_M is 0.8431122827091614
# Iteration round 2 X_L is -3.0
# Iteration round 2 X_R is 0.34242581469521693
# Iteration round 3 F_X_R is -3.591268890497056
# Iteration round 3 F_X_L is -9.761021719902196
# Iteration round 3 F_X_M is -10.533536163634569
# Iteration round 3 X_M is 3.0800981012984665
# Iteration round 3 X_L is -3.0
# Iteration round 3 X_R is 0.8431122827091614
# def f(a,b):
#     while b>0:
#         print(a)
#         print(b)
#         b-=1
#     return b
# b=3
# a=1
# s=f(a,b)
# print("s=",s)
    