def only_element(spisok):
    array=[]
    for i in range(len(spisok)):
        flag=True
        for j in range (len(spisok)):
            if flag and spisok[j] == spisok[i] and i!=j:
                array.append(spisok[i])
                flag=False
    return len(spisok)!=len(array)

                

def valid_string(string):
    list_ = []
    for i in range(len(string)):
        if string[i] == "(" or "{" or "[":
            list_.append(string[i])
        else:
            if list_ == ["("]:
                if string[i] == ")":
                    list_.append(string[i])
            
            if list_ == ["["]:
                if string[i] == "]":
                    list_.append(string[i])
            if list_ == ["{"]:
                if string[i] == "}":
                    list_.append(string[i])
        for j in range(len(list_)-1):
            if list_[j] == "(" or "{" or "{" and list_[j+1] == ")" or "}" or "]":
                list_.pop(j)
                list_.pop(j)
                if list_[j] == 0:
                    return True
                return False
                        
                        
                    
       

def test_function():
    test_array={"()":True,"()[]{}":True,"(]":False,
                "([)]":False,"([])":True,"(":False,"":True}
    for key in test_array.keys():
        print(key,valid_string(key),test_array[key])
string = '([])'
print(valid_string(string))
