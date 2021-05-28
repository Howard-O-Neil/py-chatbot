from app import db
from sqlalchemy import Integer, String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

class UserWeeklyReview(db.Model):
  __tablename__ = 'user-weekly-review'

  id = db.Column(UUID(as_uuid=True), primary_key=True)
  user_id = db.Column(UUID(as_uuid=True), ForeignKey(column='user.id', deferrable=True))
  review = db.Column(String, nullable=False)
  start_date = db.Column(DateTime, nullable=False)
  created_at = db.Column(DateTime, nullable=False)
  updated_at = db.Column(DateTime, nullable=False)
  deleted_at = db.Column(DateTime, nullable=True) 