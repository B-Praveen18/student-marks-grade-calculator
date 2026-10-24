
"""
Student Marks and Grade Calculator Package.
Core operations for student mark calculations.
"""

def total_marks(marks):
    return sum(marks)


def average_marks(marks):
    if len(marks) == 0:
        raise ValueError("Marks list cannot be empty.")
    return sum(marks) / len(marks)


def percentage(marks, max_mark=100):
    if len(marks) == 0:
        raise ValueError("Marks list cannot be empty.")
    if max_mark <= 0:
        raise ValueError("Maximum mark must be positive.")
    return (sum(marks) / (len(marks) * max_mark)) * 100


def calculate_grade(percent):
    if percent >= 90:
        return "O"
    elif percent >= 80:
        return "A+"
    elif percent >= 70:
        return "A"
    elif percent >= 60:
        return "B+"
    elif percent >= 50:
        return "B"
    else:
        return "U"

def calculate_gpa(grade_points):
    """
    Calculate GPA from a list of grade points.
    Assumes all subjects have equal credit weight.
    """
    if len(grade_points) == 0:
        raise ValueError("Grade points list cannot be empty.")

    if any(point < 0 or point > 10 for point in grade_points):
        raise ValueError("Grade points must be between 0 and 10.")

    return round(sum(grade_points) / len(grade_points), 2)
