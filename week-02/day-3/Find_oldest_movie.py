"""
Read this input file and print the title of the oldest movie. The file has the following columns:

   Title
   Year
   Director
"""
try:
    fr_movies = open("movies.csv", 'r')
    movies = fr_movies.readlines()
    movies_sep = {}
    for i in range(len(movies)):
        temp = []
        temp = movies[i].split(';')
        movies_sep[temp[0]] = temp[1]
    sorted_movies = sorted(movies_sep.items(), key = lambda x: int(x[1]))
    print(f"The oldest movie is '{sorted_movies[0][0]}', which is pulished in {sorted_movies[0][1]}")
    fr_movies.close()
except:        
    print("Error")