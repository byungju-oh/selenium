from selenium import webdriver
import urllib.request
import os
import time

search='하체비만'
url='https://www.google.co.in/search?q='+search+'&tbm=isch'
구글경로='C:/Users/qkd/python/chromedriver_win32/chromedriver.exe'
저장위치='E:/데이터사진/하체비만/'

driver=webdriver.Chrome(구글경로)
driver.get(url)
time.sleep(1)
link=[]
for i in range(200):

    try:
        time.sleep(0.5)
        driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div['+ str(i) +']/a[1]/div[1]/img').click()
        time.sleep(0.5)
        img=driver.find_element_by_xpath('//*[@id="Sva75c"]/div/div/div[3]/div[2]/div/div[1]/div[1]/div/div[2]/a/img')
        time.sleep(0.5)

        ui=img.get_attribute('src')
        filename=os.path.join(저장위치,search+str(i)+ '.jpg')
        t=urllib.request.urlopen(ui).read()
        with open(filename,"wb") as f:
            f.write(t)
            print('img save')
    except:
        continue

driver.close()
