<<<<<<< HEAD
from selenium import webdriver

driver_path = './chromedriver'

driver = webdriver.Chrome(driver_path, options=options)
variable = driver.current_url

print(variable)
=======
# a, b = input('숫자 두 개를 입력하세요: ').split()

# print(a,b)
# print("asdasd%s \n asdasd%s"% (a,b))

import urllib.parse

for i in range(0,30,10):
    if (i == 0):
        pluseurl = input('검색어를 터미널에서 입력하세요 : ')
        url = 'https://www.google.com/search?q=%s' %(pluseurl)
    ch = "&start=%d" % (i)
    churl = url + ch
    print(churl)
>>>>>>> c78d4edcfbb12d64451fb656c864be0a90aec917