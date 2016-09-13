#calculate the factorial for a given number
x = int(input("Enter an integer: "))
count = 1
for i in range (1,x+1):
    count = count * i
print (count)
