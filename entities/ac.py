from sqlalchemy.sql.schema import ForeignKey
from app import db
from sqlalchemy import Float, DateTime, String, Date
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime

class AC(db.Model):
  __tablename__ = 'ac'

  id = db.Column(UUID(as_uuid=True), primary_key=True)
  backlog_id = db.Column(UUID(as_uuid=True), ForeignKey('backlog.id'))
  name = db.Column(String, nullable=False)
  description = db.Column(String, nullable=False)
  created_at = db.Column(DateTime, nullable=False, default=datetime.utcnow)
  updated_at = db.Column(DateTime, nullable=False, default=datetime.utcnow)
  deleted_at = db.Column(DateTime, nullable=True)