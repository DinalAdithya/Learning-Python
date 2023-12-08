from StudentClass import Student
from Inheritance import Inheritance as Ir

stud1 = Student("Jayathilka", 23, 69, "Male", True, 2.1)
stud2 = Student("Anna", 25, 70, "Female", True, 3.1)

"""print(stud1.name)
print(stud1.age)
print(stud1.gender)
print(stud1.grade)


print(stud2.name)
print(stud2.age)
print(stud2.gender)
print(stud2.grade)"""

###print the Object Function
print(stud2.on_honor_role())

Ir.selected(stud2)

