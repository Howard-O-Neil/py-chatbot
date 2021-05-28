from sqlalchemy.orm import relationship
from app import db
from sqlalchemy import Integer, Float, String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

class Backlog(db.Model):
  __tablename__ = 'backlog'

  id = db.Column(UUID(as_uuid=True), primary_key=True)
  theme_id = db.Column(UUID(as_uuid=True), ForeignKey('theme.id'))
  epic_id = db.Column(UUID(as_uuid=True), ForeignKey('epic.id'))
  status = db.Column(String, nullable=False)
  progress = db.Column(Float, nullable=True)
  name = db.Column(String, nullable=False)
  goal = db.Column(String, nullable=False)
  description = db.Column(String, nullable=False)
  point = db.Column(Integer, nullable=False)
  created_at = db.Column(DateTime, nullable=False)
  updated_at = db.Column(DateTime, nullable=False)
  deleted_at = db.Column(DateTime, nullable=True)