def minimum(array):
    if len(array) == 0:
        return None
    local_min = array[0]
    for element in array:
        if element < local_min:
            local_min = element
    return local_min
                
def index(array,a):
    for i in range(len(array)):
        if array[i] == a:
            return i
    return -1
array = [2,4,1,5,6]
print(minimum(array),index(array,minimum(array)))
