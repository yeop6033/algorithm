grade_change={"A+":4.5,"A0":4.0,"B+":3.5,"B0":3.0,"C+":2.5,"C0":2.0,"D+":1.5,"D0":1.0,"F":0}
total_grade_num=0
total=0
for i in range(20):
    a=list(map(str,input().strip().split()))
    # print(a[1])
    stu_gra=float(a[1])
    grade = a[2]
    
    if grade == "P":
        continue

    sub_grade= grade_change.get(grade, 0)
    total+=sub_grade*stu_gra
    total_grade_num +=stu_gra
# print(total)

gpa=total/total_grade_num
print(f"{gpa:.6f}") 