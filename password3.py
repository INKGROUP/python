"""
 author:nick
"""


def check_number_exist(password):
    has_number = False
    for c in password:
        if c.isnumeric():
            has_number = True
            break
    return has_number


def check_letter_exist(password):
    has_letter = False
    for c in password:
        if c.isalpha():
            has_letter = True
            break
    return has_letter


def main():
    times = 5

    while times > 0:
        password = input("input password")
        strength_level = 0
        # 规则1：密码长度大于8
        if len(password) >= 8:
            strength_level += 1
        else:
            print("密码不能少于8位")

        # 规则2：包含数字
        if check_number_exist(password):
            strength_level += 1
        else:
            print("必须含有数字")

        # 规则2：包含数字
        if check_letter_exist(password):
            strength_level += 1
        else:
            print("必须含有字母")

        f = open('password3.0.txt', 'a')
        f.write('密码：{},强度：{}\n'.format(password, strength_level))
        f.close()

        if strength_level == 3:
            print("恭喜，密码强度合格")
            break
        else:
            print("密码强度不合格")
            times -= 1

    if times <= 0:
        print("你已经超过5次了")


if __name__ == "__main__":
    main()