if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
ans=sum(student_marks[query_name])/len(student_marks[query_name]) #Defining a variable, ans.
print("%.2f" % ans)#Printing ans with 2 decimal places
