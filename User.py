from database import DB
import hashlib


class user:
    def __init__(self, id, name, email, password, phone_number, address):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.phone_number = phone_number
        self.address = address

        self.values = (
            self.id, self.name, self.email,  self.password, self.phone_number, self.address
        )

    def add_user(self):
        with DB() as db:
            db.execute(
                '''
                    INSERT INTO users (id, name, email, password, phone_number, address)
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', self.values
            )

            return self

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

    @staticmethod
    def get_user(id):

        with DB() as db:
            values = db.execute(
                '''
                    SELECT * FROM users
                    WHERE id=?
                ''', (id,)
            ).fetchone()

        return user(*values)

    @staticmethod
    def get_user_id(mail):
        with DB() as db:
            id = db.execute(
                '''
                    SELECT id FROM users
                    WHERE email=?
                ''', (mail,)
            ).fetchone()

        return id[0]
