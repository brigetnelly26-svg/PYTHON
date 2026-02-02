def get_marks():
    marks=[]
    for i in range(3):
        marks=float(input(f"enter marks{i+1}"))
    return marks
def calculate_average(m1,m2,m3):
    return(m1,m2,m3)/3
def get_grade(average):
    if average>=70:
        return"A"
    elif average>=60:
        return"B"
    elif average>=50:
        return"C"
    elif average>=40:
        return "D"
    else:
        return"FAIL"
    print("everage"+everage)
    print("grade"+grade)

