# Classes basically like blueprints for creating objects. An object has properties and methods(functions) associated with it.

class student:
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name   
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

