list=[9,7,6,1,8,2,65,234,235,4]

def merge(left,right):
    result=[]
    i=j=0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(list):
    if len(list)<=1:
        return list
    mid=len(list)//2
    left=merge_sort(list[:mid])
    right=merge_sort(list[mid:])
    a=merge(left,right)
    return a
print(merge_sort(list))

