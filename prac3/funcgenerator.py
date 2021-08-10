def simpleGeneratorFun(): 
    yield 7            
    yield 8            
    yield 9            
   
for value in simpleGeneratorFun(): 
    print(value)