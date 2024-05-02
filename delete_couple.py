def delete_couple_dict(spisok):
    new_spisok={}
    for i in range(len(spisok)):
        if spisok[i] not in new_spisok.keys():
            new_spisok.update({spisok[i]:None})
    return list(new_spisok.keys())
            
    
    

dictionary = [30,20,20,10,40,10,40,20,30,50,30]
print(delete_couple_dict(dictionary))

