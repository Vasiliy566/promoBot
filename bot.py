import telebot

from functools import wraps


class bot:
    """docstring"""

    def __init__(self):

        self.start_text = """👋Всем привет, меня зовут Виктор и в этом боте я буду с вами делиться информацией, как можно заработать на IEO на самой популярной бирже в СНГ. Я расскажу вам тактику, на которой я лично зарабатываю уже несколько лет. Благодаря этому вы сможете увеличивать свой капитал в разы.
        
        12 ноября я всем советовал учавствовать в airdrop на бирже, не вкладывая своих средств, что по итогу? Все мои подписчики не вложив ни рубля заработали более 60$ за 2 минуты в битках и еще почти 6000$ положили под проценты.
        
        Моя тактика сработала. Все подтверждения будут дальше в сообщениях.
        
        ✅Как вы сможете заработать сейчас? Способ очень простой. Участвовать в IEO на бирже➡ https://yobit.net/?bonus=XcciZ
        
        ❗Пожалуйста, регистрируйтесь по моей реф ссылке, от этого зависит, буду ли я с вами делиться новой информацией или нет. Если вы уже регистрировались на сайте ранее, то советую заново зарегистрироваться.
        
        🔥Способ заработка очень простой: 21 ноября в 16:00 по Московскому времени стартует IEO . Тоесть будет продажа токенов, продав которые по определенной тактике, можно заработать более чем в 10 раз. Есть несколько тактик, которые я использую при продаже токенов после проведения IEO. Ими я готов с вами поделиться.
        
        Да и дальше в рассылке я покажу вам примеры, как я на таких IEO я смог заработать ранее, и какую тактику использовал. Будет полезно.
        
        ✅Для этого вам нужно выполнить 2 простых действия.
        
        1) Зарегистрироваться на бирже по моей реф ссылке yobit.net/?bonus=XcciZ
        
        2) Прислать сюда в ответ фото, как вы только что зарегистрировались.
        
        Все. После того, как станете моим рефералом, вам в боте придет сообщение, где я покажу вам, как я зарабатывал ранее на IEO на данной бирже, и когда я выходил с проектов и почему.
        При возникновении вопросов вы можете писать в мой чат t.me/yobitairdrop """
        self.second_message = """💰Как будем зарабатывать на IEO? Как учавствовать в IEO?
        
        21 ноября в 16 00 по Москве стартует IEO на бирже https://yobit.net/?bonus=XcciZ в котором мы будем участвовать. У меня есть несколько тактик, на которых я заработал х4, где-то х10, где-то даже по 1 BTC, где-то был и минус, но по итогу я в хорошем плюсе. С вами я готов поделиться тактикой, если вы будете моим рефералом.
        
        🔥IEO на данной бирже привлекательны тем, что они растут всегда и дают иксы, поэтому IEO на данной бирже обычно закрывается в течение пару минут, и как с BNB от бинанса, всегда происходит рост монет. Смотрите по истории предыдущих IEO, поэтому важно участвовать на старте, в 16 00 и заранее подготовить деньги.
        
        💵💵💵Схема заработка:
        Сегодня в твиттере биржи я увидел вот такой пост https://vk.cc/a1YRbF , это значит, что IEO/ICO у биржи будет с Investbox. Что значит InvestBox? Это когда мы кладем деньги под процент и увеличиваем наш капитал, выполняя определенные действия, например, имея в распоряжении биржевой токен YO. Это не пирамида. У вас просто так не будет увеличиваться капитал, нужно будет сделать определенные действия каждый день, нужно лишь грамотно их делать. Много разных тактик есть, об этом я еще отдельно напишу.
        
        По твиттеру понятно, что будет инвестбокс, а это значит, дикий ажиотаж на IEO и рост цены сразу же при листинге, так как все, кто не успеют войти в IEO, будут покупать токен при листинге, чтобы в нем участвовать. Тем самым биржа мотивирует вкладываться в свои IEO. ИнвестБокс не резиновый и заканчивается рано или поздно, им проект мотивирует своих вкладчиков. Если он есть-ждите рост.
        
        ❗Так что нам нужно покупать токен в 16 00 по Москве или в первые минуты при листинге, дальше будет свечка верх и рост. Если будет инвестбокс с такой формулой ( 1+Yo/20), значит что для держателей YO токенов будут бонусы, они у меня есть, я еще их давно получил бесплатно и после докупал. В цене токен растет постоянно, так что точно не потеряете ничего, купив его для большего бонуса.
        
        По этой формуле, судя по опыту других IEO, инвест бокс будет приблизительно 3 месяца, это значит нам нужно будет выходить с него примерно через 1-2 месяца максимум, но не жадничать. Будут, возможно, ложные пробои, чтобы хомяков подстричь, главное на это не вестись.
        
        💎В любом случае вы будете в плюсе, как по прошлому моему совету. Вам спасибо, мне как рефеводу было приятно это. В этот раз будет плюс еще больше, главное не жадничать и действовать согласно схеме выше.
        
        IEO закрывается очень быстро, поэтому ставим будильник на 15:50 21 ноября, готовим битки и YO токены, заходим в этот чат и ждем роста.
        
        👑P.S Рост будет, вот уведите, мой третий совет по следующему IEO будет уже платный, стоимость 5000 рублей, писать в директ. Рефки это хорошо, но на них много не заработаешь. Раз в 5 IEO я буду давать бесплатно советы по вкладыванию и тактике.
        
        Вы уже благодаря мне заработали один раз, сейчас второй раз, вы увидите мой опыт и, надеюсь, придете ко мне на обучение или купите мои прогнозы, только когда убедитесь в том, что я помогаю увеличивать капитал.
        
        Еще раз напомню свою реф ссылку: https://yobit.net/?bonus=XcciZ
        Если остались вопросы, вы можете его спросить в нашем телеграм чате, вам там помогут, если для вас слова выше новые и непонятные: t.me/yobitairdrop
        
        На фото пример моего заработка на инвестбоксе, даже на BTC"""

        self.foto2 = open('./message2.jpg', 'rb')

        self.bot = telebot.TeleBot('*******************')
        self.admins=[359297087, 60201964]
        self.commands = {  # command description used in the "help" command
            'start'       : 'Get used to the bot',
            'help'        : 'Gives you information about the available commands'
        }
        self.log = open('log.txt', 'w')

    def send_message(self, id, message):
        bot.send_message(id , message)

    def send_message_admins(self, message):
        for id in self.admins:
            bot.send_message(id , message)


    def all_users(self,):
        users = []

        f = open('all_users', 'r')
        for user in f:
            users.append(str(user) )
        f.close()
        return users

    #@bot.message_handler(commands=['mailing'])
    def mailing(self,message):
        if (message.chat.id in self.admins):
            bot.send_message(message.chat.id, '!!!your next message will send to all bot users, do not forget to use picture!!!')
            bot.register_next_step_handler(message, self.send_content)

        else:
            pass
    def send_content(self,message):
        try:
            fileID = message.photo[-1].file_id
            file_info = bot.get_file(fileID)
            downloaded_file = bot.download_file(file_info.file_path)
            with open("image.jpg", 'wb') as new_file:
                new_file.write(downloaded_file)
            foto = open('./image.jpg', 'rb')
            f = open('all_id', 'r')

            for id in f:
                bot.send_photo(int(id), foto, message.caption)
        except Exception as e:
            pass
            #send_message(message.chat.id, 'что то пошло не так, рассылка не отправилась')




    #@bot.message_handler(commands=['mailing_text_only'])
    def mailing_text_only(self,message):
        if (message.chat.id in self.admins):
            bot.send_message(message.chat.id, '!!!your net message will send to all bot users!!!')
            bot.register_next_step_handler(message, self.send_text)

        else:
            pass
    def send_text(self,message):
         f = open('all_id', 'r')
         for id in f:
            self.send_message(int(id), str(message.text))


    #@bot.message_handler(commands=['start'])

    def start_message(self,message):

        if not((message.chat.username + '\n') in self.all_users()):

            f = open('all_id', 'a')
            f.write(str(message.chat.id) + '\n')
            f.close()

            f = open('all_users', 'a')
            f.write(str(message.chat.username) + '\n')
            f.close()

            group_name = "organic"
            if len(message.text.split()) > 1:
                group_name = message.text.split()[1]
            #send_message_admins('new user: ' + message.chat.last_name + ' ' + message.chat.first_name + ' group: ' + group_name )
            full_info = []

            f = open('group_stats', 'r')
            for group in f:
                full_info.append(group.split())
            f.close()
            found = False
            for i in range(len(full_info)):
                if full_info[i][0] == group_name:
                    full_info[i][1] = str(int(full_info[i][1]) + 1)
                    found = True
                    break;
            if found:
                f = open('group_stats', 'w')
                for i in range(len(full_info)):
                    f.write(full_info[i][0] + ' ' + full_info[i][1] + ' \n')
            else:
                 f = open('group_stats', 'a')
                 f.write(group_name + ' 1\n')
            f.close()

        self.send_message(message.chat.id, self.start_text)
        bot.register_next_step_handler(message, self.check_photo)
    def check_photo(self,message):
        if message.content_type == 'photo':
            bot.send_message(message.chat.id, self.second_message)
            bot.send_photo(message.chat.id, self.foto2, )
        else:
            bot.send_message(message.chat.id, 'Чтобы продолжить работу с ботом, зарегистрируйтесь по реферальной ссылке и отправьте фото подтверждение регистрации')
            bot.register_next_step_handler(message, self.check_photo)

    #@bot.message_handler(commands=['stats'])
    def start_message(self,message):
        if (message.chat.id in self.admins):
            f = open('group_stats', 'r')
            for group in f:
                bot.send_message(message.chat.id, group)
            f.close
        else:
            pass

    #@bot.message_handler(commands=['stats_users'])
    def start_message(self,message):
        if (message.chat.id in self.admins):
            f = open('all_users', 'r')
            data = ''
            for group in f:
                data += group + '\n'
            bot.send_message(message.chat.id, data)
            f.close
        else:
            pass


    # help page
    #@bot.message_handler(commands=['help'])
    def command_help(self,m):
        cid = m.chat.id
        help_text = "The following commands are available: \n"
        for key in self.commands:  # generate help text out of the commands dictionary defined at the top
            help_text += "/" + key + ": "
            help_text += self.commands[key] + "\n"
        bot.send_message(cid, help_text)  # send the generated help page
