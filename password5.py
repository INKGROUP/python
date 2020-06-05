"""
 author:nick
"""


class PasswordTool:
    def __init__(self, password):
        self.password = password
        self.strength_level = 0

    def check_process(self):
        # 规则1：密码长度大于8
        if len(self.password) >= 8:
            self.strength_level += 1
        else:
            print("密码不能少于8位")

        # 规则2：包含数字
        if self.check_number_exist():
            self.strength_level += 1
        else:
            print("必须含有数字")

        # 规则2：包含数字
        if self.check_letter_exist():
            self.strength_level += 1
        else:
            print("必须含有字母")

    def check_number_exist(self):
        has_number = False
        for c in self.password:
            if c.isnumeric():
                has_number = True
                break
        return has_number

    def check_letter_exist(self):
        has_letter = False
        for c in self.password:
            if c.isalpha():
                has_letter = True
                break
        return has_letter


def main():
    try_times = 5
    while try_times > 0:
        password = input("input password")
        password_tool = PasswordTool(password)
        password_tool.check_process()

        f = open("password3.0.txt", "a")
        f.write("密码：{}，强度：{}\n".format(password, password_tool.strength_level))
        f.close()

        if password_tool.strength_level == 3:
            print("password set successfully")
            break
        else:
            print("不合格")

    if try_times <= 0:
        print("超过5次了")


if __name__ == "__main__":
    main()