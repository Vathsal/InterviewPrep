
#------------------------------------------------
# SELECTION SORT
#------------------------------------------------
import random 
def selection_sort(input_list):
    N = len(input_list)
    if N<=1 :
        return input_list
    else :
        for i in range(0, N) :
            smallest_index = i
            for j in range(i+1, N) :
                if input_list[smallest_index] > input_list[j] :
                    smallest_index = j
            input_list[i], input_list[smallest_index] = input_list[smallest_index], input_list[i]
    return input_list

# main program 
#input_list = [54,26,93,17,77,31,44,55,20]
#print("Unsorted Array : ", input_list)
#selection_sort(input_list)
#print("Sorted Array   : ", input_list)

input_list = random.sample(range(0, 1000000), 10000)
selection_sort(input_list)
f = open("selection_sort_result.txt", 'w')
f.write(str(input_list))
f.close()
