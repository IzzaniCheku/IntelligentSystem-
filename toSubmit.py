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
    if (0 <= start + 1 < len(lizt)):
        valid.append('1R')
    if (0 <= start + 2 < len(lizt)):
        valid.append('2R')
    if (0 <= start + 3 < len(lizt)):
        valid.append('3R')
    if (0 <= start - 1 < len(lizt)):
        valid.append('1L')
    if (0 <= start - 2 < len(lizt)):
        valid.append('2L')
    if (0 <= start - 3 < len(lizt)):
        valid.append('3L')
    return valid

# expand
def expansionCost(validMoves, string2):
    expand = [] # open list 
    cost = 0                                # g(n) valu
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
def heuristicFunction (asdf):
    heuristicList = [] 
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
    heuristicList.append(track)
    track = 0 
    return heuristicList
    
##############################--INITIALIZING--###################################
string = 'BBBWWWE'
stringList = listChange(string)

database = []
temp = [] 
hFunction = heuristicFunction(stringList)
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
'''
todo: favoritism!
'''
w = open("AStar.txt", "w")                      #write at AStar.txt

while True :
    end = False
    fnList = []                                 # to store f(n)
    for i in range(len(OPEN)):
        for j in range(len(database)): 
            if OPEN[i] == database[j][0]:
                tempList = []
                tempList.append(database[j][3]) # f(n) value
                tempList.append(OPEN[i])        # string
                tempList.append(database[j][5]) # move
                fnList.append(tempList)
                
    small = min(fnList)
    small = small[0]
    smallestFn = []
    preferred = []                              # after being picked
    if fnList.count(small) > 1:
        for i in range(len(fnList)):
            if fnList[i][0] == small:
                smallestFn.append(fnList[i])
        for j in range(len(smallestFn)):        # favoritism check
            if smallestFn[j][-1] == '2R' or smallestFn[j][-1] == '3R':
                preferred.append(smallestFn[j])
                if len(prefered) == 1:
                    node = preferred[1]
                else:
                    node = smallestFn[0][1]
                    
    for i in range(len(fnList)):
        if fnList[i][0] == small:
            node = fnList[i][1]
                
    validMoves = initialize(node)
    expand = expansionCost(validMoves,node)
    
    for i in range(len(database)):
        if database[i][0] == node:
            parentsG = database[i][1]           # current g(n)
            break
        
    for i in range(len(expand)):
            childG = expand[i].pop(-1)          # g(n) cost calculated before    
            sTring = expand[i]
            move = validMoves[i]
            gValu = parentsG + childG
            heuristic = heuristicFunction(expand[i])
            if heuristic[0] == 0:
                end = True
            fValu = gValu + heuristic[0]
            tempList = [] 
            tempList.append(sTring)
            tempList.append(gValu)
            tempList.append(heuristic[0])
            tempList.append(fValu)
            tempList.append(node)
            tempList.append(move)
            if sTring not in CLOSE:             # check for ancestor
                database.append(tempList)
                OPEN.append(sTring)
            if end == True:
                sol = sTring                    # set string as solution
                break
    if end == True:
        break
    CLOSE.append(node)
    for i in range(len(OPEN)):
        if OPEN[i] == node:
            del OPEN[i]
            break

finalSolution = []
backtrack = sol
while backtrack != None:                        # backtracking
    for i in range(len(database)):
        if backtrack == database[i][0]:
            tepm = []
            tepm.append(database[i][-1])
            tepm.append(database[i][0])
            tepm.append(database[i][1])
            finalSolution.append(tepm)
            backtrack = database[i][4]
            
for i in range(len(finalSolution)):
    if finalSolution[i][0] == None:
        finalSolution[i][0] = 'start'
        
for j in reversed(finalSolution):
    w.write(str(j) + '\n')
        
w.close()

