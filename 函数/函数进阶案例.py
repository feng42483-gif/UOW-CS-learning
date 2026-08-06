# 递归函数：自己调用自己，一定要有终结点(先层层递进，再逐步回归)
# def calc(ar):
#     if ar == 1:
#         return 1
#     else:
#         return ar * calc(ar - 1)
# result = calc(6)
# print(result)

# 案例1
"""
定义 一个用于根据传入的一批商品信息（商品名，价格，数量），优惠（优惠劵，积分抵扣），运费信息计算订单的总金额函数。
优惠卷需要商品金额满5000才可以使用，且优惠金额不得超过商品总价
积分抵扣需要商品界满5000才可以使用，100积分抵扣1元（且抵扣金额不能超过商品总价，积分只能整百抵扣。）
"""


def clac_goods_price(*args:tuple[str,float,int], coupon, score, express):
    """

       :param args:商品信息
       :param coupon:优惠卷
       :param score:积分
       :param express:运费
       :return:
       """
    # 商品总额
    total_price = [goods[1] * goods[2] for goods in args]
    total_cost = sum(total_price)

    # 优惠券
    if total_cost >= 5000 and coupon <= total_cost:
        total_cost -= coupon

    # 积分抵扣
    if total_cost >= 5000:
        score_money = score // 100 * 1
        total_cost -= min(score_money, total_cost)

    # 加运费
    total_cost += express

    return total_cost
total = clac_goods_price(("鼠标",200,2),("键盘",300,2),("laptop",5000,1),coupon=10,score=1000,express=10  )
print(total)