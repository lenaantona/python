from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update, Bot
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)
import operations
# from config import TOKEN
import ui
import exportdb
import importdb
import logging

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)


# bot = Bot(token=TOKEN)
# updater = Updater(token=TOKEN)
# dispatcher = updater.dispatcher

OPER, INPUT_RECORD, SEARCH_RECORD, DELETE_RECORD, EDITING_RECORD = range(5)

def start(update, _):
    reply_keyboard = [['внесение записи', 'поиск записи', 'удаление записи', 'редактирование', 'просмотр базы', 'импорт', 'экспорт']]
    # Создаем простую клавиатуру для ответа
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    # Начинаем разговор с вопроса
    update.message.reply_text(
        'Доступны следующие функции '
        'Команда /cancel, чтобы прекратить разговор.\n\n'
        'Ты можешь выбрать, что сделать?',
        reply_markup=markup_key,)
    return OPER

def oper(update, _):
    operat = update.message.text
    user = update.message.from_user
    if operat == 'внесение записи':
        update.message.reply_text(
       'Запиши какую ты запись хочешь добавить в формате:\n <Имя>,<Фамилия>,<Основной телефон>,<Дополнительный телефон>,<Описание')
        return INPUT_RECORD
    elif operat == 'поиск записи':
        update.message.reply_text('что будем искать?')
        return SEARCH_RECORD
    elif operat == 'удаление записи':
        resive_data = operations.db_parse()
        update.message.reply_text(ui.view(resive_data))
        update.message.reply_text('введи id который удаляем')
        return DELETE_RECORD
    elif operat == 'редактирование':
        resive_data = operations.db_parse()
        update.message.reply_text(ui.view(resive_data))
        update.message.reply_text('введи id записи, которую редактируете и через "," новую запись')
        return EDITING_RECORD
    elif operat == 'просмотр базы':
        resive_data = operations.db_parse()
        update.message.reply_text(ui.view(resive_data))
        logger.info("Пользователь %s просмотрел базу.", user.first_name)
        start(update, _)
    elif operat == 'импорт':
        try:
            filename_json = "db.json"
            filename_csv = "db.csv"
            importdb.db_import(filename_json, filename_csv)
            update.message.reply_text('Импорт успешно выполнен')
            logger.info("Пользователь %s произвел импорт.", user.first_name)
        except Exception:
            update.message.reply_text('Что-то пошло не так')
            logger.info("Пользователь %s не смог произвести импорт.", user.first_name)
        start(update, _)
    elif operat == 'экспорт':
        exportdb.db_export("db.csv","db.json")
        update.message.reply_text('Экспорт успешно выполнен, файл db.json')
        logger.info("Пользователь %s произвел экспорт.", user.first_name)
        start(update, _)

def input_record(update, _): #ввод записи
    user = update.message.from_user
    user_data = update.message.text.split(',')
    if len(user_data) == 5:
        operations.db_input(user_data)
        update.message.reply_text('Запись внесена')
        logger.info("Пользователь %s внес запись %s", user.first_name, update.message.text)
    else:
        update.message.reply_text('Указаны не все парметры')
        logger.info("Пользователь %s не верно внес запись %s", user.first_name, update.message.text)
    return start(update, _)

def search_record(update, _): # поиск записи
    user = update.message.from_user
    user_data = update.message.text
    resive_data = operations.db_search(user_data)
    update.message.reply_text(ui.view(resive_data))
    logger.info("Пользователь %s искал запись %s", user.first_name, user_data)
    return start(update, _) 

def delete_record(update, _): #удление
    user = update.message.from_user
    user_data = update.message.text
    resive_data2 = operations.db_item_del(user_data)
    print(resive_data2)
    if resive_data2 != []:
        update.message.reply_text('Запись удалена')
        logger.info("Пользователь %s удалил запись %s", user.first_name, ','.join(resive_data2))
    else:
        update.message.reply_text('Запись c таким id не найдена')
        logger.info("Пользователь %s ввел не верный id %s", user.first_name, user_data)
    return start(update, _)

def editing_record(update, _): #редактирование
    user = update.message.from_user
    user_data1 = update.message.text
    user_data2 = user_data1.split(',')
    user_data = user_data2[0]
    user_data2 = user_data2[1:]
    resive_data2 = operations.db_edit(user_data,user_data2)
    if len(user_data2) == 6 and resive_data2 != []:
        update.message.reply_text('Запись отредактирована')
        logger.info("Пользователь %s отредактировал запись на %s", user.first_name, user_data1)
    else: 
        update.message.reply_text('Некорректна внесена запись, либо неверно указан id')
        logger.info("Пользователь %s некорректно ввел запись %s", user.first_name, user_data1)
    return start(update, _)

def cancel(update, _):
    # определяем пользователя
    user = update.message.from_user
    # # Пишем в журнал о том, что пользователь не разговорчивый
    logger.info("Пользователь %s отменил разговор.", user.first_name)
    # Отвечаем на отказ поговорить
    update.message.reply_text(
        'До новых встреч', 
        reply_markup=ReplyKeyboardRemove()
    )
    # Заканчиваем разговор.
    return ConversationHandler.END    

if __name__ == '__main__':
    # Создаем Updater и передаем ему токен вашего бота.
    updater = Updater("TOKEN")
    # получаем диспетчера для регистрации обработчиков
    dispatcher = updater.dispatcher    

    conv_handler = ConversationHandler( # здесь строится логика разговора
        # точка входа в разговор
        entry_points=[CommandHandler('start', start)],
        # этапы разговора, каждый со своим списком обработчиков сообщений
        states={
            OPER: [MessageHandler(Filters.regex('^(внесение записи|поиск записи|удаление записи|редактирование|просмотр базы|импорт|экспорт)$'), oper)],
            INPUT_RECORD: [MessageHandler(Filters.text & ~Filters.command, input_record)],
            SEARCH_RECORD: [MessageHandler(Filters.text & ~Filters.command, search_record)],
            DELETE_RECORD: [MessageHandler(Filters.text & ~Filters.command, delete_record)],
            EDITING_RECORD: [MessageHandler(Filters.text & ~Filters.command, editing_record)], 
            },
        # точка выхода из разговора
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    # Добавляем обработчик разговоров `conv_handler`
    dispatcher.add_handler(conv_handler)

    # Запуск бота
    print('server started')
    updater.start_polling()
    updater.idle()