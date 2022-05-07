class Exam:


    def __init__(self, examname, total_points):
        self.__examname = examname
        self.__studname = None
        self.__totalposspoint = total_points
        self.__pointsearned = 0

    def examname(self):
        return self.__examname
    
    def totalposspoint(self):
        return self.__totalposspoint

    def take_exam(self, name1):
        self.__studname = name1


    def grade_exam(self, grade1):
        self.__pointsearned = grade1

    def __str__(self):
        return f'Exam({self.take_exam},{self.grade_exam})'

    def print_info(self, obj1name):
        print("Object rn is: ", obj1name)
        print("The student name is: ", self.__studname)
        print("Points Earned is: ", self.__pointsearned)

def main():
    obj1 = Exam("GCIS", 100)
    obj1.take_exam("Sahana")
    obj1.grade_exam(90)
    print(obj1)
    obj1.print_info("Student 1")

    
main()


