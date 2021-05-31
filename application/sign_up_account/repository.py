from entities.user import User
from app import db

class Repository:
    def add_data(self, data):
        db.session.add(data)
        db.session.commit()

repository = Repository()
