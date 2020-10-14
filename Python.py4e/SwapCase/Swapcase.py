# Swapcase is a built in function of python.
# Before I came to know this fact, I tried out the following logic but niether of them worked.
# 1. Converting a string to a list with all the letters as it's indexes and then running a loop to convert notice if the letter was lowercase or uppercase and then converting them to the opposite. (For example, converting the word, "Python" to a list; ["P", "y", "t", "h", "o", "n" ] and then running the following code:
# def swap_case(s):
#    s.split()
#    x=0
#    for i in range(len(s)):
#        if s[x] == s[x].lower:
#            s[x].capitalize()
#        elif s[x] == s[x].upper:
#            s[x].lower()
#        x += 1
#    return(s)

# # The correct method is below and it is very simple:
 
def swap_case(s):
    return(s.swapcase())

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
