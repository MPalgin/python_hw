import random

from telebot import types, TeleBot, custom_filters
from telebot.storage import StateMemoryStorage
from telebot.handler_backends import State, StatesGroup
from common_sql_funcs import (table_scema_creator, get_common_words, add_user_id, delete_word_from_user_db,
                              add_new_user_word)


print('Start telegram bot...')

state_storage = StateMemoryStorage()
token_bot = '8161961562:AAHJ6FSk4sawdmeEKqorfpD2TXl-FySBimQ'
bot = TeleBot(token_bot, state_storage=state_storage)
session = table_scema_creator()

known_users = []
userStep = {}
buttons = []


def show_hint(*lines):
    return '\n'.join(lines)


def show_target(data):
    return f"{data['target_word']} -> {data['translate_word']}"


class Command:
    ADD_WORD = 'Добавить слово ➕'
    DELETE_WORD = 'Удалить слово🔙'
    NEXT = 'Дальше ⏭'


class MyStates(StatesGroup):
    target_word = State()
    translate_word = State()
    another_words = State()


def get_user_step(uid):
    if uid in userStep:
        return userStep[uid]
    else:
        known_users.append(uid)
        userStep[uid] = 0
        print("New user detected, who hasn't used \"/start\" yet")
        return 0


@bot.message_handler(commands=['cards', 'start'])
def create_cards(message):
    cid = message.chat.id
    if cid not in known_users:
        known_users.append(cid)
        add_user_id(session, cid)
        userStep[cid] = 0
        bot.send_message(cid, "Привет 👋 Давай попрактикуемся в английском языке. Тренировки можешь проходить "
                              "в удобном для себя темпе. У тебя есть возможность использовать тренажёр, "
                              "как конструктор, и собирать свою собственную базу для обучения. Для этого воспрользуйся "
                              "инструментами:\n добавить слово ➕\n удалить слово 🔙\n Ну что, начнём ⬇️")
    markup = types.ReplyKeyboardMarkup(row_width=2)

    global buttons
    buttons = []
    common_words = get_common_words(session, 'common', cid)
    random_words = get_common_words(session, 'random', cid)
    find_target_word_id = random.randint(1, len(common_words) - 1)
    target_word = str(common_words[find_target_word_id][2])
    translate = str(common_words[find_target_word_id][1])
    target_word_btn = types.KeyboardButton(target_word)
    buttons.append(target_word_btn)
    others = [str(random_words[random.randint(1, len(common_words))][0]),
              str(random_words[random.randint(1, len(common_words))][0]),
              str(random_words[random.randint(1, len(common_words))][0])]
    other_words_btns = [types.KeyboardButton(word) for word in others]
    buttons.extend(other_words_btns)
    random.shuffle(buttons)
    next_btn = types.KeyboardButton(Command.NEXT)
    add_word_btn = types.KeyboardButton(Command.ADD_WORD)
    delete_word_btn = types.KeyboardButton(Command.DELETE_WORD)
    buttons.extend([next_btn, add_word_btn, delete_word_btn])

    markup.add(*buttons)

    greeting = f"Выбери перевод слова:\n🇷🇺 {translate}"
    bot.send_message(message.chat.id, greeting, reply_markup=markup)
    bot.set_state(message.from_user.id, MyStates.target_word, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['target_word'] = target_word
        data['translate_word'] = translate
        data['other_words'] = others


@bot.message_handler(func=lambda message: message.text == Command.NEXT)
def next_cards(message):
    create_cards(message)


@bot.message_handler(func=lambda message: message.text == Command.DELETE_WORD)
def delete_word(message):
    send = bot.send_message(message.chat.id, 'Введите слово, которое нужно удалить')
    bot.register_next_step_handler(send, delete_word_request_data)


@bot.message_handler(func=lambda message: message.text == Command.ADD_WORD)
def add_word(message):
    cid = message.chat.id
    userStep[cid] = 1
    send = bot.send_message(message.chat.id, 'Введите слово и перевод слова, которые нужно добавить')
    bot.register_next_step_handler(send, add_word_request_data)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def message_reply(message):
    text = message.text
    markup = types.ReplyKeyboardMarkup(row_width=2)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        target_word = data['target_word']
        if text == target_word:
            hint = show_target(data)
            hint_text = ["Отлично!❤", hint]
            hint = show_hint(*hint_text)
        else:
            for btn in buttons:
                if btn.text == text:
                    btn.text = text + '❌'
                    break
            hint = show_hint("Допущена ошибка!",
                             f"Попробуй ещё раз вспомнить слово 🇷🇺{data['translate_word']}")
    markup.add(*buttons)
    bot.send_message(message.chat.id, hint, reply_markup=markup)


@bot.message_handler(content_types=['text'])
def delete_word_request_data(message):
    global text
    text = message.text
    delete_result = delete_word_from_user_db(session, str(message.text), message.chat.id)
    if delete_result:
        bot.reply_to(message, f'{message.text} удалено')
    else:
        bot.reply_to(message, f'{message.text} не найдено')


@bot.message_handler(content_types=['text'])
def add_word_request_data(message):
    global text
    text = message.text
    add_results = add_new_user_word(session, {'new_word': str(message.text.split()[0]),
                                              'translate': str(message.text.split()[1])}, message.chat.id)
    if add_results:
        bot.reply_to(message,f'{message.text.split()[0]} добавлено')
    else:
        bot.reply_to(message,f'{message.text.split()[0]} уже есть в словаре')


bot.add_custom_filter(custom_filters.StateFilter(bot))

bot.infinity_polling(skip_pending=True)
