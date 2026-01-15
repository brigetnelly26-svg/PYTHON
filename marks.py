def evaluate_grade(marks):
    if marks>=70:
        grade="A"
        remark="excellent"
    elif marks>=60:
        grade+"B"
        remarks="very good"
    elif marks>=50:
        grade="C"
        remarks="good"
    elif marks>=40:
        grade="D"
        remarks="pass"
    else:
        grade="f"
        remark="fail"
        return grade,remark
    #input
    marks=int(input("enter marks(0-100):"))
    #function call
    grade,remarks=evaluate_grade(marks)
    #output 
    print("grade:",grade)
    print("remarks:",remarks)