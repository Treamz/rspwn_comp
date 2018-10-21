import time
from time import sleep
import telebot
from telebot import types
import urllib.request
import urllib.parse
import re


API_TOKEN = '688874394:AAFQn7xHTC81w0n5i-kFipO0sod4a8xc5Mg'

bot = telebot.TeleBot(API_TOKEN)

user_dict = {}

class User:
    def __init__(self, name):
        self.name = name
        self.ref = None




# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    msg = bot.reply_to(message, """\
Хочешь принять участие в конкурсе? Тогда пиши /competition
""")

# Handle '/start' and '/help'
@bot.message_handler(commands=['me', 'shance'])
def send_shance(message):
    excpt = True
    while(excpt):
        try:
            uname = "username="+message.from_user.username
            data = uname.encode("ascii")
            response = urllib.request.urlopen("http://treamz.zzz.com.ua/shance.php",data)
            html = response.read().decode("utf-8") # utf-8 чтобы принять русские буквы
            excpt = False
            if "Нет шансов" in html:
                bot.send_message(message.chat.id, "<b>Ты пригласил меньше 2ух друзей, у тебя нет шансов :c</b>", parse_mode="HTML")
            else: 
                print(html)
                parts = html.rsplit('%%%', 2)  # ['my-name-1.my', 'lovely', 'local']
                me_sh = parts[0]  # my-name-1.my
                me_inv = parts[1]  # my-name-1.my
                bot.send_message(message.chat.id,"<b>Твой шанс на победу:</b> " + me_sh +"%" + "\n" "<b>Ты пригласил:</b> "+ me_inv, parse_mode="HTML")
        except Exception as e:
            bot.reply_to(message, 'oooops, подожди')
            sleep(5)    
            continue


# Handle '/start' and '/help'
@bot.message_handler(commands=['add_ref'])
def send_add_ref(message):
    msg = bot.reply_to(message, """\
