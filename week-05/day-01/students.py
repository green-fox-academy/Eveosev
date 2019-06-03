# Students
from collections import namedtuple
from pprint import pprint

# Given a list of students with the following fields: name, age, gender and grades.
students = namedtuple('students', ['name', 'age', 'gender', 'grades'])
Students = [students(name = 'John', age = 16, gender = 'male', grades = '5,5,4,2'),
            students(name = 'Bob', age = 17, gender = 'male', grades = '2,2,3,1'),
            students(name = 'Jane', age = 15, gender = 'female', grades = '4,3,4,4,5')]

# Create a new list that only includes the boys
boys_only = tuple(filter(lambda x: x.gender == 'male', Students))

pprint(boys_only)

# Create a new list that only includes who's name starts with the letter J
J_start = tuple(filter(lambda x: x.name.startswith('J'), Students))

pprint(J_start)


# Create a new list that only includes the girls
girls_only = tuple(filter(lambda x: x.gender == 'female', Students))

pprint(girls_only)


# Create a new list that only includes who's grade average is above 4
avg_above_4 = tuple(filter(lambda x: sum(map(int, x.grades.split(','))) / len(x.grades.split(',')) > 4, Students))

pprint(girls_only)


# Create a new list that only includes the boys who's name starts with the letter J
J_start_boys = tuple(filter(lambda x: x.name.startswith('J') and x.gender == 'male', Students))

pprint(J_start_boys)
# Create a new list that only includes the girls who's grade average is above 4
avg_above_4_girls = tuple(filter(lambda x: sum(map(int, x.grades.split(','))) / len(x.grades.split(',')) > 4 and x.gender == 'female', Students))

pprint(avg_above_4_girls)


# Create a new list that only includes who's at least two 5s
at_least_two_5s = tuple(filter(lambda x: x.grades.split(',').count('5') >= 2, Students))

pprint(at_least_two_5s)


# Create a new list that only includes who's grade average is above 4 and at at least got two 5s
at_least_two_5s_and_avg_above_4 = tuple(filter(lambda x: x.grades.split(',').count('5') >= 2 and sum(map(int, x.grades.split(','))) / len(x.grades.split(',')) > 4, Students))

pprint(at_least_two_5s_and_avg_above_4)