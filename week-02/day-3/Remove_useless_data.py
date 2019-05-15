"""
In this file you can find the raw data of a public election. 
Unfortunately something went wrong and there are some row which cannot be used (a value is missing). 
We need to remove these rows and then print them to the console. 
Columns (mandatory fields are signed with *):

    Name *
    Candidate *
    Time
    State *
"""
def printmissing(x):
    print('The rows with missing value are:')
    for i in x:
        print(f"{i}")
        
def printrow(x):
    print("The rows without missing value are:")
    for i in x:
        print(f"{i}")


f_election = open("election.csv", 'r')
content = f_election.read().splitlines()
content_sep = []
for i in content:
    content_sep.append(i.split(','))
rwithmissingv = []
for i in content_sep:
    if "" in i:
        rwithmissingv.append(i)
        content_sep.remove(i)
printmissing(rwithmissingv)

printrow(content_sep)
    
