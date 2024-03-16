import os

import requests
import privateinfo
import get_weather
from telebot import types
from random import choice, randint
linkhstoday='https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign='
linkhstmw='https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-tomorrow.aspx?sign='
linkhsmonth='https://www.horoscope.com/us/horoscopes/general/horoscope-general-monthly.aspx?sign='
linkhsyear='https://www.horoscope.com/us/horoscopes/yearly/2024-horoscope-'
textquestion='Ask me a question'
textanotherquestion = 'Ask me another question'
getsonyaphoto = 'Get Sonya photo ᓚ₍ ^. .^₎'
back_menu = 'Back to main menu'
fortune_ = 'What\'s my fortune today? ❤'
answers = ['That depends on you', 'Yes of course', 'Chatprivateinfo.bot Binnie will help you', 'Not tomorrow']
sharm = 'Sharm El-Sheikh'
cairo = 'Cairo'
moscow = 'Moscow'
zelen = 'Zelenogorsk'
location='My location'
horoscope='Horoscope'
today_horoscope='Today'
tmw_horoscope='Tomorrow'
month_horoscope='Month'
year_horoscope='Year'
capricorn_='Capricorn♑'
cancer_='Cancer♋'
scorpio_='Scorpio♏'
libra_='Libra♎'
virgo_='Virgo♍'
aquarius_='Aquarius♒'
aries_='Aries♈'
taurus_='Taurus♉'
gemini_='Gemini♊'
leo_='Leo♌'
pisces_='Pisces♓'
sagittarius_='Sagittarius♐'
course_rate='Course Exchange rate'
dollar='Dollar'
euro='Euro'
egp='Egyptian Pound'
msg_horoscope='Choose zodiac sign'
sharmpic='Picture of Sharm El-Sheikh'


sharmpicway='C:\\Users\\Alia\\Downloads\\sharm_pics'
sonyaphotoway='C:\\Users\\Alia\\Pictures\\Соня'
horoscope_type=''

def horoscopeprocess(message):
    link = ''
    hstext = None
    if horoscope_type==today_horoscope:
        link=linkhstoday
    elif horoscope_type==tmw_horoscope:
        link=linkhstmw
    elif horoscope_type==month_horoscope:
        link=linkhsmonth
    elif horoscope_type==year_horoscope:
        link=linkhsyear
    if message.text== scorpio_ :
        if link==linkhsyear:
            data = requests.get(f'{link}scorpio.aspx')
            hstext=gethoroscopeyear(data)
        else:
            data = requests.get(f'{link}8')
            hstext=gethoroscopetoday(data)
        privateinfo.bot.send_message(message.chat.id, hstext)
    elif message.text== aries_ :
        if link == linkhsyear:
            data = requests.get(f'{link}aries.aspx')
            hstext = gethoroscopeyear(data)
        else:
            data = requests.get(f'{link}1')
            hstext=gethoroscopetoday(data)
        privateinfo.bot.send_message(message.chat.id, hstext)
    elif message.text== taurus_ :
        if link == linkhsyear:
            data = requests.get(f'{link}taurus.aspx')
            hstext = gethoroscopeyear(data)
        else:
            data = requests.get(f'{link}2')
            hstext=gethoroscopetoday(data)
        privateinfo.bot.send_message(message.chat.id, hstext)
    elif message.text== gemini_ :
        if link == linkhsyear:
            data = requests.get(f'{link}gemini.aspx')
            hstext = gethoroscopeyear(data)
        else:
            data = requests.get(f'{link}3')
            hstext=gethoroscopetoday(data)
        privateinfo.bot.send_message(message.chat.id, hstext)
    elif message.text== cancer_ :
        if link == linkhsyear:
            data = requests.get(f'{link}cancer.aspx')
            hstext = gethoroscopeyear(data)
        else:
            data = requests.get(f'{link}4')
            hstext=gethoroscopetoday(data)
        privateinfo.bot.send_message(message.chat.id, hstext)
    elif message.text== leo_ :
        if link == linkhsyear:
            data = requests.get(f'{link}leo.aspx')
            hstext = gethoroscopeyear(data)
        else:
            data = requests.get(f'{link}5')
            hstext=gethoroscopetoday(data)
        privateinfo.bot.send_message(message.chat.id, hstext)
    elif message.text== virgo_ :
        if link == linkhsyear:
            data = requests.get(f'{link}virgo.aspx')
            hstext = gethoroscopeyear(data)
        else:
            data = requests.get(f'{link}6')
            hstext=gethoroscopetoday(data)
        privateinfo.bot.send_message(message.chat.id, hstext)
    elif message.text== libra_ :
        if link == linkhsyear:
            data = requests.get(f'{link}libra.aspx')
            hstext = gethoroscopeyear(data)
        else:
            data = requests.get(f'{link}7')
            hstext=gethoroscopetoday(data)
        privateinfo.bot.send_message(message.chat.id, hstext)
    elif message.text == sagittarius_ :
        if link == linkhsyear:
            data = requests.get(f'{link}sagittarius.aspx')
            hstext = gethoroscopeyear(data)
        else:
            data = requests.get(f'{link}9')
            hstext = gethoroscopetoday(data)
        privateinfo.bot.send_message(message.chat.id, hstext)
    elif message.text== capricorn_ :
        if link == linkhsyear:
            data = requests.get(f'{link}capricorn.aspx')
            hstext = gethoroscopeyear(data)
        else:
            data = requests.get(f'{link}10')
            hstext=gethoroscopetoday(data)
        privateinfo.bot.send_message(message.chat.id, hstext)
    elif message.text== aquarius_ :
        if link == linkhsyear:
            data = requests.get(f'{link}aquarius.aspx')
            hstext = gethoroscopeyear(data)
        else:
            data = requests.get(f'{link}11')
            hstext=gethoroscopetoday(data)
        privateinfo.bot.send_message(message.chat.id, hstext)
    elif message.text == pisces_ :
        if link == linkhsyear:
            data = requests.get(f'{link}pisces.aspx')
            hstext = gethoroscopeyear(data)
        else:
            data = requests.get(f'{link}12')
            hstext = gethoroscopetoday(data)
        privateinfo.bot.send_message(message.chat.id, hstext)
    return hstext


