import requests
from lxml import html



# 定义url
target_url = "https://www.tiobe.com/tiobe-index/"

# 发出请求，获取数据
response =  requests.get(target_url)

# 输出数据
# print(response.text)
document = html.fromstring(response.text)


# 解析数据
th_list =  document.xpath("//table[@id='top20']/thead/tr/th/text()")
print(th_list)

# 解析表格数据
tr_list =  document.xpath("//table[@id='top20']/tbody/tr")
# print(tr_list)
for tr in tr_list:
    td_list = tr.xpath("./td/text()")
    print(td_list)