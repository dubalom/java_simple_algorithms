def delete_couple_list(spisok):
    i=0
    while i<len(spisok):
        first=spisok[i]
        j=0
        while j<len(spisok):
            second=spisok[j]
            if i!=j and first==second:
                spisok.pop(j)
            j+=1
        print(spisok)
        i+=1
    return spisok
spisok = [30,20,20,10,40,10,40,20,30,50,30]
print(delete_couple_list(spisok))
