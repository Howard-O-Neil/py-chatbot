from app import db
from sqlalchemy import Float, String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from uuid import uuid4
from sqlalchemy.sql import func
from sqlalchemy.sql.expression import text

class UserWorkload(db.Model):
    __tablename__ = "user_workload"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4())
    user_id = db.Column(UUID(as_uuid=True), ForeignKey("user.id"))
    iteration_id = db.Column(UUID(as_uuid=True), ForeignKey("iteration.id"))
    wordload = db.Column(Float, nullable=False)
    created_at = db.Column(DateTime, nullable=False, default=func.now())
    updated_at = db.Column(
        DateTime, nullable=False, default=func.now(), onupdate=func.now()
    )
    deleted_at = db.Column(DateTime, nullable=True)
