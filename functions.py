def calculate_total(marks):
    """Calculate the total marks."""
    return sum(marks)


def calculate_average(marks):
    """Calculate the average marks."""
    return sum(marks) / len(marks)


def assign_grade(average):
    """Assign a grade based on average marks."""
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


def check_result(marks):
    """Check whether a student has passed all subjects."""
    for mark in marks:
        if mark < 40:
            return "Fail"
    return "Pass"