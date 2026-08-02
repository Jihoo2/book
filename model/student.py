class Student:
    def __init__(self, number, name ,major):
        self.number = number
        self.name = name
        self.major = major
    def __str__(self):
        return f"학번: {self.number}\n이름: {self.name}\n학과:{self.major}"

