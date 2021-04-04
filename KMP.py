def computeLPSArray(find,findLength,findnumber):
    len = 0 

    findnumber[0] = 0 #lps[0] is always 0
    i = 1


    while i < findLength:
        if find[i] == find[len]:
            len += 1
            findnumber[i] = len
            i += 1

        else:
            if len != 0:
                len = findnumber[len - 1]

            else:
                findnumber[i] = 0
                i += 1

txt = "algorithmisfun"
find = "thm"

findLength = len(find)
txtLength = len(txt)


findnumber = [0]*findLength


computeLPSArray(find,findLength,findnumber)

i = 0 #index for txt[]
j = 0 
while i < txtLength : 
    if find[j] == txt[i]:
        i += 1
        j += 1

    if j == findLength:
        print ("Found pattern at index "+str(i-j))
        j = findnumber[j-1]

    elif i< txtLength and find[j] != txt[i]:
        if j != 0:
            j = findnumber[j-1]
        else:
            i +=1