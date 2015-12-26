#binary search implementation

def binarysearch(data, target, low, high):
	if low > high:
		return False
	else:
		mid = (low + high)//2
		if target == data[mid]:
			return True
		elif target > data[mid]:
			return binarysearch(data, target, mid+1, high)
		elif target < data[mid]:
			return binarysearch(data, target, low, mid-1)