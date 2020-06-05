"""
作者：殷腾飞
"""

# rmb_str_value = input("input count:")
# rmb_value = eval(rmb_str_value)
#
# usd_vs_rmb = 6.77
# usd_value = rmb_value / usd_vs_rmb
#
# print(usd_value)


def convert_currency(im, er):
    out = im * er
    return out


def main():
    USD_VS_RMB = 6.77
    # 带单位的货币输入
    currency_str_value = input("输入带单位的金额")
    # while currency_str_value != 'Q':
    unit = currency_str_value[-3:]
    if unit == "CNY":
        exchange_rate = 1 / USD_VS_RMB
        # rmb_str_value = currency_str_value[:-3]
        # rmb_value = eval(rmb_str_value)
        # usd_value = rmb_value / USD_VS_RMB
        # print("美元金额：", usd_value)
    elif unit == "USD":
        exchange_rate = USD_VS_RMB
        # usd_str_value = currency_str_value[:-3]
        # usd_value = eval(usd_str_value)
        # rmb_value = usd_value * USD_VS_RMB
        # print("人民币金额：", rmb_value)
    else:
        exchange_rate = -1
        # print("暂不支持")

    # currency_str_value = input("输入带单位的金额")

    if exchange_rate != -1:
        in_money = eval(currency_str_value[:-3])

        convert_currency2 = lambda x:x * exchange_rate
        # out_money = convert_currency(in_money, exchange_rate)
        out_money = convert_currency2(in_money)
        print("换后金额", out_money)
    else:
        print("not support!")


if __name__ == "__main__":
    main()