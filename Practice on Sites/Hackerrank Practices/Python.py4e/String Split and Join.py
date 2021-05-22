def split_and_join(line):
    line=line.split(" ") # Splitting the string to a list where each word is a list-item(for example- "Hello World" to ['Hello', 'World'])
    line="-".join(line) # Joining the list items to a string in which each word is seperated by a "-" rather than a space.(for example- ['Hello', 'World'] to "Hello-World")
    return(line) # Returning the output. We won't print it because if we do so, we will get two outputs those are: 1. (None) and 2. (the neccesary output)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line) # The code for checking the results.
    print(result)
