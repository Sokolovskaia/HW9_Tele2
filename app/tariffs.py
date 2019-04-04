class Tariff:
    def __init__(
            self,
            name,
            price=0,  # 0 без абонентской платы
            price_period='месяц',
            gb=0,  # -1 - безлимит
            gb_unlim=None,
            minutes=0,
            minutes_unlim_tele2=True,
            sms=0,
            hit=False,
            archived=False
    ):
        self.name = name
        self.price = price
        self.price_period = price_period
        self.gb = gb
        self.gb_unlim = gb_unlim
        self.minutes = minutes
        self.minutes_unlim_tele2 = minutes_unlim_tele2
        self.sms = sms
        self.hit = hit
        self.archived = archived


class TariffManager:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def actual(self):
        return list(filter(lambda tariff: not tariff.archived, self.items))

    def archived(self):
        return list(filter(lambda tariff: tariff.archived, self.items))
