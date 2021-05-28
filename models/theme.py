from sqlalchemy.orm import relationship
from app import db
from sqlalchemy import Float, String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

class Theme(db.Model):
  __tablename__ = 'theme'

  id = db.Column(UUID(as_uuid=True), primary_key=True)
  project_id = db.Column(UUID(as_uuid=True), ForeignKey('project.id'))
  name = db.Column(String, nullable=False)
  description = db.Column(String, nullable=False)
  created_at = db.Column(DateTime, nullable=False)
  updated_at = db.Column(DateTime, nullable=False)
  deleted_at = db.Column(DateTime, nullable=True)