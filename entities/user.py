from datetime import datetime
from sqlalchemy.orm import relationship
from app import db
from sqlalchemy import String, DateTime
from sqlalchemy.dialects.postgresql import UUID

class User(db.Model):
  __tablename__ = 'user'

  id = db.Column(UUID(as_uuid=True), primary_key=True)
  facebook_url = db.Column(String, nullable=False)
  name = db.Column(String(100), nullable=False)
  phone = db.Column(String(15), nullable=False)
  email = db.Column(String, nullable=False)
  created_at = db.Column(DateTime, nullable=False, default=datetime.utcnow)
  updated_at = db.Column(DateTime, nullable=False, default=datetime.utcnow)
  deleted_at = db.Column(DateTime, nullable=True)

  # relationship
  projects = relationship(
    'Project',
    secondary='user_project',
    back_populates='users'
  )