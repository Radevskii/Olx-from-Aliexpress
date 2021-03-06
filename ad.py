from database import DB
from datetime import date



class ad:

    def __init__(self, id_ad, name_ad, info_ad, price, user_id, date=date.today(), is_active = 1, buyer = 0):
        self.id_ad = id_ad
        self.name_ad = name_ad
        self.info_ad = info_ad
        self.price = price
        self.user_id = user_id
        self.date = date
        self.is_active = is_active
        self.buyer = buyer
        self.values = (

        self.id_ad, self.name_ad, self.info_ad, self.price, self.user_id, self.date, self.is_active, self.buyer
        )

        self.editing = (
             self.name_ad, self.info_ad, self.price, self.id_ad
        )

    def add_ad(self):
        with DB() as db:
            db.execute(
                '''
                    INSERT INTO ads (id_ad ,name_ad, info_ad, price, user_id, date, is_active, buyer)
                    VALUES ( ?, ?, ?, ?, ?, ?, ?, ?)
                ''', self.values
            )

            return self

    def edit_ad(self):
        with DB() as db:
            db.execute(
                '''
                    UPDATE ads SET name_ad = ?, info_ad = ?, price = ?
                    WHERE id_ad = ? 
                ''', self.editing
            )
            return self

    @staticmethod
    def find(id):
        with DB() as db:
            row = db.execute(
                'SELECT * FROM ads WHERE id_ad = ?',
                (id,)
            ).fetchone()
            return ad(*row)

    @staticmethod
    def all():
        with DB() as db:
            rows = db.execute('SELECT * FROM ads').fetchall()
            return [ad(*row) for row in rows]

    @staticmethod
    def find_user_name(user_id):
        with DB() as db:
            name = db.execute(
                '''
                SELECT name FROM users 
                WHERE id = ?
                ''',
                (user_id,)).fetchone()
        return name[0]

    @staticmethod
    def find_buyer(buyer):
        with DB() as db:
            user = db.execute(
                '''
                SELECT * FROM users
                WHERE id = ?
                ''', (buyer,)).fetchone()
            return user

    def add_bought_ads(self):
        with DB() as db:
            buyer = (
                self.buyer,
                self.id_ad

            )
            db.execute('''
                        UPDATE ads SET buyer = ?, is_active = 0
                         WHERE id_ad = ?''', buyer)
            return self

    def delete(self):
        with DB() as db:
            db.execute('DELETE FROM ads WHERE id_ad = ?', (self.id_ad, ))


