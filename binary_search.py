def binary_search(array,element):
    position = 0
    mid = int(len(array)/2)
    while len(array)>1:
        if array[mid] == element:
            return position + mid
        elif array[mid] < element:
            position += mid + 1
            array = array[mid+1:]
            mid = int((len(array))/2)
        else:
            array = array[:mid]
            mid=int((len(array))/2)
    return position

array=[0,1,2,3,4,5,6,7,8]
print(binary_search(array,3))        
            
            
