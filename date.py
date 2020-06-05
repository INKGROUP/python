"""
 author:nick
"""
from datetime import datetime

def main():
    input_date_str = input("请输入日期（yyyy/mm/dd）:")
    input_date = datetime.strptime(input_date_str, '%Y/%m/%d')
    print(input_date)
    year = input_date.year
    month = input_date.month
    day = input_date.day
    print(year, month, day)

    days_in_month_tup = (31, 28, 31, 30)



    pass




if __name__ == "__main__":
    main()
