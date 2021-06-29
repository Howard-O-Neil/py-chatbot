from sqlalchemy.sql.schema import ForeignKey
from app import db
from sqlalchemy import Float, DateTime, String, Date
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from uuid import uuid4
from sqlalchemy.sql import func
from sqlalchemy.sql.expression import text

class Meeting(db.Model):
    __tablename__ = "meeting"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4())
    name = db.Column(String, nullable=False)
    start = db.Column(DateTime, nullable=False)
    end = db.Column(DateTime, nullable=False)
    assignee = db.Column(UUID(as_uuid=True), ForeignKey("user.id"), nullable=False)
    location_id = db.Column(UUID(as_uuid=True), ForeignKey("meeting_location.id"), nullable=False)
    created_at = db.Column(DateTime, nullable=False, default=func.now())
    updated_at = db.Column(
        DateTime, nullable=False, default=func.now(), onupdate=func.now()
    )
    deleted_at = db.Column(DateTime, nullable=True)
