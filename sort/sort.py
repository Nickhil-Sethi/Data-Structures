from typing import List

def is_sorted(arr: List) -> bool:
	c = 0
	while c < len(arr) - 1:
		if arr[c] > arr[c+1]:
			return False
		c += 1
	return True

def bubble_sort(arr: List) -> List:
	swap = True
	while swap:
		c = 0
		swap = False
		while c < len(arr) - 1:
			if arr[c] < arr[c+1]:
				c += 1
				continue 
			arr[c], arr[c+1] = \
				arr[c+1], arr[c]
			swap = True
			c += 1
	return arr

def merge(a: List, b: List) -> List:
	mergedList = []
	c = 0
	d = 0
	while c < len(a) and d < len(b):
		if a[c] < b[d]:
			mergedList.append(a[c])
			c += 1
		else:
			mergedList.append(b[d])
			d += 1

	while c < len(a):
		mergedList.append(a[c])
		c += 1
	
	while d < len(b):
		mergedList.append(b[d])
		d += 1
	
	return mergedList

def merge_inplace(
		arr: List, 
		begin: int, 
		mid: int, 
		end: int) -> List:

	mergedList = []
	c = begin 
	d = mid + 1
	while c <= mid and d <= end:
		if arr[c] < arr[d]:
			mergedList.append(arr[c])
			c += 1
		else:
			mergedList.append(arr[d])
			d += 1
	
	while c <= mid:
		mergedList.append(arr[c])
		c += 1
	
	while d <= end:
		mergedList.append(arr[d])
		d += 1

	for i in range(begin, end+1):
		arr[i] = mergedList[i-begin]

	return arr

def merge_sort(arr: List, begin=None, end=None) -> List:
	if begin == None:
		begin = 0

	if end == None:
		end = len(arr) - 1

	if begin == end:
		return arr

	mid = (begin + end) // 2

	# recursibely sort the left and right halves
	arr = merge_sort(arr, begin, mid)
	arr = merge_sort(arr, mid+1, end)

	# merge the two halves into another list
	merge_inplace(arr, begin, mid, end)	
	return arr

if __name__ == '__main__':
	s1 = ['z','a','b', 'd', 's', 'e', 'h', 'r']
	assert(is_sorted(bubble_sort(s1)))