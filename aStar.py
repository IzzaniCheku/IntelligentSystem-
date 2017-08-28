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
    expand = [] # open list 
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

# first hn
def hnfirst (asdf):
    hnList2 = [] 
    track = 0
    stringList = []
    for i in range(len(asdf)):
        stringList.append(asdf[i])
    for i in range(len(stringList)):
        if stringList[i] == 'B':
            for j in range(i,len(stringList)):
                if stringList[j] == 'W':
                    track = track + 1
                    stringList[j] = '_'
                    break
    hnList2.append(track)
    track = 0 
##    print(stringList)
    return hnList2

# hn function
def hn(asdf):
    hnfunction = []
    hnList = []
    countz = 0
    for i in range(len(asdf)):
        hnfunction.append(asdf[i])
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
##        print(enlarge)
##        print(hnfunction)
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

    return smallest, minIndex

# favoritism
##def favoritism (enlarge):

    
##############################--TESTINGAREA--###################################

string = 'BBWWE'
stringList = listChange(string)

database = []
temp = [] 
hFunction = hnfirst(stringList)
gFunction = 0
fFunction = hFunction[0]  + gFunction 
print(fFunction)
temp.append(stringList)
temp.append(gFunction)
temp.append(hFunction[0])
temp.append(fFunction)
temp.append(None)
temp.append(None)
database.append(temp)
##temp = []
print(database)

openList = []
closeList = []

openList.append(stringList)
print(openList)

##############################--LOOPPOINT--###################################
'''
todo: check ancestors!
todo: favoritism!
todo: eat first!
'''
while True :
    end = False
    fList = []
    tempList = []
    for i in range(len(openList)):
        for j in range(len(database)):
            if openList[i] == database[j][0]:
                tempList.append(database[j][3])
                tempList.append(openList[i])
                fList.append(tempList)
    #print(fList)
    small = min(fList)
    #print(small)
    potter = fList[0][1] # chosen one
    validMoves = initialize(potter)
    print(validMoves)
    expand = expansionCost(validMoves,potter)
    #print(expand)
    for i in range(len(database)):
        if database[i][0] == potter:
            parentsG = database[i][1]
            break
    for i in range(len(expand)):
        #for j in range(len(expand[i])):
            childG = expand[i].pop(-1)
            sTring = expand[i]
            move = validMoves[i]
            finalG = parentsG + childG
            heurs = hnfirst(expand[i])
            if heurs[0] == 0:
                end = True
            eff = finalG + heurs[0]
            tempList = [] 
            tempList.append(sTring)
            tempList.append(finalG)
            tempList.append(heurs[0])
            tempList.append(eff)
            tempList.append(potter)
            tempList.append(move)
            database.append(tempList)
            openList.append(sTring)
            if end == True:
                sol = sTring
                break
    if end == True:
        print('found the end!')
        break
    closeList.append(potter)
    for i in range(len(openList)):
        if openList[i] == potter:
            del openList[i]
            break
    print('\n')
    #print(database)

print(sol)         

print('\n')
view = []
whereufrom = sol
while whereufrom != None:
    for i in range(len(database)):
        if whereufrom == database[i][0]:
            tepm = []
            tepm.append(database[i][3])
            tepm.append(database[i][0])
            tepm.append(database[i][-1])
            view.append(tepm)
            whereufrom = database[i][4]

        
for i in range(len(view)):
    print(view[i])
            
            
        



