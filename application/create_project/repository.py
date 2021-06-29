from entities.user import User
from app import db

class Repository:
    def add_data_flush(self, data):
        db.session.add(data)
        db.session.flush()
        db.session.refresh(data)

        return data

    def commit(self):
        db.session.commit()

    def rollback(self):
        db.session.rollback()




repository = Repository()
