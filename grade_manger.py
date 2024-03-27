name_list =  []
id_list =  []
english_list = []
math_list = []
language_list = []

for i in range(5): 
    name_list.append(input("이름 : "))
    id_list.append(int(input("학번 : ")))
    math_list.append(int(input("수학 : ")))
    language_list.append(int(input("국어 : ")))
    english_list.append(int(input("영어 : ")))

def grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def add(get_num):
    return math_list[get_num] + language_list[get_num] + english_list[get_num]

avg = [(add(i) / 3) for i in range(5)]  # 각 학생의 평균을 계산하여 리스트에 저장
rank = [0] * 5  # 등수를 저장할 리스트 초기화

sorted_avg = sorted(avg, reverse=True)  # 평균을 내림차순으로 정렬

for i, n in enumerate(avg):  # 등수 부여
    rank[i] = sorted_avg.index(n) + 1

for i in range(5): 
    print("이름", name_list[i], " 학번", id_list[i])
    print("총점 : ", add(i), "평균 : ", "%.2f" % (add(i) / 3), "학점 : ", grade(add(i) / 3), rank[i], "등")
