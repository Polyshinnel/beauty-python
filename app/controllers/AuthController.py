import hashlib
import secrets


class AuthController:
    def __init__(self, db, users, username=None, password=None):
        self.db = db
        self.users = users
        self.username = username
        self.password = password

    def __check_auth(self):
        username = self.username
        password = self.password
        users = self.users
        pass_hash = self.__get_hash(password)
        res = users.query.filter_by(login=username, passw=pass_hash).all()
        if len(res) > 0:
            return res[0]
        return False

    def get_token(self):
        model = self.__check_auth()
        if model:
            token = secrets.token_hex(16)
            model.token = token
            self.db.session.commit()
            return token
        return False

    def check_token(self, token):
        users = self.users
        res = users.query.filter_by(token=token).all()
        if len(res) > 0:
            return True
        return False



    @staticmethod
    def __get_hash(password):
        hashobj = hashlib.md5(password.encode())
        return hashobj.hexdigest()
