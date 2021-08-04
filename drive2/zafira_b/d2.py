import requests
from bs4 import BeautifulSoup
import telebot
# -*- coding: utf-8 -*-

bot_id = '1728590521:AAFaHbiXfpD2yx_Iz8-px6RTe0E0INQ7lMc'
chat_id = '-1001295855582'	#Meriva B chat
#test_chat_id = '-1001499088147' #test chat
admin_chat_id = '219922526'
url = 'https://www.drive2.ru/cars/opel/zafira/g1738/' #URL Zafira B
url_path = '/home/ubuntu/python/drive2/zafira_b/link.txt'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.',
}

f = open(url_path)
for current_link in f.readlines():
    print (current_link),
f.close()

r = requests.get(url, headers=HEADERS)
soup = BeautifulSoup(r.text, 'lxml')
string = (str(soup.findAll('a')))
start = string.find('href="/l/')
string = string[start+3:start+34]
piece = string.split('"')
link = 'https://www.drive2.ru' + str(piece[1])

#print(type(link), type(current_link))
#print(current_link)
#print(link != current_link)

if (link != current_link):
    bot = telebot.TeleBot(bot_id)
    bot.send_message(chat_id, 'Новый пост на Drive2 ' + link)
    bot.send_message(admin_chat_id, 'Новый пост найден и опубликован на канал Zafira B ' + link)
    file = open(url_path, 'w')
    file.write(link)
    file.close()
    print('Новый пост отправлен в телеграм!')

else:
    print('Обновлений нет')
    bot = telebot.TeleBot(bot_id)
    bot.send_message(admin_chat_id, 'Новых постов про Zafira B нет')
