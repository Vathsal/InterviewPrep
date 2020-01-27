
#------------------------------------------------
# HEAP SORT
#------------------------------------------------

def heap_sort(input_list) :
    N = len(input_list)
    
    build_max_heap(input_list, N)
    
    for i_index in range(N-1, 0, -1) :
        input_list[0], input_list[i_index] = input_list[i_index], input_list[0]
        heapify(input_list, i_index, 0)
    
    return input_list

def build_max_heap(input_list, input_list_len) :
    for i_index in range(input_list_len, 0, -1) :
        heapify(input_list, input_list_len, i_index)
    return input_list

def heapify(input_list, input_list_len, index) :
    # Find largest among root, left child and right child
    largest_index = index
    left_index = 2*index + 1 
    right_index = 2*index + 2
    
    if left_index < input_list_len and input_list[left_index] > input_list[index] :
        largest_index = left_index
        
    if right_index < input_list_len and input_list[right_index] > input_list[largest_index] :
        largest_index = right_index
    
    # If root is not largest, swap with largest and continue heapifying
    if largest_index != index :
        input_list[largest_index], input_list[index] = input_list[index], input_list[largest_index]
        heapify(input_list, input_list_len, largest_index)
        
    return input_list

# main program 
input_list = [54,26,93,17,77,31,44,55,20]
print("Unsorted Array : ", input_list)
heap_sort(input_list)
print("Sorted Array   : ", input_list)