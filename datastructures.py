def search_student_grade(name) :
    from studentGrades_dict import STUDENT_DICT_DATA
    from studenGrades_list import STUDENT_LIST_DATA

    all_assignment_grades = {**assignment_grades1, **assignment_grades2}

    if name in all_assignment_grades:
        grades = all_assignment_grades[name]
    
    average_grade = sum(grades) / len (grades)
    max_score = max(grades)
    max_score_assignment = [assignment for assignment, score in all_assignment_grades[name].items() if score == max_score][0]

    return average_grade, max_score_assignment

else:
return None

student_name = ""
average_grade, highest_score_assignment = search_student_grade(student_name)

if average_grade is not None:
    print(f"Average grade for {student_name}: {average_grade}")
    print(f"Highest score assignment for {student_name}: {highest_score_assignment}")
else:
    print(f"No data found for {student_name}")