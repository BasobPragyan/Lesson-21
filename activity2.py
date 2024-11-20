def match_word(words):
    count=0
    lis=[]
    for word in words:
        if len(word)>1 and word[0]==word[-1]:
            count+=1
            lis.append(word)
    print(lis)
    return count
totalcount=match_word(['mom','75575757','Manchester United'])
print("Words with same first and lats letter are: ",totalcount)