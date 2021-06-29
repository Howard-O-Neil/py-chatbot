from entities.project import Project
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

    def add_meeting(self, meeting):
        db.session.add(meeting)
        db.session.commit()

    def get_user_by_slack_id(self, user_id):
        return (
            db.session.query(User).filter(User.slack_id==user_id).first()
        )
    
    def get_all_project(self):
        return (
            db.session.query(Project).all()
        )

    def get_available_meeting_location(self, limit_result):
        m1 = aliased(Meeting)

        subquery1 = db.session.query(MeetingLocation)
        subquery2 = db.session.query(MeetingLocation).join(
            m1, m1.location_id == MeetingLocation.id
        )

        if limit_result >= 0:
            return (
                db.session.query(MeetingLocation)
                .from_statement(except_(subquery1, subquery2).limit(limit_result))
                .all()
            )
        else:
            return (
                db.session.query(MeetingLocation)
                .from_statement(except_(subquery1, subquery2))
                .all()
            )


repository = Repository()
