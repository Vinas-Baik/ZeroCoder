
import telebot
from datetime import datetime
import threading


# Инициализация бота
API_TOKEN = '7155478435:AAFpuiJotd36swgw72ZRDz1Pcl3iFfGBxJc'


# Инициализация бота
bot = telebot.TeleBot(API_TOKEN)

# Заготовка для хранения данных пользователей
users_data = {}

# Функция для отправки уроков и заданий
def send_lessons_and_tasks(chat_id):
    lessons = [
        "Урок 1: Введение в Python",
        "Урок 2: Переменные и типы данных",
        "Урок 3: Условные операторы и циклы",
        # Добавьте больше уроков по мере необходимости
    ]
    for lesson in lessons:
        bot.send_message(chat_id, lesson)
        # Отправить задание после урока
        bot.send_message(chat_id, f"Задание для {lesson}")

# Функция для предоставления помощи куратора
def curator_help(chat_id):
    bot.send_message(chat_id, "Свяжитесь с куратором через @Vinas_0175")

# Функция для отправки видеоуроков с Youtube
def send_video_lessons(chat_id):
    videos = [
        "https://www.youtube.com/watch?v=rfscVS0vtbw",  # Пример видеоурока
        # Добавьте больше ссылок на видеоуроки
    ]
    for video in videos:
        bot.send_message(chat_id, video)

# Функция для отправки статей из открытых источников
def send_articles(chat_id):
    articles = [
        "https://realpython.com/",  # Пример статьи
        # Добавьте больше ссылок на статьи
    ]
    for article in articles:
        bot.send_message(chat_id, article)

# Функция для записи на участие в хакатонах и конкурсах
def register_for_hackathons(chat_id):
    bot.send_message(chat_id, "Для регистрации на хакатоны и конкурсы отправьте ваше имя и email.")

# Обработчик команд
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! \n"
                          "Я бот для изучения программирования на Python. \n"
                          "Выберите команду: /lessons, /help, /videos, /articles, /register")

@bot.message_handler(commands=['lessons'])
def handle_lessons(message):
    chat_id = message.chat.id
    send_lessons_and_tasks(chat_id)

@bot.message_handler(commands=['help'])
def handle_help(message):
    chat_id = message.chat.id
    curator_help(chat_id)

@bot.message_handler(commands=['videos'])
def handle_videos(message):
    chat_id = message.chat.id
    send_video_lessons(chat_id)

@bot.message_handler(commands=['articles'])
def handle_articles(message):
    chat_id = message.chat.id
    send_articles(chat_id)

@bot.message_handler(commands=['register'])
def handle_register(message):
    chat_id = message.chat.id
    register_for_hackathons(chat_id)

# Обработчик всех сообщений, которые не являются командами
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Привет! Введите /start, чтобы начать.")


# Функция для запуска бота в отдельном потоке
def start_bot():
    bot.polling()

# Запуск бота в отдельном потоке
if __name__ == "__main__":

    bot_thread = threading.Thread(target=start_bot)
    bot_thread.start()