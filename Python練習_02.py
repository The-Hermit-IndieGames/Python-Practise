import requests
from bs4 import BeautifulSoup

# 取得 HTML
url = "https://www.cwa.gov.tw/V8/C/W/Town/index.html"
headers = {"User-Agent": "Mozilla/5.0"}  # 模擬瀏覽器
response = requests.get(url, headers=headers)

# 解析 HTML
soup = BeautifulSoup(response.text, "html.parser")

# 1. 透過標籤名稱選取
title = soup.find("h2").text  # "文章標題"
print("title = " + title)  # 取得 HTML 內容
