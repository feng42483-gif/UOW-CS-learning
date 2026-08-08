# 学生类

class Student:
    def __init__(self, name, chinese,math,english):
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english

    def __str__(self):
        return f"姓名：{self.name},语文：{self.chinese},数学：{self.math},英语：{self.english},总分：{self.chinese +self.math+ self.english}"


    def update_score(self,chinese=None,math=None,english=None):
        if chinese is not None:
            self.chinese = chinese
        if math is not None:
            self.math = math
        if english is not None:
            self.english = english

# 教务管理系统类
class EduManagement:
    system_version = "1.0"
    system_name = "教务管理系统"


    def __init__(self):
        self.student_list = []

    def add_student(self,):
        name =  input("请输入学生姓名：")
        for s in self.student_list:
            if s.name == name:
                print("该学生已存在")
                return

        chinese  = int(input("请输入语文成绩："))
        math = int(input("请输入数学成绩："))
        english =    int(input("请输入英语成绩："))

        if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
            stu = Student(name, chinese , math , english)
            self.student_list.append(stu)
            print("学生信息已添加")
        else:
            print("各科成绩必须在0 - 100之间")


    def update_student(self):
        name = input("请输入要修改的学生姓名")
        for s in self.student_list:
            if s.name == name:
                print(f"当前成绩{s},")

                chinese = int(input("请输入语文成绩："))
                math = int(input("请输入数学成绩："))
                english = int(input("请输入英语成绩："))

                if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
                    s.update_score(chinese,math,english)
                    print("成绩修改成功")
                    print(f"修改后的成绩为：{s}")
                    return
                else:
                    print("各科成绩必须在0 - 100之间")
                    return
        print("未找到该学生，修改失败")


    def delete_student(self):
        name = input("请输入要删除的学生姓名")
        for s in self.student_list:
            if s.name == name:
                self.student_list.remove(s)
                print("删除成功")
                return
        print("未找到，删除失败")


    def find_student(self):
        name = input("请输入要查询的学生姓名")
        for s in self.student_list:
            if s.name == name:
                print(f"学生信息{s}")
                return
        print("学生信息未找到")


    def list_student(self):
        for s in self.student_list:
            print(s)


    def run(self):
        print(f"欢迎使用教务管理系统V{EduManagement.system_version}")

        while True:
            menu = """
            ########教务处系统#########
            #       1.添加学生信息     #
            #       2.修改学生信息     #
            #       3.删除学生信息     #
            #       4.查询学生信息     #
            #       5.列出学生信息     #
            #       6.退出系统        #
            ########################
            """
            print(menu)

            choice = input("请选择要执行的操作:")
            match choice:
                case "1":
                    self.add_student()
                case "2":
                    self.update_student()
                case "3":
                    self.delete_student()
                case "4":
                    self.find_student()
                case "5":
                    self.list_student()
                case "6":
                    print("bye")
                    break
                case _:
                    print("输入错误")

# 测试
if __name__ == '__main__':
    edu_management = EduManagement()
    edu_management.run()







