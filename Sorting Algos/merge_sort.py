
#------------------------------------------------
# MERGE SORT
#------------------------------------------------
import random
def merge_sort(input_list) :
    N = len(input_list)
    if N<=1 :
        return input_list
    else :
        left_list,right_list = split(input_list)
        return merge_sorted_lists(merge_sort(left_list), merge_sort(right_list))

def split(input_list) :
    N = len(input_list)
    mid_index = N//2
    return input_list[:mid_index], input_list[mid_index:]
 
def merge_sorted_lists(input_list1, input_list2) :
        i, j = 0, 0
        result_list = []
        N1 = len(input_list1)
        N2 = len(input_list2)
    
        if N1 == 0 :
            return input_list2
        elif N2 == 0 :
            return input_list1
    
        while len(result_list) <= (N1+N2) :
            if input_list1[i] <= input_list2[j] :
                result_list.append(input_list1[i])
                i += 1
            else :
                result_list.append(input_list2[j])
                j += 1

            if i == N1 :
                result_list += input_list2[j:]
                break
            elif j == N2 :
                result_list += input_list1[i:]
                break
        
        return result_list

# main program 

#input_list = [54,26,93,17,77,31,44,55,20]
#print("Unsorted Array : ", input_list)
#output_list = merge_sort(input_list)
#print("Sorted Array   : ", output_list)

input_list = random.sample(range(0, 1000000), 1000000)
output_list = merge_sort(input_list)
f = open("merge_sort_result.txt", 'w')
f.write(str(output_list))
f.close()