from alignStrings import alignStrings,swap,sub
from extractAlignment import extractAlignment,determineOptimalOp,updateIndecies

f = open("File1.txt","r")
data = f.readline()
#udata=data.decode("utf-8")
stringX=data.encode("ascii","ignore")


f = open("File2.txt","r")
data = f.readline()
#udata=data.decode("utf-8")
stringY=data.encode("ascii","ignore")



def commonSubstrings(x,L,a):
    i = 0#counter for array 'a'
    xCounter = 0#counter for the string 'x'
    sol = []#a list that will hold the common substrings of length at least L.
    while (i < len(a)):
        if (a[i] == "No-Op"):#conditional to start searching for a sequence of No-Ops longer than L
            start = xCounter
            end = xCounter#start and end are placed where we are in the 'x' string
            while(a[i] == "No-Op" and (i+1) <= len(a)):
                i = i+1
                end = end+1#for ever No-Op we see we incriment end to move to incude all character in the common substring.
                if(i == len(a)):#if i is ever larger than what can be accessed in a then we should terminate searching for No-Ops. since we have reached the end.
                    break
            if(end-start >= L):
                sol.append(x[start:end])#append the common substring if the length is longer than L
            xCounter = end
        if(i == len(a)):#if i ever goes more higher than what a can access we are done and should end the main loop immediately.
            break
        if (a[i] == "InDel-Right"):# if a[i] is InDel-right then the 'a' array should move forward, but the counter for 'x' should not.
            xCounter = xCounter - 1#we decriment xCounter by one before it adds one so that there is no change.
        xCounter = xCounter+1
        i = i+1#counters incriment
    print(sol)


commonSubstrings(stringX,10,extractAlignment(alignStrings(stringX,stringY),stringX,stringY))
