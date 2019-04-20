from app.tariffs import TariffManager, Tariff


class TestTariffManager:

    def test_add(self):
        tm = TariffManager()
        expected = [{'name': 'Мой Онлайн', 'price': 0, 'price_period': 'month', 'gb': 0, 'gb_unlim': None, 'minutes': 0,
                     'minutes_unlim_tele2': True, 'sms': 0, 'hit': False, 'archived': False}]
        my_online = Tariff(name='Мой Онлайн', price=0, price_period='month', gb=0, gb_unlim=None, minutes=0,
                           minutes_unlim_tele2=True, sms=0, hit=False, archived=False)
        actual = tm.add(my_online)
        assert expected == actual

