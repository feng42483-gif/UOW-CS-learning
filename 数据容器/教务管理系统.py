student_message = {}
menu = """
########教务处系统#########
#       1.添加学生信息     #
#       2.修改学生信息     #
#       3.删除学生信息     #
#       4.查询学生信息     #
#       5.列出学生信息     #
#       6.统计学生信息     #
#       7.退出系统        #
########################
"""
print(menu)
while True:
    choice = input("请选择要执行的操作（1-7）：")
    match choice:
        case "1":
            student_name = input("请输入学生姓名:")
            chinese_score =int(input("请输入学生语文成绩:"))
            math_score = int(input("请输入学生数学成绩:"))
            english_score = int(input("请输入学生英语成绩:"))
            if student_name in student_message:
                print("该学生信息已存在,请重新选择")
            else:
                student_message[student_name] = {"语文":chinese_score,"数学":math_score,"英语":english_score}
                print("添加成功")
        case "2":
            student_name = input("请输入修改的学生姓名")
            chinese_score = input("请输入修改的语文成绩：")
            math_score = float(input("请输入最新的数学成绩："))
            english_score = int(input("请输入最新的英语成绩："))
            if student_name not in student_message:
                print("该商品不存在，请重新选择")
            else:
                student_message[student_name] = {"语文":chinese_score,"数学":math_score,"英语":english_score}
                print("商品修改完毕")
        case "3":
            student_name = input("请输入要删除的商品名称：")
            if student_name not in student_message:
                print("该商品不存在，请重新选择")
            else:
                del student_message[student_name]
                print("商品删除完毕")
        case "4":
            for student_name in student_message.keys():
                dict_values = student_message[student_name]
                print(
                    f"学生姓名{student_name}, "
                    f"语文成绩{dict_values['语文']}, "
                    f"数学成绩{dict_values['数学']}, "
                    f"英语成绩{dict_values['英语']}"
                )
        case "5":
            for name, info in student_message.items():
                print(name, info)
        case "6":
            if len(student_message) == 0:
                print("当前没有学生信息")
            else:
                chinese_scores = []
                math_scores = []
                english_scores = []

                for student_name, scores in student_message.items():
                    chinese_scores.append(scores["语文"])
                    math_scores.append(scores["数学"])
                    english_scores.append(scores["英语"])

                # 计算最高最低平均分
                print("语文最高分:", max(chinese_scores))
                print("语文最低分:", min(chinese_scores))
                print("语文平均分:", sum(chinese_scores) / len(chinese_scores))

                print("数学最高分:", max(math_scores))
                print("数学最低分:", min(math_scores))
                print("数学平均分:", sum(math_scores) / len(math_scores))

                print("英语最高分:", max(english_scores))
                print("英语最低分:", min(english_scores))
                print("英语平均分:", sum(english_scores) / len(english_scores))

                # 找最高分和最低分学生
                chinese_max_student = ""
                chinese_min_student = ""

                math_max_student = ""
                math_min_student = ""

                english_max_student = ""
                english_min_student = ""

                chinese_max = max(chinese_scores)
                chinese_min = min(chinese_scores)

                math_max = max(math_scores)
                math_min = min(math_scores)

                english_max = max(english_scores)
                english_min = min(english_scores)

                for student_name, scores in student_message.items():

                    if scores["语文"] == chinese_max:
                        chinese_max_student = student_name

                    if scores["语文"] == chinese_min:
                        chinese_min_student = student_name

                    if scores["数学"] == math_max:
                        math_max_student = student_name

                    if scores["数学"] == math_min:
                        math_min_student = student_name

                    if scores["英语"] == english_max:
                        english_max_student = student_name

                    if scores["英语"] == english_min:
                        english_min_student = student_name

                print("语文最高分学生:", chinese_max_student)
                print("语文最低分学生:", chinese_min_student)

                print("数学最高分学生:", math_max_student)
                print("数学最低分学生:", math_min_student)

                print("英语最高分学生:", english_max_student)
                print("英语最低分学生:", english_min_student)
        case "7":
            print("已退出")
            break
        case _:
            print("操作不支持")
