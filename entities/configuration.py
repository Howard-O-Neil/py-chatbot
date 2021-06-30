from sqlalchemy.orm import relationship
from app import db
from sqlalchemy import Integer, Float, String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from uuid import uuid4
from sqlalchemy.sql import func
from sqlalchemy.sql.expression import text


class Configuration(db.Model):
    __tablename__ = "configuration"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4())
    key = db.Column(String, nullable=False, unique=True)
    value = db.Column(String, nullable=False)
    created_at = db.Column(DateTime, nullable=False, default=func.now())
    updated_at = db.Column(
        DateTime, nullable=False, default=func.now(), onupdate=func.now()
    )
    deleted_at = db.Column(DateTime, nullable=True)
