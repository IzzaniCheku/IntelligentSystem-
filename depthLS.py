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

 
##############################--INITIALIZING--###################################

string = 'BEWWB'
stringList = listChange(string)

database = []
temp = [] 
##print(fFunction)
temp.append(stringList)
print(temp)
temp.append(None) # where they came from 
temp.append(None) # how many moves taken 
database.append(temp)
print(database)
##temp = []
##print(database)


##print(openList)

##############################--LOOPPOINT--###################################
'''
todo: favoritism!
'''
w = open("outputLimitSearch.txt", "w") #write at outputbwt.txt

OPEN = []
CLOSE = []

OPEN.append(stringList)
print(OPEN[0])

end = False
while end == False :
    
    potter = OPEN.pop(-1)
    validMoves = initialize(potter)
    expand = expansionCost(validMoves, potter)
    for i in range(len(expand)):
            if expand[i] not in CLOSE and expand[i] not in OPEN: # check ancestor
                print(expand[i])
                OPEN.append(expand[i])
    CLOSE.append(potter)
    
    end = True
    if end == True:
        sol = sTring
        break 

w.close()

