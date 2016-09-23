#8_remove_duplicate_values_function.py
#A function that remove duplicate values from a list
#By: Al


def remove_duplicate_values(my_list):
     
    new_list = []
      
    for i in my_list:
         
        if i not in new_list:
            
            new_list.append(i)
     
    return new_list
