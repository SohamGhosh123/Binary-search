print("binarysearch")
def binarySearch(arr1,start,end,x):
    if end>=start:
        mid=start+(end-start)//2
        if arr1[mid]==x:
            return mid
        elif arr1[mid]>x:
            return binarySearch(arr1,start,mid-1,x)
        else:
            return binarySearch(arr1,mid+1,end,x)
    else:
        return -1
arr1=sorted(["a","b","c","d"])
x=input("What is your number?")
result=binarySearch(arr1,0,len(arr1)-1,x)
if result!=-1:
    print("Element is present"+str(result))
else:
    print("Element is not present")