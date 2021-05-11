from urllib.request import urlopen
from bs4 import BeautifulSoup

day = input('day : ')
html = urlopen("https://comic.naver.com/webtoon/weekdayList.nhn?week=%s&order=StarScore&view=image" %day)

soup = BeautifulSoup(html, "lxml")

chart_table = soup.find_all('div',{'class':'list_area daily_img'})

chart_table_div=chart_table[0].find_all("ul",{'class':'img_list'})

li = chart_table_div[0].find_all('li')