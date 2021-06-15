import requests
import urllib
from bs4 import BeautifulSoup as BS

def getInfo(teacher_name, find_info):
    url = "https://research.osakac.ac.jp/index.php?" + urllib.parse.quote(teacher_name)
    site = requests.get(url)
    data = BS(site.text, "html.parser")

    print(data.title.text)
    tab_data = data.select(".list1")

    select_data = [i.text for i in tab_data if find_info in i.text]
    if select_data is None:
        select_data = data.find_all(text = find_info)[0].string
    return select_data[0]