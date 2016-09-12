
# coding: utf-8

# In[ ]:

import math
import sys
while True:
    try:
        a = float(input("Please enter a"))
        b = float(input("Please enter b"))
        c = float(input("Please enter c")) 
        x1 = (-b+math.sqrt(b**2-4*a*c))/(2*a) #calculate first solution
        x2 = (-b-math.sqrt(b**2-4*a*c))/(2*a) #calculate second solution
        break
    except ValueError:# if the b**2-4ac<0, math.sqrt will print ValueError
        print("can't solve negative square root") #execute exception
        sys.exit() #quit program 
    finally: #if no error occur, print solutions. 
        print (x1,x2)


# alternate method, use if instead of try
import math
import sys
a = float(input("Please enter a"))
b = float(input("Please enter b"))
c = float(input("Please enter c"))
if b**2-4*a*c < 0:
    print ("error, can't solve negative square root")
    sys.exit()
else:
    x1 = (-b+math.sqrt(b**2-4*a*c))/(2*a)
    x2 = (-b-math.sqrt(b**2-4*a*c))/(2*a)
print (x1,x2)
