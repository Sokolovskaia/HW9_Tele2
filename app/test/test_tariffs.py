from app.tariffs import TariffManager, Tariff


def test_actual():
    tm = TariffManager()
    my_online_1 = Tariff('Мой Онлайн 1', price=0, price_period='month', gb=0, gb_unlim=None, minutes=0,
                         minutes_unlim_tele2=True, sms=0, hit=False, archived=False)
    my_online_2 = Tariff('Мой Онлайн 2', price=0, price_period='month', gb=0, gb_unlim=None, minutes=0,
                         minutes_unlim_tele2=True, sms=0, hit=False, archived=False)
    my_online_3 = Tariff('Мой Онлайн 3', price=0, price_period='month', gb=0, gb_unlim=None, minutes=0,
                         minutes_unlim_tele2=True, sms=0, hit=False, archived=True)
    my_online_4 = Tariff('Мой Онлайн 4', price=0, price_period='month', gb=0, gb_unlim=None, minutes=0,
                         minutes_unlim_tele2=True, sms=0, hit=False, archived=True)
    tm.add(my_online_1)
    tm.add(my_online_2)
    tm.add(my_online_3)
    tm.add(my_online_4)
    actual = tm.actual()
    assert [my_online_1, my_online_2] == actual


def test_archived():
    tm = TariffManager()
    my_online_1 = Tariff('Мой Онлайн 1', price=0, price_period='month', gb=0, gb_unlim=None, minutes=0,
                         minutes_unlim_tele2=True, sms=0, hit=False, archived=False)
    my_online_2 = Tariff('Мой Онлайн 2', price=0, price_period='month', gb=0, gb_unlim=None, minutes=0,
                         minutes_unlim_tele2=True, sms=0, hit=False, archived=False)
    my_online_3 = Tariff('Мой Онлайн 3', price=0, price_period='month', gb=0, gb_unlim=None, minutes=0,
                         minutes_unlim_tele2=True, sms=0, hit=False, archived=True)
    my_online_4 = Tariff('Мой Онлайн 4', price=0, price_period='month', gb=0, gb_unlim=None, minutes=0,
                         minutes_unlim_tele2=True, sms=0, hit=False, archived=True)
    tm.add(my_online_1)
    tm.add(my_online_2)
    tm.add(my_online_3)
    tm.add(my_online_4)
    archived = tm.archived()
    assert [my_online_3, my_online_4] == archived
