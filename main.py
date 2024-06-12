# Define the grades and their weights including the exam grade
grades_with_exam = {
    "grade 1": {"weight": 10, "grade": 3.6},
    "grade 2": {"weight": 15, "grade": 4.6},
    "grade 3": {"weight": 25, "grade": 5.3},
    "grade 4": {"weight": 5, "grade": 4.0},
    "grade 5": {"weight": 45, "grade": 6.0}
}

# Calculate the total weighted sum of the grades
total_weighted_sum_with_exam = sum(item["weight"] * item["grade"] for item in grades_with_exam.values())

# Calculate the total weight
total_weight_with_exam = sum(item["weight"] for item in grades_with_exam.values())

# Calculate the overall grade
overall_grade_with_exam = total_weighted_sum_with_exam / total_weight_with_exam

# Round the overall grade to the nearest 0.1 and the nearest 0.5
precise_overall_grade = round(overall_grade_with_exam * 10) / 10
rounded_overall_grade = round(overall_grade_with_exam * 2) / 2

# Print the results
print(f"Precise Overall Grade (rounded to the nearest 0.1): {precise_overall_grade}")
print(f"Rounded Overall Grade (rounded to the nearest 0.5): {rounded_overall_grade}")