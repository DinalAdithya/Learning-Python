from StudentClass import Student
class Inheritance(Student):

    def selected(self):
        if self.gpa >= 3.0:
            print("selected to the company")
        else:
            print("did not get selected")
