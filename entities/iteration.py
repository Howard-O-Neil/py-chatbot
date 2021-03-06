from app import db
from sqlalchemy import Float, String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from uuid import uuid4
from sqlalchemy.sql import func
from sqlalchemy.sql.expression import text


class Iteration(db.Model):
    __tablename__ = "iteration"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4())
    project_id = db.Column(UUID(as_uuid=True), ForeignKey("project.id"))
    start_date = db.Column(DateTime, nullable=False)
    status = db.Column(String, nullable=False) # Processing, Done, NotStarted
    name = db.Column(String, nullable=False)
    goal = db.Column(String, nullable=False)
    description = db.Column(String, nullable=False)
    velocity = db.Column(Float, nullable=False)
    point = db.Column(Float, nullable=False)
    estimated_hours = db.Column(Float, nullable=False)
    logged_hours = db.Column(Float, nullable=False)
    created_at = db.Column(DateTime, nullable=False, default=func.now())
    updated_at = db.Column(
        DateTime, nullable=False, default=func.now(), onupdate=func.now()
    )
    deleted_at = db.Column(DateTime, nullable=True)
