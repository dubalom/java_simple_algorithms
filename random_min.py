from random import shuffle

def minimum(array):
    if len(array)==0:
        return None
    local_min=array[0]
    for element in array:
        if element<local_min:
            local_min=element
    return [local_min, local_min_index]

def random_array(lenght):
    array=[]
    for i in range(lenght):
        array.append(i)
    shuffle(array)
    return array

def index(array,a):
    for i in range(len(array)):
        if array[i] == a:
            return i
    return -1


        
        
