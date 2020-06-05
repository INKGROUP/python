"""
 author:nick
"""


def main():
    print("Doesn't support")
    gender = "男"
    wight = 70
    height = 175
    age = 25

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


if __name__ == "__main__":
    main()
