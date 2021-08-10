from functools import reduce num=[134,434,234,34,16,165,3165,316]

num_first=list(filter(lambda n:n%3==0,num))
print(num_first) 
 num_new=list(map(lambda n:n*2/10,num)) 
print (num_new) 
sum=reduce (lambda m,n:m+n, num)
print(sum)