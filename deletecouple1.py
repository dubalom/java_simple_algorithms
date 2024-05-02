def deletecouple(spisok):
    spisok1 = []
    for i in spisok:
        if i not in spisok1:
            spisok1.append(i)
    return spisok1
spisok= [3,2,2,1]
print(deletecouple(spisok))
