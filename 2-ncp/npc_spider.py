import requests

url = 'https://ncov.dxy.cn/ncovh5/view/pneumonia_peopleapp'

txt = requests.get(url).text
print(txt)