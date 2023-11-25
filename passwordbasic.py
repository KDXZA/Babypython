x=list(input())   
upper=0
lower=0
number=0
sig=0

if len(x)>=3 and len(x)<=20:
   for i in range(len(x)):
    for num in range(ord("0"),ord(":")):
        if x[i] in chr(num):
          number+=1 
    for num in range(ord(":"),ord("@")):
        if x[i] in chr(num):
          sig+=1
    for num in range(ord("["),ord("_")):
        if x[i] in chr(num):
          sig+=1
    for j in range(ord("!"),ord("/")):
       if x[i] in chr(j):
          sig+=1                                                          
    for m in range(ord("A"),ord("Z")):            
         if x[i] in chr(m):
           upper+=1 
    for p in range(ord("a"),ord("z")):             
         if x[i] in chr(p):
            lower+=1        
if(upper>=1 and lower>=1 and sig>=1 and number>=1):
   print("Valid.")
else:
   print("Invalid.")   