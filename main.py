from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, ConversationHandler
from config import TOKEN
from operation import oper, oper_res


bot = Bot(token=TOKEN)
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

def start(update, context):
    arg = context.args
    if not arg:
        context.bot.send_message(update.effective_chat.id, """Приветствую тебя в игре. На столе лежит 221 конфета, ты можешь взять не больше 28 конфет. Для перехода к новой игре нажим команду: /new""")

def info(update, context):
    context.bot.send_message(update.effective_chat.id,
                             """Доступны следующие команды:
                             /start - приветствие, правила игры,
                             /info - информация (команды),
                             /new - новая игра""")

def new(update, context):
    context.bot.send_message(update.effective_chat.id, 'Игра началась! Введите кол-во конфет: ')
    context.user_data['ost'] = 221

def give_word(update,context):
    word = update.message.text
    res = oper(word, context.user_data.get('ost'))
    if res[1] == 0:
        context.bot.send_message(update.effective_chat.id, res[0])
    else:
        context.bot.send_message(update.effective_chat.id, res[0])
        res_list = oper_res(word, res[1])
        context.bot.send_message(update.effective_chat.id, res_list[0])
        context.user_data['ost'] = res_list[1]


start_handler = CommandHandler('start', start)
info_handler = CommandHandler('info', info)
new_handler = CommandHandler('new', new)
message_handler = MessageHandler(Filters.text, give_word)


dispatcher.add_handler(new_handler)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(info_handler)
dispatcher.add_handler(message_handler)

print('server started')
updater.start_polling()
updater.idle()      
