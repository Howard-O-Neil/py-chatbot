from uuid import UUID
from sqlalchemy.sql.expression import and_
from entities.iteration import Iteration
from entities.project import Project
from entities.task import Task
from entities.meeting import Meeting
from entities.meeting_location import MeetingLocation
from entities.user import User
from sqlalchemy.orm import aliased
from sqlalchemy import intersect, except_
from app import db


class Repository:
    def add_data(self, data):
        db.session.add(data)
        db.session.commit()

    def find_meeting_location_by_name(self, name):
        return (
            db.session.query(MeetingLocation)
            .filter(MeetingLocation.name.ilike(f"%{name}%"))
            .first()
        )

    def get_task_by_id(self, task_id):
        return db.session.query(Task).filter(Task.id==task_id).first()

    def asign_task(self, user_id, task_id, estimate):
        task = self.get_task_by_id(task_id)
        task.assignee = user_id
        if estimate > 0:
            task.estimated_hours = estimate

        db.session.commit()

    def markdone_task(self, task_id, status):
        task = self.get_task_by_id(task_id)
        task.status = status

        db.session.commit()

    def add_meeting(self, meeting):
        db.session.add(meeting)
        db.session.commit()

    def get_user_by_slack_id(self, user_id):
        return (
            db.session.query(User).filter(User.slack_id==user_id).first()
        )        

    def get_project_by_team_id(self, team_id):
        return db.session.query(Project).filter(Project.slack_team_id==team_id).first()

    def get_current_iteration_by_team_id(self, team_id):
        team = self.get_project_by_team_id(team_id)
        return db.session.query(Iteration).filter(
            and_(
                Iteration.project_id==team.id,
                Iteration.status=="Processing"
            )
        ).first()

    def get_available_task(self, team_id, limit_result):
        iteration = self.get_current_iteration_by_team_id(team_id)

        return db.session.query(Task).filter(Task.iteration_id==iteration.id).limit(limit_result).all()

    def get_available_doing_task(self, team_id, user_id):
        iteration = self.get_current_iteration_by_team_id(team_id)

        return db.session.query(Task).filter(
            and_(
                Task.iteration_id==iteration.id,
                Task.assignee==user_id,
                Task.status=='Undone'
            )
            ).all()


repository = Repository()
