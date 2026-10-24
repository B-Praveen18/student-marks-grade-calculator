
# Student Marks and Grade Calculator

A simple Python package for calculating student marks,
average, percentage, and grades.

## Features

- Calculate total marks
- Calculate average marks
- Calculate percentage
- Determine student grade

## Installation

Run the following command:

    py -m pip install .

## Usage

```python
from studentutils import (
    total_marks,
    average_marks,
    percentage,
    calculate_grade
)

marks = [85, 90, 78, 92, 88]

print("Total:", total_marks(marks))
print("Average:", average_marks(marks))

percent = percentage(marks)
print("Percentage:", percent)
print("Grade:", calculate_grade(percent))
```

## Author

B.Praveen

## Version

1.0.0
