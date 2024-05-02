def delete_couple(spisok):
    i = 0
    spisok1 = []
    while i < len(spisok):
        if spisok[i] not in spisok1:
            spisok1.append(spisok[i])
        i += 1
    return spisok1
spisok = [30,20,20,10,40,10,40,20,30,50,30]
print(delete_couple(spisok))
