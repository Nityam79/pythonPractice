num = int(input("Enter the number: "))
f = 1


for i in range (1, num+1):
    f = f*i


print ("Factorial of the number %d is %d" %(num, f))