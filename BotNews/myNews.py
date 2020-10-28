import requests, time
from my_functools import get_news_ynet, get_news_calcalist
chat_id = '-1001241432791' # id group to send update
token = '1323518969:AAE4fKPcESPo_t5gI2xGosB-dY38CRg1dfM' # token api bot telegram
URL_API = 'https://api.telegram.org/bot{0}/sendmessage?chat_id={1}&text='.format(token, chat_id) # url to requestsn
def main():
    global old_news
    counter = {'send': 0, 'error': 0}
    while True:
        news_ynet = get_news_ynet()
        news_calcalist = get_news_calcalist()
        service_list = [news_ynet, news_calcalist]
        for news in service_list: # list service post
            
           # print(news['link_post'] + ' ' + old_news[news['service']])
            if not news['link_post'] == old_news[news['service']]:
                old_news[news['service']] = news['link_post']
                keyBoard = '&reply_markup={"inline_keyboard":[[{"text":"📲 לקריאה","url": "'+ old_news[news['service']].replace('#autoplay', '') + '"},{"text":"👨🏻‍💻 מנהל ","url":"t.me/writeXcode"}]]}'
                if requests.get(URL_API + f'תוכן: {news["captoin"]}{keyBoard}' ).json()['ok']:
                    counter['send'] += 1
                    print(f'SEND TO TRAGET [{counter["send"]}] service [{news["service"]}]')
                else:
                    counter['error'] += 1
                    print(f'ERROR FROM API TELEGRAM {counter["error"]} service [{news["service"]}]')
        
        time.sleep(120)





old_news = {'ynet':'https://www.ynet.co.il/article/Sk26w5ZOw#autoplay', 'calcalist':''}


main()
