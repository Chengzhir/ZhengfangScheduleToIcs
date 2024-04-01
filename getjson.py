## 这个函数是用来获取指定url返回的json响应数据并保存为data.json
import json
import requests

# 发送 API 请求获取 JSON 数据
response = requests.get("http://www.gdjw.zjut.edu.cn/jwglxt/kbcx/xskbcx_cxXsgrkb.html?gnmkdm=N253508")
# print(response.text)
# 解析 JSON 数据
data = json.loads(response.text)

# 将数据写入本地文件
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False)
