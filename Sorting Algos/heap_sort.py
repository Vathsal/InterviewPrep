
#------------------------------------------------
# HEAP SORT
#------------------------------------------------
import random 
def heap_sort(input_list) :
    N = len(input_list)
    if N <=1 :
        return input_list
    else :
        build_max_heap(input_list, N)
        for i in range(N-1, 0, -1) :
            input_list[0], input_list[i] = input_list[i], input_list[0]
            heapify(input_list, i, 0)
    return input_list

def build_max_heap(input_list, N) :
    for i in range(N, 0, -1) :
        heapify(input_list, N, i)
    return input_list

def heapify(input_list, N, index) :
    # Find largest among root(index), left child(left_index) and right child(right_index)
    largest_index = index
    left_index = 2*index + 1 
    right_index = 2*index + 2
    
    if left_index < N and input_list[left_index] > input_list[index] :
        largest_index = left_index
        
    if right_index < N and input_list[right_index] > input_list[largest_index] :
        largest_index = right_index
    
    # Initially the root(index) was the largest. If root is not largest => largest has changed  
    # and we need to swap the largest with the index. Swap with largest and continue heapifying
    if largest_index != index :
        input_list[largest_index], input_list[index] = input_list[index], input_list[largest_index]
        heapify(input_list, N, largest_index)
        
    return input_list

# main program 
#input_list = [54,26,93,17,77,31,44,55,20]
#print("Unsorted Array : ", input_list)
#heap_sort(input_list)
#print("Sorted Array   : ", input_list)

input_list = random.sample(range(0, 1000000), 10000)
heap_sort(input_list)
f = open("heap_sort_result.txt", 'w')
f.write(str(input_list))
f.close()
