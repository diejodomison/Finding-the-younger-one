n1 = input() 
d1 = input() 
n2 = input() 
d2 = input() 
if d1==d2: 
    if n1<n2 : 
        print(n1) 
    else : 
        print(n2) 
elif d1[-4:] != d2[-4:] : 
    if int(d1[-4:]) < int(d2[-4:]): 
        print(n2) 
    else : 
        print(n1) 
elif d1[3:5] != d2[3:5]: 
    if int(d1[3:5]) < int(d2[3:5]): 
        print(n2) 
    else : 
        print(n1) 
else : 
    if int(d1[0:2]) < int(d2[0:2]): 
        print(n2) 
    else : 
        print(n1) 
