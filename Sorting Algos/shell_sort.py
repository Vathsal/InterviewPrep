
#------------------------------------------------
# SHELL SORT
#------------------------------------------------
import random
def shell_sort_1(input_list) :
    N = len(input_list)
    gap = N//2
    while (gap > 0):
        for index in range(gap,N):
            while index>=gap and input_list[index-1] > input_list[index]:
                input_list[index], input_list[index-1] = input_list[index-1], input_list[index]
                index -= gap     
        gap //= 2
    return input_list


def shell_sort_2(input_list) :
    count =0
    N = len(input_list)
    gap = N//2
    while (gap > 0):
        for i in range(gap,N):
            while i>=gap and input_list[i] < input_list[i-gap]:
                input_list[i], input_list[i-gap] = input_list[i-gap], input_list[i]
                count+=1
                i -= gap 
            #print(input_list)
        gap //= 2
    print(count)
    return input_list
    
def shell_sort_3(input_list) :
    count = 0 
    N = len(input_list)
    gap = N//2
    while (gap > 0):
        for i in range(gap,N):
            j =i
            while j>=gap and input_list[j] < input_list[j-gap]:
                input_list[j], input_list[j-gap] = input_list[j-gap], input_list[j]
                count+=1
                j -= gap 
            #print(input_list)
        gap //= 2
    return input_list


# main program 
#input_list_1 = [54,26,93,17,77,31,44,55,20]
#print("Unsorted Array : ", input_list_1)
#shell_sort_1(input_list_1)
#print("Sorted Array   : ", input_list_1)
#
#input_list_2 = [54,26,93,17,77,31,44,55,20]
#print("Unsorted Array : ", input_list_2)
#shell_sort_2(input_list_2)
#print("Sorted Array   : ", input_list_2)
#
#input_list_3 = [54,26,93,17,77,31,44,55,20]
#print("Unsorted Array : ", input_list_3)
#shell_sort_3(input_list_3)
#print("Sorted Array   : ", input_list_3)

input_list_1 = random.sample(range(0, 1000000), 10000)
shell_sort_1(input_list_1)
f = open("shell_sort_1_result.txt", 'w')
f.write(str(input_list_1))
f.close()

input_list_2 = random.sample(range(0, 1000000), 10000)
shell_sort_2(input_list_2)
f = open("shell_sort_2_result.txt", 'w')
f.write(str(input_list_2))
f.close()

input_list_3 = random.sample(range(0, 1000000), 10000)
shell_sort_3(input_list_3)
f = open("shell_sort_3_result.txt", 'w')
f.write(str(input_list_3))
f.close()


