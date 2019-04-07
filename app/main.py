import waitress
from flask import Flask, render_template, request, url_for, redirect

from app.tariffs import TariffManager, Tariff

import os


def start():
    app = Flask(__name__)

    manager = TariffManager()

    my_online = Tariff('Мой Онлайн', price=290, gb=15, gb_unlim=['vk', 'fb'], minutes=400, hit=True)
    unlim = Tariff('Безлимит', price=350, gb=-1, minutes=500, sms=50)
    classic = Tariff('Классический', minutes_unlim_tele2=False)
    boundless_black = Tariff('Беспредельно черный', price=310, gb=30, gb_unlim=None, minutes=200,
                             minutes_unlim_tele2=False, sms=200, archived=True)
    city = Tariff('СИТИ', minutes_unlim_tele2=False, archived=True)
    my_talk = Tariff('Мой разговор', price=190, gb=3, minutes=250)
    my_tele2 = Tariff('Мой Tele2', price=7, price_period='день', gb=6)
    my_start = Tariff('Мой старт', price=99, gb=2, minutes=100, minutes_unlim_tele2=False, archived=True)

    # my_online = Tariff('Мой Онлайн', price=0, price_period='month', gb=0, gb_unlim=None, minutes=0, minutes_unlim_tele2=True, sms=0, hit=False, archived=False)

    manager.add(my_online)
    manager.add(unlim)
    manager.add(classic)
    manager.add(boundless_black)
    manager.add(city)
    manager.add(my_talk)
    manager.add(my_tele2)
    manager.add(my_start)

    @app.route('/')
    def index():
        actual = manager.actual()
        return render_template('index.html', actual=actual)

    @app.route('/archive')
    def archive():
        archived = manager.archived()
        return render_template('archive.html', archived=archived)

    if os.getenv('APP_ENV') == 'PROD' and os.getenv('PORT'):
        waitress.serve(app, port=os.getenv('PORT'))
    else:
        app.run(port=9873, debug=True)


if __name__ == '__main__':
    start()
