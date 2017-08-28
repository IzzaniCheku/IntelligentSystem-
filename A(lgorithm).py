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
    cost = 0                            # g(n) value
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



# hn function
def hn (asdf):
    hn = [] 
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
    hn.append(track)
    track = 0 
    return hn

 
##############################--INITIALIZING--###################################

string = 'BBWWE'
stringList = listChange(string)

database = []
temp = [] 
hFunction = hn(stringList)
gFunction = 0
fFunction = hFunction[0]  + gFunction 
temp.append(stringList)                 # string 
temp.append(gFunction)                  # g(n) value
temp.append(hFunction[0])               # h(n) value
temp.append(fFunction)                  # f(n) value
temp.append(None)                       # parent 
temp.append(None)                       # move 
database.append(temp)


OPEN = []
CLOSE = []

OPEN.append(stringList)

##############################--LOOPPOINT--###################################

w = open("output.txt", "w") #write at output.txt

while True :
    end = False
    fList = []
    for i in range(len(OPEN)):
        for j in range(len(database)): 
            if OPEN[i] == database[j][0]: 
                tempList = [] 
                tempList.append(database[j][3]) # f(n) value
                tempList.append(OPEN[i])        # string 
                tempList.append(database[j][5]) # move 
                fList.append(tempList)
                
    small = min(fList)
    small = small[0]
    smallest = []
    preferred = [] 
    if fList.count(small) > 1:
        for i in range(len(fList)):
            if fList[i][0] == small:
                smallest.append(fList[i])
        for j in range(len(smalls)):            # favoritism check 
            if smallest[j][-1] == '2R' or smallest[j][-1] == '3R':
                preferred.append(smallest[j])  
                if len(prefered) == 1:
                    node = preferred[1]
                else:
                    node = smallest[0][1]
                    
    for i in range(len(fList)):
        if fList[i][0] == small:
            node = fList[i][1]
                
    validMoves = initialize(node)
    expand = expansionCost(validMoves,node)
    
    for i in range(len(database)):
        if database[i][0] == node:
            parentsG = database[i][1]
            break
        
    for i in range(len(expand)):
            childG = expand[i].pop(-1)
            sTring = expand[i]
            move = validMoves[i]
            gnValu = parentsG + childG
            heuristic = hn(expand[i])
            if heuristic[0] == 0:
                end = True
            fnValu = gnValu + heuristic[0]
            tempList = [] 
            tempList.append(sTring)
            tempList.append(gnValu)
            tempList.append(heuristic[0])
            tempList.append(fnValu)
            tempList.append(node)
            tempList.append(move)
            if sTring not in CLOSE:             # check for ancestor 
                database.append(tempList)
                OPEN.append(sTring)
            if end == True:
                sol = sTring
                break
            
    if end == True:
        break
    
    CLOSE.append(node)
    
    for i in range(len(OPEN)):
        if OPEN[i] == node:
            del OPEN[i]
            break
        
solution = []
backtrack = sol
while backtrack != None:                        # backtracking
    for i in range(len(database)):
        if backtrack == database[i][0]:
            tepm = []
            tepm.append(database[i][-1])
            tepm.append(database[i][0])
            tepm.append(database[i][1])
            solution.append(tepm)
            backtrack = database[i][4]

for i in range(len(solution)):
    if solution[i][0] == None:
        solution[i][0] = 'start'
        for j in reversed(solution):
            w.write(str(j) + '\n')
    
w.close()
