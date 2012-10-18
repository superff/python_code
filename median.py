def median(arr1, arr2):
	new_Arr = arr1 + arr2
	new_Arr.sort()
	if len(new_Arr) % 2 == 1:
		#print new_Arr
		return new_Arr[len(new_Arr)/2]
	else:
		mid = (len(new_Arr)-1)/2
		return (new_Arr[mid] + new_Arr[mid +1])/2



def binarySearch(tar,arr,start,end):
	mid = start + end;
	if tar < arr[start]:
		return start
	elif tar == arr[start]:
		return start + 1
	elif tar >= arr[end]:
		return end + 1
	else:
		mid = (start + end)/2
		if tar == arr[mid]:
			return mid + 1
		elif tar > arr[mid]:
			return binarySearch(tar,arr,mid + 1,end)
		else:
			return binarySearch(tar,arr,start,mid-1)



arr1 = [2,4,6,7]
arr2 = [1,5,7,8,8,9,10]
print len(arr1)
print arr1
print len(arr2)
print arr2
print median(arr1,arr2)


total = len(arr1) + len(arr2)

#print medianRes(arr1,arr2,0,len(arr1)-1,0,len(arr2)-1,total)

print binarySearch(8,arr2,0,len(arr2)-1)





