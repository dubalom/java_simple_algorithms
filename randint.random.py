from random import shuffle,randint, choice

def minimum(array):
    if len(array)==0:
        return None
    local_min=array[0]
    local_min_index=0
    for index in range(len(array)):
        element=array[index]
        if element<local_min:
            local_min=element
            local_min_index=index
    return [local_min,local_min_index]
def randint_(a,b):
    array=[a::b]
    for i in range(array):
        array.choice()
    return array

def random_array(lenght):
    array=[]
    for i in range(lenght):
        array.append(randint(0,lenght))
    return array

array=random_array(20)
print(minimum(array))

