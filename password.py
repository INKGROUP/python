"""
 author:nick
"""


def check_number_exist(password):
    for c in password:
        if c.isnumeric():
            return True
    return False


def check_letter_exist(password):
    for c in password:
        if c.isalpha():
            return True
    return False

def main():
    password = input("input password")
    strength_levev = 0
    # 规则1：密码长度大于8
    if len(password) >= 8:
        strength_levev +=1
    else:
        print("密码不能少于8位")

    # 规则2：包含数字
    if check_number_exist(password):
        strength_levev += 1
    else:
        print("必须含有数字")

    # 规则2：包含数字
    if check_letter_exist(password):
        strength_levev += 1
    else:
        print("必须含有字母")

    if strength_levev == 3:
        print("恭喜，密码强度合格")
    else:
        print("密码强度不合格")

if __name__ == "__main__":
    main()