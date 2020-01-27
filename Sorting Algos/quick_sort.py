
#------------------------------------------------
# QUICK SORT
#------------------------------------------------

def quick_sort(input_list) :
	N = len(input_list)
	if N<=1 :
		return input_list 
	else :
		return quick_sort_helper(input_list, 0, N-1)

# sp = start_pointer, ep = end_pointer, pp = pivot_pointer
def quick_sort_helper(input_list, sp, ep) :
	if sp>=ep :
		return
	pp = partition(input_list, sp, ep)
	quick_sort_helper(input_list, sp, pp-1)
	quick_sort_helper(input_list, pp+1, ep)

def partition(input_list, sp, ep):
    follower = leader = sp
    while leader < ep:
        if input_list[leader] <= input_list[ep]:
            input_list[follower], input_list[leader] = input_list[leader], input_list[follower]
            follower += 1
        leader += 1
    input_list[follower], input_list[ep] = input_list[ep], input_list[follower]
    return follower

# main program 
input_list = [54,26,93,17,77,31,44,55,20]
print("Unsorted Array : ", input_list)
quick_sort(input_list)
print("Sorted Array   : ", input_list)
