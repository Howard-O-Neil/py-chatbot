from sqlalchemy.sql.schema import ForeignKey
from app import db
from sqlalchemy import Float, DateTime, String, Date
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from datetime import datetime
from uuid import uuid4
from sqlalchemy.sql.expression import text



class MeetingLocation(db.Model):
    __tablename__ = "meeting_location"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4())
    name = db.Column(String, nullable=False, unique=True)
    created_at = db.Column(DateTime, nullable=False, default=func.now())
    updated_at = db.Column(
        DateTime, nullable=False, default=func.now(), onupdate=func.now()
    )
    deleted_at = db.Column(DateTime, nullable=True)