def gethoroscopetoday(data):
    hstext = ''
    for i in range(len(data.text) - 100):
        if data.text[i] == '/' and data.text[i + 1] == 's' and data.text[i + 2] == 't' and data.text[i + 3] == 'r':
            for j in range(i + 5 + 6, i + 5 + 7 + 3000):
                if data.text[j] == '<':
                    break
                hstext += data.text[j]
            break
    print(hstext)
    return hstext

def gethoroscopeyear(data):
    hstext = ''
    allow=True
    for i in range(len(data.text) - 100):
        if data.text[i] == '<' and data.text[i + 1] == '/' and data.text[i + 2] == 'h' and data.text[i + 3] == '2' and data.text[i + 4] == '>':
            for j in range(i + 5 +5 , i + 5 + 7 + 3000):
                if data.text[j] == '<' and data.text[j+1] == '/' and data.text[j+2] == 'p':
                    break
                if data.text[j]== '<':
                    allow=False
                if data.text[j] == '&':
                    allow=False
                if allow==True:
                    hstext += data.text[j]
                if data.text[j] == '>':
                    allow=True
                if data.text[j] == ';':
                    allow=True
            break
    print(hstext)
    return hstext

def create_horoscope_menu():
    horoscopemenu=types.ReplyKeyboardMarkup(resize_keyboard=True)
    capricorn=types.KeyboardButton(text=capricorn_)
    cancer=types.KeyboardButton(text=cancer_)
    scorpio=types.KeyboardButton(text=scorpio_)
    libra = types.KeyboardButton(text=libra_)
    virgo = types.KeyboardButton(text=virgo_)
    aquarius = types.KeyboardButton(text=aquarius_)
    aries = types.KeyboardButton(text=aries_)
    taurus = types.KeyboardButton(text=taurus_)
    gemini = types.KeyboardButton(text=gemini_)
    leo = types.KeyboardButton(text=leo_)
    pisces = types.KeyboardButton(text=pisces_)
    sagittarius = types.KeyboardButton(text=sagittarius_)
    backmenu = types.KeyboardButton(text=back_menu)
    horoscopemenu.add(capricorn, scorpio, cancer, libra, leo, virgo, aquarius, aries,
                      taurus, gemini, pisces, sagittarius, backmenu)
    return horoscopemenu

def createmainmenu():
    mainmenu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    infowiki = types.KeyboardButton(text='Wikipedia')
    weather = types.KeyboardButton(text='Weather')
    location_ = types.KeyboardButton(text=location)
    sonya = types.KeyboardButton(text=getsonyaphoto)
    question = types.KeyboardButton(text=textquestion)
    fortune = types.KeyboardButton(text=fortune_)
    horoscope_=types.KeyboardButton(text=horoscope)
    courserate=types.KeyboardButton(text=course_rate)
    sharmpic_=types.KeyboardButton(text=sharmpic)
    mainmenu.add(infowiki, weather, location_, sonya, question, fortune, horoscope_, courserate, sharmpic_)
    return mainmenu

def weatherlocation():
    weathermenu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    cairo_ = types.KeyboardButton(text=cairo)
    sharm_ = types.KeyboardButton(text=sharm)
    moscow_ = types.KeyboardButton(text=moscow)
    zelenogorsk = types.KeyboardButton(text=zelen)
    backMenu = types.KeyboardButton(text=back_menu)
    weathermenu.add(cairo_, sharm_, moscow_, zelenogorsk, backMenu)
    return weathermenu

@privateinfo.bot.message_handler(commands=['start'])

def greeting(message):
    greetinguser=f'Hello {message.from_user.first_name} {message.from_user.last_name}'
    mainmenu=createmainmenu()
    privateinfo.bot.send_message(message.chat.id, greetinguser, reply_markup=mainmenu)

isask=False

@privateinfo.bot.message_handler(content_types=['location'])
def locoation_toAdmin(message):
    if message.location is not None:
        privateinfo.bot.send_message(privateinfo.privateinfo.myid, message.location)

