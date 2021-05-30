from sqlalchemy.orm import relationship
from app import db
from sqlalchemy import Integer, Float, String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

class Task(db.Model):
  __tablename__ = 'task'

  id = db.Column(UUID(as_uuid=True), primary_key=True)
  backlog_id = db.Column(UUID(as_uuid=True), ForeignKey('backlog.id'), nullable=True)
  iteration_id = db.Column(UUID(as_uuid=True), ForeignKey('iteration.id'), nullable=False)
  type = db.Column(String, nullable=False)
  status = db.Column(String, nullable=False)
  name = db.Column(String, nullable=False)
  estimated_hours = db.Column(Float, nullable=False)
  created_at = db.Column(DateTime, nullable=False)
  updated_at = db.Column(DateTime, nullable=False)
  deleted_at = db.Column(DateTime, nullable=True)