Хочешь принять участие в конкурсе? Тогда пиши /competition
""")
# Handle '/start' and '/help'
@bot.message_handler(commands=['count'])
def send_count(message):
    excpt = True
    while(excpt):
        try:
            uname = "username="+message.from_user.username
            data = uname.encode("ascii")
            response = urllib.request.urlopen("http://treamz.zzz.com.ua/active_members.php",data)
            html = response.read().decode("utf-8") # utf-8 чтобы принять русские буквы
            excpt = False
            if "Нет участников" in html:
                bot.send_message(message.chat.id, "<b>Еще нет участников, которые пригласили больше 2ух друзей</b>", parse_mode="HTML")
            else: 
                #print(html)
                parts = html.rsplit('%%%', 2)  # ['my-name-1.my', 'lovely', 'local']
                res = parts[0]  # my-name-1.my
                print(res)
                bot.send_message(message.chat.id,"<b>Кол-во активных участников:</b> "+res, parse_mode="HTML")
        except Exception as e:
            bot.reply_to(message, 'oooops, подожди') 
            sleep(5)
            continue

# Handle '/start' and '/help'
@bot.message_handler(commands=['top'])
def send_top(message):
    excpt = True
    while(excpt):
        try:
            uname = "username={}".format(message.from_user.username)
            data = uname.encode("ascii")
            response = urllib.request.urlopen("http://treamz.zzz.com.ua/top.php",data)
            html = response.read().decode("utf-8") # utf-8 чтобы принять русские буквы

            if "Нет участников" in html:
                bot.send_message(message.chat.id, "<b>Еще нет участников, которые пригласили больше 2ух друзей</b>", parse_mode="HTML")
            else: 
                #print(html)
                parts = html.rsplit('<!-- zzz', 1)  # ['my-name-1.my', 'lovely', 'local']
                res = parts[0]  # my-name-1.my
                print (res)
                res2 = str(res).rsplit('%%%', 5)
                nfo = ('\n'.join(res2))
                #info = ('\n'.join(parts))
                bot.send_message(message.chat.id, nfo, parse_mode="HTML")
            excpt = False
        except Exception as e:
            bot.reply_to(message, 'oooops, подожди')
            sleep(5)
            continue

# Handle '/start' and '/help'
@bot.message_handler(commands=['competition', 'Competition'])
def send_ans(message):
    excpt = True
    while(excpt):
        try:
            getterchat = bot.get_chat(message.chat.id)
            chmemb = bot.get_chat_member("@rspwn",getterchat.id)
            excpt = False
            #bot.send_message(message.chat.id, message.from_user.username)
            if chmemb.status == "member" or chmemb.status == "creator":
                print(chmemb.user.username)
                usern = str(chmemb.user.username)
                if "None" in usern:
                    bot.send_message(message.chat.id, "Для начала установи @username в настройках телеграмм. Это надо для того, чтобы ты смог получить приз в случае победы!")
                else:
                    uname = "username={}".format(message.from_user.username)
                
                    data = uname.encode("ascii")
                   
                    response = urllib.request.urlopen("http://treamz.zzz.com.ua/reg.php",data)
                    html = response.read().decode("utf-8") # utf-8 чтобы принять русские буквы
                    #print (html)
                    if str(message.from_user.username) in html:
                        bot.send_message(message.chat.id, "Ты уже принимаешь участие!")
    
                    else:
                        if "New record created successfully" in html:
                            bot.send_message(message.chat.id, "Ты подписался, молодец!")
                            chat_id = message.chat.id
                            name = chmemb.user.username
                            user = User(name)
                            user_dict[chat_id] = user
                            msg = bot.reply_to(message, 'Если тебя кто-то пригласил напиши его @username (без собачки) или "0"?')
                            bot.register_next_step_handler(msg, process_ref_step)
                        else:
                            bot.reply_to(message, 'Какая-то ошибка, попробуй заново /start')
                
                #admin_group = "-275571794"
                #message_accept = 'ID:' + (chmemb.user.id) + 'Username:' (chmemb.user.username)
                #bot.send_message(admin_group, "<b>ID:</b>"+ str(chmemb.user.id) + '\n' "<b>UN:</b>@" + str(chmemb.user.username) + '\n' "<b>Имя:</b>" + str(chmemb.user.first_name)+ '\n' "<b>Фамилия:</b>" + str(chmemb.user.last_name), parse_mode="HTML")
            elif chmemb.status == "administrator":
                bot.send_message(message.chat.id, "Админы не могут принимать участие!")
            else:
                bot.send_message(message.chat.id, "Для начала вступи в ряды @RSPWN")
                bot.send_message(message.chat.id, "https://t.me/rspwn")
        except Exception as e:
            bot.reply_to(message, 'oooops, подожди')
            sleep(5)
            continue

def process_ref_step(message):
    excpt = True
    while(excpt):
        try:
            chat_id = message.chat.id
            ref = message.text
            user = user_dict[chat_id]
            excpt = False
            if "/" not in ref:
                if (ref != '0'):
                    user.ref = ref
                    uname = "username={}".format(user.ref)
                    data = uname.encode("ascii")
                    response = urllib.request.urlopen("http://treamz.zzz.com.ua/add_ref.php",data)
                    html = response.read().decode("utf-8") # utf-8 чтобы принять русские буквы\
                #print (html)
                    if "New record created successfully" in html:
                        print ("REF DOBAVLEN")
                        bot.send_message(chat_id, '<b>'+user.name+'</b> ' + ', ты принял участие ' + '\n Твой реферал:' + user.ref, parse_mode="HTML")
                        bot.send_message(-275571794, '<b>'+user.name+'</b>'+ ', принял участие \n' + '<b>Invited by</b> :' + user.ref, parse_mode="HTML")
                    else:
                        print ("REF NE DOBAVLEN")
                        #bot.send_message(chat_id, "Ошибочка вышла", parse_mode="HTML")
                        #bot.send_message(chat_id, '<b>'+user.name+'</b> ' + ', ты все равно принял участие ' + '\n У тебя нет реферала', parse_mode="HTML")
                        #bot.send_message(-275571794, '<b>'+user.name+'</b>'+ ', принял участие \n' + '<b>Invited by</b>: None', parse_mode="HTML")
                        msg = bot.reply_to(message, 'oooops, повторите...')
                        bot.register_next_step_handler(msg, process_ref_step)
    
                else: 
                    bot.send_message(chat_id, '<b>'+user.name+'</b> ' + ', ты принял участие ' + '\n У тебя нет реферала', parse_mode="HTML")
                    bot.send_message(-275571794, '<b>'+user.name+'</b>'+ ', принял участие \n' + '<b>Invited by</b>: None', parse_mode="HTML")
            elif ref == "/competition":
                msg = bot.reply_to(message, 'oooops, повторите...')
                bot.register_next_step_handler(msg, process_ref_step)
    
        
        except Exception as e:
            bot.reply_to(message, 'oooops, подожди')
            sleep(5)
            continue


# Enable saving next step handlers to file "./.handlers-saves/step.save".
# Delay=2 means that after any change in next step handlers (e.g. calling register_next_step_handler())
# saving will hapen after delay 2 seconds.
bot.enable_save_next_step_handlers(delay=2)

# Load next_step_handlers from save file (default "./.handlers-saves/step.save")
# WARNING It will work only if enable_save_next_step_handlers was called!
bot.load_next_step_handlers()


#bot.polling(none_stop=True)
bot.polling(none_stop=True)
