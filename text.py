#
# # -*- coding: utf-8 -*-
# __author__ = 'Apple'
#
# def rebuild_area(item):
#     data = item.json
#     data["member"] = [require_member(ap, ac, am) for (ap, ac, am, ad) in query_data if ad == item.id]
#     member_data = [i for i in query_data if i[3] == item.id]
#     data['total_amount'] = float(sum([i[0] for i in member_data]))
#     data['gross_rate'] = None
#     if len(member_data):
#         data['gross_rate'] = round(float(sum([i[1] for i in member_data])) / len(member_data), 2)
#     return data
# # 过滤大于零的
#
# total_area = sorted([rebuild_area(i) for i in Area.query.all()], key=lambda x: x['total_amount'], reverse=True)[:10]
#
# # 1月1日至今的营业额统计
# item = db.session.query(db.func.sum(AccountPayment.bid_price)) \
#         .filter(db.and_(
#             AccountPayment.create_time > "2018-01-01",
#             AccountPayment.is_deleted == False,
#         )).first()
# total_amount_1_1 = float(item[0]) if item else 0
#
# a = [{"a":1,"b":2},{"a":2,"b":2},{"a":3,"b":2},{"a":4,"b":2}]
#
# a = filter(lambda x: x['a'] > 3, a)
# print(a)
#
# def rebuild_area(i):
#     data = {}
#     data['total_amount'] = i
#     data['gross_rate'] = None
#     return data
# b = [1,2,3,4,0]
#
# # middle = filter(lambda x: x['total_amount'] > 0, [rebuild_area(i) for i in b])
#
# total_area = sorted(filter(lambda x: x['total_amount'] > 0, [rebuild_area(i) for i in b]), key=lambda x: x['total_amount'], reverse=True)[:10]
#
# print total_area
import datetime
import time
def get_day_nday_ago(n):
    d = datetime.datetime.now()
    Date = str(datetime.datetime(d.year, d.month,d.day) - datetime.timedelta(n)).split()
    return Date[0]

# 示例
a=get_day_nday_ago(30)
print a