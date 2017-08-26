# change string to list
def listChange(string):
    lizt = []
    for i in range(len(string)):
        lizt.append(string[i])
    return(lizt)

# look for Empty space
# steps validity and count
def initialize (lizt):
    valid = []
    for i in range(len(lizt)):
        if lizt[i] == 'E':
            start = i
    step1 = start + 1
    step2 = start + 2
    step3 = start + 3
    step4 = start - 1
    step5 = start - 2
    step6 = start - 3
    if (0 <= step1 < len(lizt)):
        valid.append('1R')
    if (0 <= step2 < len(lizt)):
        valid.append('2R')
    if (0 <= step3 < len(lizt)):
        valid.append('3R')
    if (0 <= step4 < len(lizt)):
        valid.append('1L')
    if (0 <= step5 < len(lizt)):
        valid.append('2L')
    if (0 <= step6 < len(lizt)):
        valid.append('3L')
    return valid

# expand
def expansionCost(validMoves, string2):
    expand = []
    cost = 0
    for i in range(len(validMoves)):
        for j in range(len(string2)):
            if string2[j] == 'E':
                if validMoves[i] == '1R':
                    string2[j],string2[j+1] = string2[j+1],string2[j]
                    string3 = string2[:]
                    expand.append(string3)
                    cost = cost + 1
                    expand[i].insert(len(string3),cost)
                    cost = 0
                    string2[j],string2[j+1] = string2[j+1],string2[j]

                if validMoves[i] == '2R':
                    string2[j],string2[j+2] = string2[j+2],string2[j]
                    string3 = string2[:]
                    expand.append(string3)
                    cost = cost + 1
                    expand[i].insert(len(string3),cost)
                    cost = 0
                    string2[j],string2[j+2] = string2[j+2],string2[j]

                if validMoves[i] == '3R':
                    string2[j],string2[j+3] = string2[j+3],string2[j]
                    string3 = string2[:]
                    expand.append(string3)
                    cost = cost + 2
                    expand[i].insert(len(string3),cost)
                    cost = 0
                    string2[j],string2[j+3] = string2[j+3],string2[j]

                if validMoves[i] == '1L':
                    string2[j],string2[j-1] = string2[j-1],string2[j]
                    string3 = string2[:]
                    expand.append(string3)
                    cost = cost + 1
                    expand[i].insert(len(string3),cost)
                    cost = 0
                    string2[j],string2[j-1] = string2[j-1],string2[j]

                if validMoves[i] == '2L':
                    string2[j],string2[j-2] = string2[j-2],string2[j]
                    string3 = string2[:]
                    expand.append(string3)
                    cost = cost + 1
                    expand[i].insert(len(string3),cost)
                    cost = 0
                    string2[j],string2[j-2] = string2[j-2],string2[j]

                if validMoves[i] == '3L':
                    string2[j],string2[j-3] = string2[j-3],string2[j]
                    string3 = string2[:]
                    expand.append(string3)
                    cost = cost + 2
                    expand[i].insert(len(string3),cost)
                    cost = 0
                    string2[j],string2[j-3] = string2[j-3],string2[j]

    return expand

# gn function
def gn(enlarge):
    gnfunction = enlarge[:]
    gnList = []
    for i in range(len(gnfunction)):
        for j in range(len(gnfunction[i])):
            gnValue = gnfunction[i][-1]
        gnList.append(gnValue)

    return gnList


# hn function
def hn(enlarge):
    hnfunction = enlarge[:]
    hnList = []
    countz = 0 
    for i in range(len(hnfunction)):
        for j in range(len(hnfunction[i])):
            if hnfunction[i][j] == 'B':
                for k in range(j,len(hnfunction[i])-1):
                    if hnfunction[i][k] == 'W':
                        countz = countz + 1
                        hnfunction[i][k] = '_'
                        break
        hnList.append(countz)
        countz = 0
    return hnList


# fn function
def fn(gnValu, hnValu):
    addition = []
    for i in range(len(gnValu)):
        for j in range(len(hnValu)):
            if i == j:
                x = gnValu[i] + hnValu[j]
                addition.append(x)
                
    return addition 

# changebackkkkkkk for ancestor omg 
def changeBack(enlarge):
    for i in range(len(enlarge)):
        for j in range(len(enlarge[i])):
            if enlarge[i][j] == '_' :
                enlarge[i][j] = 'W'
    return enlarge             

# pick min valu(s)
def minValus(fnValu):
    minIndex = []
    smallest = min(fnValu)
    for index, element in enumerate(fnValu):
            if smallest == element: # check if this element is the minimum_value
                    minIndex.append(index) # add the index to the list if it is
s
    return smallest, minIndex
            
##############################--TESTINGAREA--###################################

string = 'WEBBW'
stringList = listChange(string)

lc = listChange(string)
##print(lc)
check = hn(lc)
##print(check)
validMoves = initialize(lc)
##print(validMoves)
##print('this one:' + str(stringList))
enlarge = expansionCost(validMoves,stringList)
##print('enlarge' + str(enlarge))
gnValu = gn(enlarge)
print(gnValu)
##print('gn' + str(enlarge))
hnValu = hn(enlarge)
print(hnValu)
##print('hn' + str(enlarge))
##printz(enlarge)
##checkancestor(enlarge)
fnValu = fn(gnValu,hnValu)
print(fnValu)
##print('fn' + str(enlarge))
ohgod = changeBack(enlarge)
print(ohgod)
findmin = minValus(hnValu)
print(findmin)

