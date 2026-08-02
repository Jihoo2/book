from model.student import Student

student_list = []

def print_menu():
    print("----- menu ------")
    print("0. 프로그램 종료")
    print("1. 학생 등록")
    print("2. 학생 목록")
    print("3. 학생 조회")
    print("4. 학생 검색")
    print("5. 학생 삭제")
    print("6. 학과 수정")
    print("7. 학생 수")
def scan_user_input():
    return int(input("메뉴번호: "))

def process(num):
    match num:
        case 0:
            return
        case 1:
            enroll_student()
        case 2:
            show_student()
        case 3:
            select_student()
        case 4:
            search_student()
        case 5:
            delete_student()
        case 6:
            update_student()
        case 7:
            count_student()


# 학생등록
def enroll_student():
    print("----- 학생 등록 -----")
    number = input("학번: ")
    name = input("이름: ")
    major = input("학과: ")
    student = Student(number = number, name = name, major = major)
    student_list.append(student)
    print("학생 등록 완료 !!")
#학생목록
def show_student():
    print("학생 목록 조회")
    for idx, student in enumerate(student_list):
        print(f"{idx}, {student.name}")
#상세조회
def select_student():
    print("-----상세 조회-----")
    num=int(input("조회 할 번호: "))
    student = student_list[num]
    print(student)
#학생 검색
def search_student():
    name = input("검색할 이름: ")
    for student in student_list:
        if student.name == name:
            print(student)
            return
    print("학생을 찾을 수 없습니다")


#학생삭제
def delete_student():
    print("-----학생 목록------")
    num=int(input("삭제 할 번호: "))
    del student_list[num]
    print("삭제 완료!")


#학생수정
def update_student():
    num = int(input("수정 할 번호 : "))
    student = student_list[num]
    student.major =input("새로운 학과: ")
    print("수정완료")

#등록된 학생
def count_student():
    print(f"현재 학생 수: {len(student_list)}명")