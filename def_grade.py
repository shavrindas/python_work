student = []
repeat = 5


#입력 함수 
def user_input():
    global student
    for i in range(repeat):
        student.append([])
        student[i].append(int(input("학번 : ")))
        student[i].append(input("이름 : "))
        student[i].append(int(input("영어 : ")))
        student[i].append(int(input("C-언어: ")))
        student[i].append(int(input("파이썬: ")))


#총점/평균 계산 함수
def addavg():
    global student
    for i in range(repeat):
        student[i].append(student[i][2] + student[i][3] + student[i][4])
        student[i].append(student[i][5] / 3)

#학점계산 함수
def grade():
    global student 
    for i in range(repeat):
        score = student[i][6]
        if score >= 90:
            student[i].append("A")
        elif score >= 80:
            student[i].append("B")
        elif score >= 70:
            student[i].append("C")
        elif score >= 60:
            student[i].append("D")
        else:
            student[i].append("F")
    
#등수계산 함수
        
def rank():
    global student
    student = sorted(student, key=lambda x: x[6], reverse=True)
    for i in range(repeat):
        student[i].append(i+1)
    

#출력 함수
def output():
    global student
    
    print("학생 성적 결과")
    print("======================================================================================")
    print("학번\t이름\t영어\tC-언어\t파이썬\t총점\t평균\t학점\t등수")
    print("======================================================================================")
    for i in range(repeat):
        print(student[i][0],"\t", student[i][1],"\t",student[i][2],"\t",student[i][3],"\t",student[i][4],"\t", student[i][5],"\t", f'{student[i][6]:.2f}',"  ", student[i][7],"\t", student[i][8])

def mian():
    user_input()
    addavg()
    grade()
    rank()
    output()

mian()