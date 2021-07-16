# function inside class

class Student:
    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa
    
    def on_honor_roll(self): # function inside class Student)
        if self.gpa >= 3.5:
            return True
        else: 
            return False 