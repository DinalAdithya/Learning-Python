class Student:
    def __init__(self, name, age, grade, gender, healthy_or_not, gpa):
        self.name = name
        self.age = age
        self.grade = grade
        self.gender = gender
        self.healthy_or_not = healthy_or_not
        self.gpa = gpa

    ###Object Function
    def on_honor_role(self):
        if self.grade >= 70:
            return True
        else:
            return False
