def only_number(spisok):
    spisok1 = []
    for i in range(len(spisok)):
        for j in range(len(spisok)):
            if spisok[i] == spisok[j] and i != j:
                spisok1.append(spisok[i])
                #spisok1.append(spisok[j])
                

    spisok=set(spisok)
    spisok1=set(spisok1)
    return int(spisok.difference(spisok1))

                
spisok = [7,1,2,1,2,5,5,6,3,3,6,4,8,8,7]
print(only_number(spisok))
