def function_sort(array):
    for i in range(len(array)):
        for j in range(len(array)-1-i):
            if array[j] > array[j+1]:
                first = array[j]
                array[j] = array[j+1]
                array[j+1] = first
    return array
                
                
array=[4,2,1,6]
print(function_sort(array))
            
