from operator import or_
from entities.project import Project
from entities.user import User
from app import db

class Repository:
    def add_data(self, data):
        db.session.add(data)
        db.session.commit()

    def find_by_team_id(self, team_id):
        return Project.query.filter(
            Project.slack_team_id==team_id
        ).all()


    def find_by_admin_team(self, admin_id, team_id):
        return Project.query.filter(
            or_(
                Project.slack_team_admin_id==admin_id,
                Project.slack_team_id==team_id
            )
        ).all()

repository = Repository()
