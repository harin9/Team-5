from urllib.request import urlopen
from bs4 import BeautifulSoup

day = input('day : ')
html = urlopen("https://comic.naver.com/webtoon/weekdayList.nhn?week=%s&order=StarScore&view=image" %day)

soup = BeautifulSoup(html, "lxml")

chart_table = soup.find_all('div',{'class':'list_area daily_img'})

chart_table_div=chart_table[0].find_all("ul",{'class':'img_list'})

li = chart_table_div[0].find_all('li')

a = []
for i in li:
    b = []
    dt = i.find_all('dt')
    strong = i.find_all('strong')


    for m in dt:
        print(m.get_text(), end = ' ')
        b.append(m.get_text())

    for m in strong:
        print(m.get_text())
        b.append(float(m.get_text()))
    print('')
    a.append(b)

print('')

web = []
star = []

count = 0
for i in a:
    count += 1
    web.append(i[0])
    star.append(i[1])
    if count == 10:
        break

print(web)
print(star)