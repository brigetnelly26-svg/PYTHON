def capture_marks():
    m1 = float(input("Enter marks for subject 1: "))
    m2 = float(input("Enter marks for subject 2: "))
    m3 = float(input("Enter marks for subject 3: "))
    return m1, m2, m3

def calculate_results(m1, m2, m3):
    total = m1 + m2 + m3
    average = total / 3
    return total, average

def determine_grade(average):
    if average >= 70:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "Fail"

m1, m2, m3 = capture_marks()
total, average = calculate_results(m1, m2, m3)
grade = determine_grade(average)

print("Total Marks:", total)
print("Average Marks:", average)
print("Final Grade:", grade)
