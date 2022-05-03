def create_list(list1):
    try:

        while True:
            student_id = int(input("Enter Student ID : "))
            if student_id == 0:
                break
            else:
                quiz1 = float(input("Enter Quiz 1 Score(out of 100) : "))
                quiz2 = float(input("Enter Quiz 2 Score(out of 100) : "))
                final_exam = float(input("Enter Final Exam Score(out of 100) : "))

                student_details = []
                total_mark = float((0.2*quiz1) +(0.3*quiz2) + (0.5*final_exam))

                student_details.append(student_id)
                student_details.append(quiz1)
                student_details.append(quiz2)
                student_details.append(final_exam)
                student_details.append(total_mark)

                list1.append(student_details)

        print(list1)

    except ValueError:
        print("Non-integer value!")



def main():
    list1 = []
    create_list(list1)
main()

