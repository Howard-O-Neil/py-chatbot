from datetime import datetime
from entities.project import Project
from entities.user import User
from app import db

class Repository:
    def add_data(self, data):
        db.session.add(data)
        db.session.commit()

    def add_user(self, user, team_id):
        team = db.session.query(Project).filter(Project.slack_team_id==team_id).first()
        team.users.append(user)

        db.session.add(team)
        db.session.commit()

        return ""

    def get_user_by_slack_id(self, user_id):
        return (
            db.session.query(User).filter(User.slack_id==user_id).first()
        )

    def remove_user(self, slack_id):
        user = db.session.query(User).filter(User.slack_id==slack_id).first()
        user.deleted_at = datetime.now()

        db.session.commit()

        return ""

    def activate_user(self, slack_id):
        user = db.session.query(User).filter(User.slack_id==slack_id).first()
        user.deleted_at = None

        db.session.commit()

        return ""

repository = Repository()
