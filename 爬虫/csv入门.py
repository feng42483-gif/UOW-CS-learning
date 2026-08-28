# csv原始方式
# with open("csv_data/01.csv","w",encoding="utf-8")as f:
 # 写入表头
    # f.write("姓名，年龄，性别，爱好\n")
    # 写入数据
    # f.write("小王，18，男，football\n")
    # f.write("小李，18，女，python\n")
    # f.write("小张，19，男，c++\n")
    # f.write("小刘，23，男，go\n")
# 读
# with open("csv_data/01.csv","r",encoding="utf-8")as f:
#     for line in f:
#         print(line.strip())

# csv操作——方式二
import csv
with open("csv_data/02.csv","w",encoding="utf-8", newline="")as f:
    writer = csv.DictWriter(f,fieldnames=["姓名","年龄","性别","爱好"])
    # 写入表头
    writer.writeheader()
    # 写入数据
    writer.writerow({"姓名":"小王","年龄": 18,"性别":"男","爱好":"python"})
    writer.writerow({"姓名":"小李","年龄": 23,"性别":"女","爱好":"c++"})
    writer.writerow({"姓名":"小张","年龄": 20,"性别":"男","爱好":"football"})
    writer.writerow({"姓名":"小红","年龄": 19,"性别":"男","爱好":"R"})