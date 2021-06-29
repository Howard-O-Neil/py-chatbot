from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from app import db
from sqlalchemy import String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from sqlalchemy.sql import func
from sqlalchemy.sql.expression import text

class User(db.Model):
    __tablename__ = "user"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4())
    slack_id = db.Column(String, nullable=False, unique=True)
    name = db.Column(String(100), nullable=True)
    phone = db.Column(String(15), nullable=True)
    email = db.Column(String, nullable=True)
    created_at = db.Column(DateTime, nullable=False, default=func.now())
    updated_at = db.Column(
        DateTime, nullable=False, default=func.now(), onupdate=func.now()
    )
    deleted_at = db.Column(DateTime, nullable=True)

    # relationship
    projects = relationship("Project", secondary="user_project", back_populates="users")
