
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
