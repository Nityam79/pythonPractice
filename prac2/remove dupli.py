
def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list
     

duplicate = [9, 7, 11, 21, 5, 9, 16, 34]
print(Remove(duplicate))