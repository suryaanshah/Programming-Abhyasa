# Enter your code here. Read input from STDIN. Print output to STDOUT
for i in range(int(input())): 
    s=input(); #Takes the input from the user
    print(*["".join(s[::2]),"".join(s[1::2])]) #Prints(displays) the even indexes
