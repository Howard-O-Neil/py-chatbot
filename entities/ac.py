from sqlalchemy.sql.schema import ForeignKey
from app import db
from sqlalchemy import Float, DateTime, String, Date
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from uuid import uuid4
from sqlalchemy.sql import func
from sqlalchemy.sql.expression import text


class AC(db.Model):
    __tablename__ = "ac"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4())
    backlog_id = db.Column(UUID(as_uuid=True), ForeignKey("backlog.id"))
    name = db.Column(String, nullable=False)
    description = db.Column(String, nullable=False)
    created_at = db.Column(DateTime, nullable=False, default=func.now())
    updated_at = db.Column(
        DateTime, nullable=False, default=func.now(), onupdate=func.now()
    )
    deleted_at = db.Column(DateTime, nullable=True)