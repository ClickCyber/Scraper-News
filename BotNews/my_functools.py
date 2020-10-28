import requests, bs4


def get_news_ynet():
    respones = requests.get('https://www.ynet.co.il/news')
    element = bs4.BeautifulSoup(respones.text, 'html.parser')
    News = element.find('div', class_='textDiv')
    link = str(News.h1.a)[9:]
    link = link[:link.find('"')]
    return {'link_post':link, 'captoin':News.text, 'service':'ynet'}


def get_news_calcalist():
    respones = requests.get('https://www.calcalist.co.il/home/0,7340,L-8,00.html')
    element = bs4.BeautifulSoup(respones.text, 'html.parser')
    body = element.find('div', class_='CdaTopStory1280')
    link = str(body.find('h2',class_='ts-title-sivug'))[str(body.find('h2',class_='ts-title-sivug')).find('href') + 6:str(body.find('h2',class_='ts-title-sivug')).find('html')+4]
    text =  str(body.find('h2',class_='ts-title-sivug'))[str(body.find('h2',class_='ts-title-sivug')).rfind('span') + 5: -9]
    captoin = str(element.find('div', class_='ts-sub-title'))[str(element.find('div', class_='ts-sub-title')).rfind('html')+6: -10]
    text = text + captoin
    return {'link_post':f'https://www.calcalist.co.il/{link}', 'captoin':text, 'service':'calcalist'}



def get_news_geektime():
    respones = requests.get('https://www.geektime.co.il/')
    element = bs4.BeautifulSoup(respones.text, 'html.parser')
    body = element.find('div', class_='featured-entry large-featured-entry right first')
    return body
