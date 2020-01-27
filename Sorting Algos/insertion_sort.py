
#------------------------------------------------
# INSERTION SORT
#------------------------------------------------

def insertion_sort(input_list) :
    N = len(input_list)

    if N <=1 :
        return input_list
    else :
        for i in range(1,N):
            while i > 0 and input_list[i-1] > input_list[i]:
                input_list[i], input_list[i-1] = input_list[i-1], input_list[i]
                i -=1   

    return input_list

# main program 
input_list = [54,26,93,17,77,31,44,55,20]
print("Unsorted Array : ", input_list)
insertion_sort(input_list)
print("Sorted Array   : ", input_list)