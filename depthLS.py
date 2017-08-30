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
    if (0 <= start + 2  < len(lizt)):
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
    for i in range(len(validMoves)):
        for j in range(len(string2)):
            if string2[j] == 'E':
                if validMoves[i] == '1R':
                    string2[j],string2[j+1] = string2[j+1],string2[j]
                    string3 = string2[:]
                    expand.append(string3)
                    string2[j],string2[j+1] = string2[j+1],string2[j]

                if validMoves[i] == '2R':
                    string2[j],string2[j+2] = string2[j+2],string2[j]
                    string3 = string2[:]
                    expand.append(string3)
                    string2[j],string2[j+2] = string2[j+2],string2[j]

                if validMoves[i] == '3R':
                    string2[j],string2[j+3] = string2[j+3],string2[j]
                    string3 = string2[:]
                    expand.append(string3)
                    string2[j],string2[j+3] = string2[j+3],string2[j]

                if validMoves[i] == '1L':
                    string2[j],string2[j-1] = string2[j-1],string2[j]
                    string3 = string2[:]
                    expand.append(string3)
                    string2[j],string2[j-1] = string2[j-1],string2[j]

                if validMoves[i] == '2L':
                    string2[j],string2[j-2] = string2[j-2],string2[j]
                    string3 = string2[:]
                    expand.append(string3)
                    string2[j],string2[j-2] = string2[j-2],string2[j]

                if validMoves[i] == '3L':
                    string2[j],string2[j-3] = string2[j-3],string2[j]
                    string3 = string2[:]
                    expand.append(string3)
                    string2[j],string2[j-3] = string2[j-3],string2[j]

    return expand

def loopchecker (asdf):
    tocount = []
    for i in range(len(asdf)):
        if asdf[i] != 'E':
            tocount.append(asdf[i])
    countW = tocount.count('W')

    return countW

def last(endcheck, fdsa):
    checkagain = []
    for i in range(len(fdsa)):
        if fdsa[i] != 'E':
            checkagain.append(fdsa[i])
            
    for i in range(0,endcheck):
        if checkagain[i] != 'W':
            return False
    return True

##############################--INITIALIZING--###################################
string = 'BBBWWWE'
limit = 9
stringList = listChange(string)
database = []
temp = [] 
temp.append(stringList)
print(temp)

temp.append(None) # where they came from 
temp.append(None) # how many moves taken
temp.append(0)    # depth 
database.append(temp)
print(database)
##############################--LOOPPOINT--###################################
#w = open("outputLimitSearch.txt", "w") #write at outputlimitSearch.txt

OPEN = []
CLOSE = []

OPEN.append(stringList)
print(OPEN[0])



end = False
endcheck = loopchecker(stringList) # count the w's
while len(OPEN) > 0 :
    potter = OPEN.pop(-1)
    last2 = last(endcheck,potter) # check for the W's
    if last2 == True:   #checks for end node
        break
    for i in range(len(database)):
        if database[i][0] == potter:
            depth = database[i][3]
    CLOSE.append(potter)
    if depth == limit - 1:  #make sure do not search past depth limit
        continue
    validMoves = initialize(potter)
    expand = expansionCost(validMoves, potter)
    for i in range(len(expand)):
            if expand[i] not in CLOSE and expand[i] not in OPEN: # check ancestor
                temp = []
                OPEN.append(expand[i])
                temp.append(expand[i])
                temp.append(potter)
                temp.append(validMoves[i])
                temp.append(depth + 1)
                database.append(temp)
                #print(database)
    
if len(OPEN) == 0:
    print('no answer found at this limit')
else:
    print(potter)
    # todo: potter is the answer, use potter backtrack the path
    next
#w.close()

################################################################################
