def shortest_word(spisok):
    min_word = spisok[0]
    for i in spisok:
        if len(i) < len(min_word):
            min_word = i
    return len(min_word)
        
spisok = [ 'abc', 'b']
print(shortest_word(spisok))
def longest_prefix(spisok):
    result =''
    if spisok == []:
        return ''
    for i in range (shortest_word(spisok)):
        for j in range (len(spisok)):
            if spisok[j][i] != spisok[0][i]:
                return result
        result = result+ spisok[0][i]
    return result
spisok = ['flower', 'flow']
print(longest_prefix(spisok))
        
            
            
        
        
            
