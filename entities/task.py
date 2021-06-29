from sqlalchemy.orm import relationship
from app import db
from sqlalchemy import Integer, Float, String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from uuid import uuid4
from sqlalchemy.sql import func
from sqlalchemy.sql.expression import text

class Task(db.Model):
    __tablename__ = "task"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4())
    backlog_id = db.Column(UUID(as_uuid=True), ForeignKey("backlog.id"), nullable=True)
    assignee = db.Column(UUID(as_uuid=True), ForeignKey("user.id"), nullable=True)
    iteration_id = db.Column(
        UUID(as_uuid=True), ForeignKey("iteration.id"), nullable=False
    )
    type = db.Column(String, nullable=False) # Iteration, Backlog
    status = db.Column(String, nullable=False) # Done, Undone
    name = db.Column(String, nullable=False)
    estimated_hours = db.Column(Float, nullable=True)
    created_at = db.Column(DateTime, nullable=False, default=func.now())
    updated_at = db.Column(
        DateTime, nullable=False, default=func.now(), onupdate=func.now()
    )
    deleted_at = db.Column(DateTime, nullable=True)
