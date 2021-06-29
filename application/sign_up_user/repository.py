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

repository = Repository()
