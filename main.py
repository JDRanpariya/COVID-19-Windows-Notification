from plyer import notification
import requests
import time
import sys,io
from bs4 import BeautifulSoup


def notify(title,message):
    notification.notify(
        title= title,
        message = message,
        app_icon = 'C://Users//Dell//Projects//Web_Scraping//Corona_Notification_Windows//corona.ico',
        #app_icon= None
        app_name = 'COVID-19 Report',
        timeout = 7,
        
        )

def getdata(url):
        
        r = requests.get(url)
        return r.text

if __name__ == "__main__":

    
 while True:
    data = getdata('https://www.worldometers.info/coronavirus/')

    #print(data)
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer,'cp437','backslashreplace')
    soup = BeautifulSoup(data, 'html.parser')
    soup.prettify()
    
    noofcases =soup.find_all("div",{'class' : 'maincounter-number'})[0].text
    noofdeaths = soup.find_all("div",{'class' : 'maincounter-number'})[1].text
    noofrecovery = soup.find_all("div",{'class' : 'maincounter-number'})[2].text
    #print(soup.find_all("div",{'class' : 'maincounter-number'}))

    messagef = f"Total Cases : {noofcases.strip()} \n Deaths : {noofdeaths.strip()}\n Recovered : {noofrecovery.strip()}"

    notify('Global COVID-19 Report', messagef)
    time.sleep(3600)


pass

