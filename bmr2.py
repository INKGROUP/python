"""
 author:nick
"""


def main():

    y_or_n =  input("quit?(Y/N): ")
    while y_or_n != "Y":
        gender = input("sexy: ")
        wight = float(input("weight:(kg) "))
        height = float(input("height:(cm) "))
        age = int(input("age: "))

        if gender == "男":
            bmr = 13.7 * wight + 5.9 * height - 6.8 * age + 66
        elif gender == "women":
            bmr = 9.6 * wight + 1.8 * height - 47 * age + 655
        else:
            bmr = -1

        if bmr != -1:
            print("basic bmr:", bmr)
        else:
            print("Doesn't support")

        print()
        y_or_n = input("quit?(Y/N): ")

if __name__ == "__main__":
    main()
