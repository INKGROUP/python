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


class FileTool:
    def __init__(self, filepath):
        self.filepath = filepath

    def write_file(self, line):
        f = open(self.filepath, 'a')
        f.write(line)
        f.close()

    def read_file(self):
        f = open(self.filepath, 'r')
        lines = f.readlines()
        f.close()
        return lines


def main():
    try_times = 5
    file_path = 'password3.0.txt'
    file_tool = FileTool(file_path)
    while try_times > 0:
        password = input("input password")
        password_tool = PasswordTool(password)
        password_tool.check_process()

        line = "密码：{}，强度：{}\n".format(password, password_tool.strength_level)
        file_tool.write_file(line)

        if password_tool.strength_level == 3:
            print("password set successfully")
            break
        else:
            print("不合格")

    if try_times <= 0:
        print("超过5次了")

    lines = file_tool.read_file()
    print(lines)


if __name__ == "__main__":
    main()