"""
 author:nick
"""
import math

def main():
    money_per_week = 10
    i = 1
    increase_money = 10
    total_week = 52
    saving = 0
    money_list = []
    for i in range(total_week):
        money_list.append(money_per_week)
        saving = math.fsum(money_list)
        print("第{}周，存入{}元，账户累计{}元".format(i+1, money_per_week, saving))
        money_per_week += increase_money
        i += 1

if __name__ == "__main__":
    main()
