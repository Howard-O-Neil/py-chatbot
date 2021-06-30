from sqlalchemy.orm import relationship
from app import db
from sqlalchemy import Float, String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from uuid import uuid4
from sqlalchemy.sql import func
from sqlalchemy.sql.expression import text

class UserProject(db.Model):
    __tablename__ = "user_project"

    id = db.Column(UUID(as_uuid=True), default=uuid4())
    user_id = db.Column(UUID(as_uuid=True), ForeignKey("user.id"), primary_key=True)
    project_id = db.Column(
        UUID(as_uuid=True), ForeignKey("project.id"), primary_key=True
    )


class Project(db.Model):
    __tablename__ = "project"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4())
    name = db.Column(String, nullable=False, unique=True)
    goal = db.Column(String, nullable=False)
    description = db.Column(String, nullable=False)
    estimated_hours = db.Column(Float, nullable=False)
    slack_team_id = db.Column(String, nullable=False, unique=True)
    slack_member_monitor_token = db.Column(String, nullable=False, unique=True)
    slack_bot_token = db.Column(String, nullable=False, unique=True)
    created_at = db.Column(DateTime, nullable=False, default=func.now())
    updated_at = db.Column(
        DateTime, nullable=False, default=func.now(), onupdate=func.now()
    )
    deleted_at = db.Column(DateTime, nullable=True)

    # relationship
    users = relationship("User", secondary="user_project", back_populates="projects")
