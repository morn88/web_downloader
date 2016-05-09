# -*- coding: utf-8 -*-
import requests
import time
import random

def get_question_response():
    db = [
        'Тупые у тебя вопросы блять.',
        'Ну и хуле ты спрашиваешь, залупа конская?',
        'Тебя не учили вежливо вопросы задавать, мразь?',
        'Чо? Хуй в очо лол.',
        'Знаю ответ, но тебе не скажу. Потому что ты под хвост долбишься.',
        '+15',
        'А нахуй тебе не пойти, с такими вопросами?',
        'Ответил тебе за щеку.',
        'У меня во дворе за такие вопросы убивают.',
        'Это не важно.',
        'Тебя ебёт?',
        'У нас на районе за такие вопросы пиздят.',
        'Пиздец ты тупой.',
        'У мамки своей спроси',
        'А нахуй тебе не пойти, с такими вопросами?',
        'Ты бы и у собаки спросил.',
        'Да ты блять нихуя не знаешь, необучаемый.',
        'Вали в свою парашу, быдло',
        'Не стоит вскрывать эту тему...',
        'Не понял, поясни.',
        'Только ебанутые задают такие вопросы.',
        'Да.',
        'Нет.',
        'Не знаю.',
        'По делу есть что спросить?'
    ]

    return random.choice(db)


def check_thread(board, thread):
    url = 'https://2ch.hk/' + board + '/res/' + str(thread) + '.json'

    r = requests.get(url)

    posts = r.json()['threads'][0]

    return posts['posts']


def answer(board, thread, post):
    url = 'https://2ch.hk/makaba/posting.fcgi'

    message = '>>' + str(post) + '\n' + get_question_response()

    data = {
            'json': (None, '1'),
            'task': (None, 'post'),
            'board': (None, board),
            'thread': (None, thread),
            'comment': (None, message),
            'email': (None, ''),
            'name': (None, ''),
            'subject': (None, ''),
        }

    r = requests.post(url, files=data)
    response = r.json()

    if response['Error']:
        print 'error: ' + response['Reason']
        return None
    else:
        print 'everything went well'
        return response['Num']


def go():
    board = 'b'
    thread = '125945891'

    sleep = 16
    limit = 500
    tries = 0

    processed_posts = []

    while tries < limit:
        tries += 1

        print u'Заход номер ' + str(tries)

        posts = check_thread(board, thread)

        for post in posts:
            if post['comment'].find('?') != -1 and post['num'] not in processed_posts:
                num = answer(board, thread, post['num'])
                if num:
                    processed_posts.append(num)
                processed_posts.append(post['num'])
                break

        time.sleep(sleep)

go()