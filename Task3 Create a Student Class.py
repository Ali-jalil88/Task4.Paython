class Student :
    def __init__(self,name,cours):
        self.names=[]
        self.courses=[]
        print (f"{name} :\t {cours}")
    def enroll (self,name_of_cours):
        self.courses.append(name_of_cours)
    def get_courses(self):
        return self.courses
student=Student("Ali","Math")
student=Student("Zara","physics")
student=Student("Ahmad","chemistry")
print("**********")
student.enroll("Math")
student.enroll("sports")
student.enroll("physics")
student.enroll("Sciences")
student.enroll("chemistry")
print(student.get_courses())

