# tests/test_calculations.py

from gradescalculator.main import calculate_grades

def test_calculate_grades():
    grades = {
        "grade 1": {"weight": 10, "grade": 3.6},
        "grade 2": {"weight": 15, "grade": 4.6},
        "grade 3": {"weight": 25, "grade": 5.3},
        "grade 4": {"weight": 5, "grade": 4.0},
        "grade 5": {"weight": 45, "grade": 4.9}
    }
    
    precise_grade, rounded_grade = calculate_grades(grades)
    
    assert precise_grade == 4.7  # Remplacer par la valeur attendue correcte
    assert rounded_grade == 4.5  # Remplacer par la valeur attendue correcte
