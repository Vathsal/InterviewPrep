
#------------------------------------------------
# BUBBLE SORT
#------------------------------------------------

# Without swap counter
def bubble_sort_1(input_list) :
    N = len(input_list)
    
    if N <=1 :
        return input_list
    else :
        for i in range(N) :
            for j in range(N-i-1) :
                if input_list[j] > input_list[j+1] :
                    input_list[j], input_list[j+1] = input_list[j+1],input_list[j]
    
    return input_list

# With swap counter
def bubble_sort_2(input_list) :
    N = len(input_list)
    swap_counter = -1
    
    if N <=1 :
        return input_list
    else :
        while swap_counter != 0 :
            swap_counter = 0 
            for i in range(N) :
                for j in range(N-i-1) :
                    if input_list[j] > input_list[j+1] :
                        input_list[j], input_list[j+1] = input_list[j+1],input_list[j]
                        swap_counter += 1
    
    return input_list

# main program 
input_list_1 = [54,26,93,17,77,31,44,55,20]
print("Unsorted Array : ", input_list_1)
bubble_sort_1(input_list_1)
print("Sorted Array   : ", input_list_1)

input_list_2 = [54,26,93,17,77,31,44,55,20]
print("Unsorted Array : ", input_list_2)
bubble_sort_2(input_list_2)
print("Sorted Array   : ", input_list_2)
