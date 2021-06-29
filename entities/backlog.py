from sqlalchemy.orm import relationship
from app import db
from sqlalchemy import Integer, Float, String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from uuid import uuid4
from sqlalchemy.sql import func
from sqlalchemy.sql.expression import text


class Backlog(db.Model):
    __tablename__ = "backlog"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4())
    theme_id = db.Column(UUID(as_uuid=True), ForeignKey("theme.id"))
    epic_id = db.Column(UUID(as_uuid=True), ForeignKey("epic.id"))
    iteration_id = db.Column(UUID(as_uuid=True), ForeignKey("iteration.id"))
    status = db.Column(String, nullable=False) # Done, Undone, PartialDone
    progress = db.Column(Float, nullable=True) # 0 - 100 %
    name = db.Column(String, nullable=False)
    goal = db.Column(String, nullable=False)
    description = db.Column(String, nullable=False)
    point = db.Column(Integer, nullable=False)
    created_at = db.Column(DateTime, nullable=False, default=func.now())
    updated_at = db.Column(
        DateTime, nullable=False, default=func.now(), onupdate=func.now()
    )
    deleted_at = db.Column(DateTime, nullable=True)
