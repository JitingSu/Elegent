# 通过正则表达式简单验证身份证号是否合法
import re


def verification(id_number):
    # 身份证号的格式
    pattern = r"(^\d{15}$)|(^\d{17}([0-9]|x)$)"
    result = re.match(pattern, id_number)
    if result:
        print("身份证号格式正确")
    else:
        print("身份证号格式不正确")


verification("431133198903270330")
