from database import DB
from datetime import date

class ad:

    def __init__(self, id_ad, name_ad, info_ad, price, user_id, date=date.today(), is_active = 1, buyer = 0):
        self.id_ad = id_ad
        self.name_ad = name_ad
        self.info_ad = info_ad
        self.price = price
        self.date = date
        self.is_active = is_active
        self.buyer = buyer
        self.user_id = user_id

        self.values = (
            self.id_ad, self.name_ad, self.info_ad, self.price, self.date, self.is_active, self.buyer , self.user_id
        )

    def add_ad(self):
        with DB() as db:
            db.execute(
                '''
                    INSERT INTO ads (id_ad ,name_ad, info_ad, price, date, is_active, buyer, user_id)
                    VALUES ( ?, ?, ?, ?, ?, ?, ?, ?)
                ''', self.values
            )

            return self

    @staticmethod
    def all():
        with DB() as db:
            rows = db.execute('SELECT * FROM ads').fetchall()
            return [ad(*row) for row in rows]