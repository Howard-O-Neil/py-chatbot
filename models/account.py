from sqlalchemy.sql.sqltypes import JSON
from app import db
from sqlalchemy import Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.sqltypes import JSON

class Account(db.Model):
  __tablename__ = 'account'

  id = db.Column(UUID(as_uuid=True), primary_key=True)
  url = db.Column(String)
  name = db.Column(String)