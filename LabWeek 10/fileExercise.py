# fileExercise.py
# Anish Reddy Nukala
# Date: 03-20-2024
# Lab Week 10 

def calculate_grades(students, scores):
    header = ["Student ID", "Name", "Total Scores", "Sum of All Scores", "Score Average"]
    master_grades = [header]

    for student_id, name in students[1:]:
        total_scores, sum_of_scores, count_of_scores = 0, 0, 0

        for score_id, assignment, score in scores[1:]:
            if score_id == student_id:
                total_scores += 1
                sum_of_scores += int(score)
                count_of_scores += 1

        average = sum_of_scores / count_of_scores if count_of_scores > 0 else 0
        master_grades.append([student_id, name, total_scores, sum_of_scores, round(average, 1)])

    return master_grades

def write_to_file(data, filename):
    with open(filename, 'w') as file:
        for row in data:
            file.write(','.join(map(str, row)) + '\n')

def main():
    students_data = [line.strip().split(', ') for line in open('students.txt')]
    scores_data = [line.strip().split(', ') for line in open('scores.txt')]

    master_grades = calculate_grades(students_data, scores_data)
    write_to_file(master_grades, 'grades.txt')

if __name__ == "__main__":
    main()
