def dictionary_switch(dictionary):
    new_dict = {}
    for i in dictionary:
        new_dict[dictionary[i]] = i
    return new_dict

    
    
        
dictionary = dictionary_switch({ 1: "a", 2: "b", 3: "c"})
print(dictionary)    
