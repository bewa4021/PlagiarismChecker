from alignStrings import alignStrings,swap,sub
import random

def extractAlignment(S,x,y):
    a = []#instruction array
    k = -1
    global i
    i = len(x)
    global j
    j = len(y)# i and j start at the end of the table so we can search find a path from the optimal solution.
    while(i>0 or j>0):
        a.append(determineOptimalOp(S,x,y))
        k = k+1
        updateIndecies(S,a[k])
    return list(reversed(a))

def determineOptimalOp(S,x,y):
    solution = []#temporary array used to choose between ties at random.
    global i
    global j
    if(S[i][j] == 1+(S[i][j-1])):#checks for Indel to the right
        solution.append("InDel-Right")
    if(S[i][j] == 1+(S[i-1][j])):#checks for Indel down
        solution.append("InDel-Down")
    if(S[i][j] == S[i-1][j-1] and x[i-1] == y[j-1]):#to check for a No-Op we need to also be sure the two strings have the same character there.
        solution.append("No-Op")
    if(S[i][j] == 10+(S[i-1][j-1])):#checks for a substitution
        solution.append("Sub")
    if((S[i][j] == 10+S[i-2][j-2] and x[i] == y[j-1] and x[i-1] == y[j])
     or (S[i][j] == 20+S[i-2][j-2] and (x[i] == y[j-1] or x[i-1] == y[j]))
     or S[i][j] == 30+S[i-2][j-2]):# This whole conditional is to make sure that the correct cost was allocated and that the correct letters were swapped in the two given strings.
        solution.append("Swap")
    return solution[random.randint(0,len(solution)-1)]

def updateIndecies(S,a):# here we just look at the new addition to solution array 'a' and change the indices to the correct position in the table based on what instruction 'a' holds.
    global i
    global j
    if(a == "InDel-Right"):
        j = j-1
    elif(a == "InDel-Down"):
        i = i-1
    elif(a == "No-Op" or a == "Sub"):
        i = i-1
        j = j-1
    else:
        i = i-2
        j = j-2
