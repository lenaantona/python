from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, ConversationHandler
from config import TOKEN
import arithmetic_operations as op
import view
import check as ch
import logger as l
global s
s = ''

bot = Bot(token=TOKEN)
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

def start(update, context):
    arg = context.args
    if not arg:
        context.bot.send_message(update.effective_chat.id, """Приветствую в программе калькулятор комплексных и рациональных чисел. Для ознакомления используй команду /info""")
                
def info(update, context):
    l.log(update, context)
    context.bot.send_message(update.effective_chat.id,
                             """Доступны следующие команды:
                             /start - приветствие
                             /info - информация (команды),
                             /regim - выбор режима калькулятора (указывается 1 - комлексные, рациональные - 2)
                             /summ - сумма двух чисел(указывается после команды через пробел)
                             /sub - разница двух чисел(указывается после команды через пробел)
                             /mult - умножение двух чисел (указывается после команды через пробел)
                             /div - деление двух чисел (указывется после команды через пробел)""")      

def regim(update,context):
    res = context.args
    if not res:
        context.bot.send_message(update.effective_chat.id, 'Забыли указать число')
        l.log(update, context, 'Забыли указать число')
    else:
        if type(ch.check_regime(res[0]))==str: #проверка на ввод режима
            context.bot.send_message(update.effective_chat.id, ch.check_regime(res[0]))
            l.log(update, context,ch.check_regime(res[0]))
        else:
            context.user_data['reg'] = int(res[0])
            s_res = view.get_regime(res[0])
            context.bot.send_message(update.effective_chat.id, s_res)
            l.log(update, context, s_res)
        
def operation(update,context,s):
    res = context.args
    if context.user_data.get('reg')== None:
        context.bot.send_message(update.effective_chat.id, 'Не введен режим работы калькулятора. /regim')
        l.log(update, context, 'Не введен режим работы калькулятора. /regim')
    elif len(res)<2:
        context.bot.send_message(update.effective_chat.id, 'Забыли указать число(а)')
        l.log(update, context, 'Забыли указать число(а)')
    else:
        result =ch.check_number(res[0], res[1], context.user_data.get('reg')) #проверка на ввод числа
        print(result)
        if type(result)==str: 
            context.bot.send_message(update.effective_chat.id, result)
            l.log(update, context, result)
        else:
            res_oper = op.oper(result[0], result[1],s)
            context.bot.send_message(update.effective_chat.id, view.view_data(s, result[0], result[1], res_oper))
            l.log(update, context, view.view_data(s, result[0], result[1], res_oper))


def summ(update,context):
    operation(update, context, '+')

def sub(update,context):
    operation(update, context, '-')

def mult(update,context):
    operation(update, context, '*')
   
def div(update,context):
    operation(update, context, '/')

def give_word(update,context):
    word = update.message.text
    print(word)
    context.bot.send_message(update.effective_chat.id, 'Введите команду для работы с калькулятором') 
    l.log(update, context, word)  
         
start_handler = CommandHandler('start', start)
info_handler = CommandHandler('info', info)
regim_handler = CommandHandler('regim', regim)
div_handler = CommandHandler('div', div)
sum_handler = CommandHandler('summ', summ)
sub_handler = CommandHandler('sub', sub)
mult_handler = CommandHandler('mult', mult)
message_handler = MessageHandler(Filters.text, give_word)


dispatcher.add_handler(regim_handler)
dispatcher.add_handler(sum_handler)
dispatcher.add_handler(sub_handler)
dispatcher.add_handler(div_handler)
dispatcher.add_handler(mult_handler)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(info_handler)
dispatcher.add_handler(message_handler)

print('server started')
updater.start_polling()
updater.idle()