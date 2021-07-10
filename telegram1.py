import telebot
import random, time
import mnogochlen
import weather2fromweathermap
bot = telebot.TeleBot('1836713851:AAHnJhLnZX-aFlDlh5om8a1iPLIvXtbFxHI')
massiveofvisitors=100*[0]
massi=0
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, f'Я бот. Приятно познакомиться, {message.from_user.first_name}')
    bot.send_message(message.from_user.id, 'используй /help чтобы узнать все возможности')
    print(message.from_user.id)
    global massi
    massiveofvisitors[massi]=2*[0]
    massiveofvisitors[massi][0]=message.from_user.id
    massi+=1
    
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, 'команды: /start, /help, /mathhelp')
    bot.reply_to(message, 'запросы: привет, помоги с математикой, рандом, рандомное число от m до n')
@bot.message_handler(commands=['mathhelp'])
def send_mathhelp(message):
    bot.reply_to(message, 'kkk')
@bot.message_handler(commands=['mnogochlen'])
def mnogochlen(message):
    bot.reply_to(message, 'hello, my king')
    massiveofvisitors[massiveofvisitors.index(message.from_user.id)][1]='king'



@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'Привет!')
    elif message.text.lower() in ('погода', 'погода в екатеринбурге', 'weather', 'weather in ekaterinburg'):
        bot.send_message(message.from_user.id, weather2fromweathermap.weathernow('Ekaterinburg,RU'))
    elif message.text.lower() == 'помоги с математикой':
        bot.send_message(message.from_user.id, 'без проблем, что ты хочешь, узнай больше с помощью /mathhelp')
    elif message.text.lower() in ('рандом', 'сгенерируй рандомное число от 0 до 1'):
        bot.send_message(message.from_user.id, random.random())
    elif ((message.text.lower()).count('рандомное число')>0 or (message.text.lower()).count('рандомная цифра')>0) and ((message.text.lower()).count('от')>0 and (message.text.lower()).count('до')>0):
        thismessage=(message.text.lower()).split(' ')
        minint=''
        maxint=''
        for i in range (len(thismessage)):
            if thismessage[i].isdigit():
                if minint=='':
                    minint=int(thismessage[i])
                else :
                    maxint=int(thismessage[i])
        #bot.send_message(message.from_user.id, str(minint)+ str(maxint))    
        
        bot.send_message(message.from_user.id, random.randint(minint, maxint))    
    else:
        bot.send_message(message.from_user.id, 'Не понимаю, что это значит.')
bot.polling(none_stop=True)
#'сгенерируй рандомную цифру'
