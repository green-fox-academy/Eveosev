class Person(object):
    def __init__(self, name = 'Jane Doe', age = 30, gender = 'female'):
            self.name = name
            self.age = age
            self.gender = gender

    def introduce(self):
        print(f"Hi, I'm {self.name}, a {self.age} year old {self.gender}")
    
    def get_goal(self):
        print("My goal is: Live for the moment!")
    
class Student(Person):
    def __init__(self, name = 'Jane Doe', age = 30, gender = 'female', previous_organization = 'The School of Live'):
        Person.__init__(self, name, age, gender)
        self.previous_organization = previous_organization
        self.skipped_days = 0
   
    def introduce(self):
        print(f"Hi, I'm {self.name}, a {self.age} year old {self.gender} from {self.previous_organization} who skipped {self.skipped_days} days from the course already.")
    
    def get_goal(self):
        print("Be a junior software developer.")
        
    def skip_days(self, number_of_days):
        self.skipped_days += number_of_days
        
class Mentor(Person):
    def __init__(self, name = 'Jnae Doe', age = 30, gender = 'female', level = 'intermediate'):
        Person.__init__(self, name, age, gender)
        self.level = level
        
    def get_goal(self):
        print("Educate brilliant junior software developers.")
        
    def introduce(self):
        print("Hi, I'm {self.name}, a {self.age} year old {self.gender} {self.level} mentor.")
    
class Sponsor(Person):
    def __init__(self, name = 'Jane Doe', age = 30, gender = 'female', company = 'Google', hired_students = 0):
        Person.__init__(self, name, age, gender)
        self.company = company
        self.hired_students = hired_students
        
    def introduce(self):
        print(f"Hi, I'm {self.name}, a {self.age} year old {self.gender} who represents {self.company} and hired {self.hired_students} students so far")
        
    def hire(self):
        self.hired_students += 1
    
    def get_goal(self):
        print(f"Hire brilliant junior software developers.")
        
class Cobort(Student, Mentor):
    def __init__(self, name, students = [], mentors = []):
        self.name = name
        self.students = students
        self.mentors = mentors
        
    def add_student(self, Student):
        self.students.append(Student)
        
    def add_mentor(self, Mentor):
        self.mentors.append(Mentor)
        
    def info(self):
        print(f"The {self.name} cohort has {len(self.students)} students and {len(self.mentors)} mentors.")

people = []

mark = Person('Mark', 46, 'male')
people.append(mark)
jane = Person()
people.append(jane)
john = Student('John Doe', 20, 'male', 'BME')
people.append(john)
student = Student()
people.append(student)
gandhi = Mentor('Gandhi', 148, 'male', 'senior')
people.append(gandhi)
mentor = Mentor()
people.append(mentor)
sponsor = Sponsor()
elon = Sponsor('Elon Musk', 46, 'male', 'SpaceX')
people.append(elon)
student.skip_days(3)

for i in range(5):
    elon.hire()

for i in range(3):
    sponsor.hire()

for person in people:
    person.introduce()
    person.get_goal()

awesome = Cobort('AWESOME')
awesome.add_student(student);
awesome.add_student(john);
awesome.add_mentor(mentor);
awesome.add_mentor(gandhi);
awesome.info();
        
        
        
        
        
        
        
        
        
        
        
        
        
        