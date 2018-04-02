def sub(x,y,i,j):#defines whether there should be a no-op used or not
    if(x[i-1] == y[j-1]):# if this conditional is not met we use a No-Op not a sub.
        return 0
    else:
        return 10

def swap(x,y,i,j):#decides if the swap is viable
    if(x[i-2] == y[j-1] and x[i-1] == y[j-2]):#conditional for a swap to be turned to 2 No-Ops
        return 0
    else:
        return 20

def alignStrings(x,y):

    S = [[0 for i in range(len(y)+1)] for j in range(len(x)+1)]

    for i in range(len(x)+1):#plus one here and in the loop below to make room for the "_" blank character.
        for j in range(len(y)+1):
            if(i==0 and j==0):#Set the base case for the dynamic programming
                S[i][j] = 0
            elif(i==0):
                S[i][j] = (S[i][j-1])+1
            elif(j==0):
                S[i][j] = S[i-1][j]+1#This and the case just above is to be sure that the algorithm doe not try to reach parts of the table that do not exist. AKA the first row and column
            elif(i >= 2 and j >= 2):
                S[i][j] = min(S[i-1][j]+1,S[i][j-1]+1,S[i-1][j-1]+sub(x,y,i,j),S[i-2][j-2]+10+swap(x,y,i,j))#this case is for deeper in the table when i-2 and j-2 exist.
            else:
                S[i][j] = min(S[i-1][j]+1,S[i][j-1]+1,S[i-1][j-1]+sub(x,y,i,j))# inbetween cases where i-1 and j-1 exist but i-2 and j-2 do not.
    return S
