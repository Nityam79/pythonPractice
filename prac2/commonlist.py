def common_data(list1, list2):
    result = False
  
    
    for x in list1:
  
       
        for y in list2:
    
           
            if x == y:
                result = True
                return result 
                  
    return result
      
# driver code
a = [11, 12, 13, 14, 15]
b = [15, 16, 17, 18, 19]
print(common_data(a, b))
  
a = [11, 12, 13, 14, 15]
b = [16, 17, 18, 19]
print(common_data(a, b))