# Getting the inputs from the user
A3pts=int(input("Enter the no. of A3 pointers"))
A2pts=int(input("Enter the no. of A2 pointers"))
A1pts=int(input("Enter the no. of A1 pointers"))
B3pts=int(input("Enter the no. of B3 pointers"))
B2pts=int(input("Enter the no. of B2 pointers"))
B1pts=int(input("Enter the no. of B1 pointers"))

# Calculating scores
Ascore=(A3pts*3)+(A2pts*2)+(A1pts)
Bscore=(B3pts*3)+(B2pts*2)+(B1pts)

# Giving the output
def MatchDecider():
    if Ascore>Bscore:
        Result = "A"
    elif Bscore>Ascore:
        Result = "B"
    else:
        Result = "T"
    return(Result)
MatchDecider()
