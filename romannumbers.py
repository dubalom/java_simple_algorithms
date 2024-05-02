def rome_numbers(number):
    result= []
    for symbol in number:
        if symbol == 'I':
            result.append(1)
        elif symbol == 'V':
            result.append(5)
        elif symbol == 'X':
            result.append(10)
        elif symbol == 'L':
            result.append(50)
        elif symbol == 'C':
            result.append(100)
        elif symbol == 'D':
            result.append(500)
        elif symbol == 'M':
            result.append(1000)

   
    arabic = 0
    for i in range(len(result)):
        if i == len(result) - 1:
           if result[i-1] > result[i]:
                arabic+= result[i]
               
        elif result[i] < result[i+1]:
                arabic +=  result[i+1] - result[i]
        else:
            arabic+= result[i]
    return arabic

                   
number= 'XXIX'
print (rome_numbers(number))

