from student_manager import print_menu,scan_user_input, process


print("===== 학생 관리 프로그램 =====")
while True:
    try:
        print_menu()
        num = scan_user_input()
        if num == 0:
            break
        process(num)

    except Exception as e:
        print(e)