@privateinfo.bot.message_handler(content_types=['text'])

def communication(message):
    global isask, horoscope_type

    if isask==True:
        answer=f'{message.from_user.first_name} {choice(answers)}'
        smallmenu=types.ReplyKeyboardMarkup(resize_keyboard=True)
        anotherquestion=types.KeyboardButton(text=textanotherquestion)
        backmenu=types.KeyboardButton(text=back_menu)
        smallmenu.add(anotherquestion, backmenu)
        privateinfo.bot.send_message(message.chat.id, answer, reply_markup=smallmenu)
        isask=False
        return
    if message.text=='how are you':
        answer=f'good, thanks {message.from_user.first_name}'
        privateinfo.bot.send_message(message.chat.id, answer)
    elif message.text==textquestion or message.text==textanotherquestion:
        privateinfo.bot.send_message(message.chat.id, 'Ask me')
        isask=True
    elif message.text==back_menu:
        menu=createmainmenu()
        privateinfo.bot.send_message(message.chat.id, 'you have returned to main menu', reply_markup=menu)
    elif message.text==getsonyaphoto:
        sonyalist=os.listdir(sonyaphotoway)
        randomsonyaphoto=choice(sonyalist)
        allwayphoto=os.path.join(sonyaphotoway, randomsonyaphoto)
        with open(allwayphoto, 'rb') as sonya:
            privateinfo.bot.send_photo(message.chat.id, sonya)
    elif message.text==fortune_:
        magicnumber=randint(1,9)
        with open(f"{magicnumber}.txt", 'r') as file:
            info=file.read()
            privateinfo.bot.send_message(message.chat.id, info)
    elif message.text=='Weather':
        menu = weatherlocation()
        privateinfo.bot.send_message(message.chat.id, 'Choose a city', reply_markup=menu)
    elif message.text==sharm:
        privateinfo.bot.send_message(message.chat.id, get_weather.getweather(sharm))
    elif message.text==cairo:
        privateinfo.bot.send_message(message.chat.id, get_weather.getweather(cairo))
    elif message.text==zelen:
        privateinfo.bot.send_message(message.chat.id, get_weather.getweather(zelen))
    elif message.text == moscow:
        privateinfo.bot.send_message(message.chat.id, get_weather.getweather(moscow))
    elif message.text==location:
        location_menu=types.ReplyKeyboardMarkup(resize_keyboard=True)
        location_btn=types.KeyboardButton(text='Map with my location', request_location=True)
        location_menu.add(location_btn)
        privateinfo.bot.send_message(message.chat.id, 'Now your location will be sent', reply_markup=location_menu)
    elif message.text==horoscope:
        horoscope_menu=types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_today=types.KeyboardButton(text=today_horoscope)
        btn_tmw=types.KeyboardButton(text=tmw_horoscope)
        btn_month=types.KeyboardButton(text=month_horoscope)
        btn_year=types.KeyboardButton(text=year_horoscope)
        btn_back=types.KeyboardButton(text=back_menu)
        horoscope_menu.add(btn_today, btn_tmw, btn_month, btn_year, btn_back)
        privateinfo.bot.send_message(message.chat.id, 'What horocope would you like?', reply_markup=horoscope_menu)
    elif message.text==today_horoscope:
        horoscope_type=today_horoscope
        privateinfo.bot.send_message(message.chat.id, msg_horoscope, reply_markup=create_horoscope_menu())
    elif message.text == tmw_horoscope:
        horoscope_type = tmw_horoscope
        privateinfo.bot.send_message(message.chat.id, msg_horoscope, reply_markup=create_horoscope_menu())
    elif message.text == month_horoscope:
        horoscope_type = month_horoscope
        privateinfo.bot.send_message(message.chat.id, msg_horoscope, reply_markup=create_horoscope_menu())
    elif message.text == year_horoscope:
        horoscope_type = year_horoscope
        privateinfo.bot.send_message(message.chat.id, msg_horoscope, reply_markup=create_horoscope_menu())

    elif message.text==course_rate:
        courserate = types.ReplyKeyboardMarkup(resize_keyboard=True)
        dollar_ = types.KeyboardButton(text=dollar)
        euro_ = types.KeyboardButton(text=euro)
        egp_ = types.KeyboardButton(text=egp)
        backmenu=types.KeyboardButton(text=back_menu)
        courserate.add(dollar_, euro_, egp_, backmenu)
        privateinfo.bot.send_message(message.chat.id, 'What currency would you like to see?', reply_markup=courserate)
    elif message.text==sharmpic:
        sharmphotolist=os.listdir(sharmpicway)
        randsharmpic=choice(sharmphotolist)
        allwayphoto=os.path.join(sharmpicway, randsharmpic)
        with open(allwayphoto, 'rb') as sharmpic_:
            privateinfo.bot.send_photo(message.chat.id, sharmpic_)


    else:
        message=horoscopeprocess(message)
        if message is None:
            privateinfo.bot.send_message(message.chat.id, 'this command doesnt work yet')
            privateinfo.bot.send_message(privateinfo.myid, f'teach me this command: {message.text}')

privateinfo.bot.polling(none_stop=True)