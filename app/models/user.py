#!/usr/bin/python3
"""
"""
from flask_login import UserMixin
from config import db

from datetime import datetime
from uuid import uuid4


class User(UserMixin, db.Model):
    """ """

    __tablename__ = "users"
    id = db.Column(db.String(100), primary_key=True, default=str(uuid4()))
    merchant_id = db.Column(db.String(100), db.ForeignKey("merchants.id"))
    customer_id = db.Column(db.String(100), db.ForeignKey("customers.id"))
    username = db.Column(db.String(80), unique=True, nullable=False)
    first_name = db.Column(db.String(120))
    last_name = db.Column(db.String(120))
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(300), nullable=False)
    is_verified = db.Column(db.Boolean, default=False)
    is_merchant = db.Column(db.Boolean, default=False)
    is_customer = db.Column(db.Boolean, default=False)
    authenticated = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    @property
    def is_active(self):
        """True, as all users are active."""
        return True
    
    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.email

    @property
    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    @property
    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False

    def __repr__(self):
        return "<User: {} - {}>".format(self.username, self.email)
