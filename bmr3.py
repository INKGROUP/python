"""
 author:nick
"""


def main():
    print("input your info, use space to split")
    input_str = input("sexy weight(kg) height(cm) age").split(" ")

    y_or_n = input("quit?(Y/N): ")
    while y_or_n != "Y":
        try:
            gender = input_str[0]
            wight = float(input_str[1])
            height = float(input_str[2])
            age = int(input_str[3])

            if gender == "man":
                bmr = 13.7 * wight + 5.9 * height - 6.8 * age + 66
            elif gender == "women":
                bmr = 9.6 * wight + 1.8 * height - 47 * age + 655
            else:
                bmr = -1

            if bmr != -1:
                print("basic bmr:{}大卡".format(bmr))
            else:
                print("Doesn't support")
        except ValueError:
            print("check your info please")
        except:
            print("exception")

        y_or_n = input("quit?(Y/N): ")


if __name__ == "__main__":
    main()
