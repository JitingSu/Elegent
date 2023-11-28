import requests

# 发送GET请求
response = requests.get("https://baidu.com")

# 获取网页内容
html_content = response.text.encode(response.encoding).decode() 

# 打印网页内容
print(html_content)