class Student:
    courseMarks={}
    name=""
    family=""

    def __init__(self, name, family):
        self.name = name
        self.family = family

    def addCourseMark(self, course, mark):
        self.courseMarks[course] = mark

    def average(self):
        marks = self.courseMarks.values()
        average = sum(marks) / len(marks)
        return average

e = Student("jimmy", "neutron")
print e.name
print e.family
e.addCourseMark("EE 240", 30)
e.addCourseMark("CMPUT 420", 2) 
print e.average()
