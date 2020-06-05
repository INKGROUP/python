"""
 author:nick
"""


def main():
    money_per_week = 10
    i = 1
    increase_money = 10
    total_week = 52
    saving = 0
    while i <= total_week:
        saving += money_per_week

        print("第{}周，存入{}元，账户累计{}元".format(i, money_per_week, saving))
        money_per_week += increase_money
        i += 1



if __name__ == "__main__":
    main()
