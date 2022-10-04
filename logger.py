from datetime import datetime as d
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, ConversationHandler

# def changes_prog(num1, num2, oper, result, regim): #запись производимых операций калькулятором
#     time_changes = d.now().strftime('%D %H:%M')
#     f_changes = 'log.csv'
#     f = open(f_changes, 'a', encoding="utf-8")
#     f.write(f'{regim} режим:{num1} {oper} {num2} = {result} =>({time_changes})\n')
#     f.close()


def log(update, context, send_message):
    time_changes = d.now().strftime('%D %H:%M')
    file = open('db.csv', 'a', encoding="utf-8")
    file.write(f'{update.effective_user.first_name}, {update.effective_chat.id}, {update.message.text}, {time_changes}, {send_message}\n')
    file.close()