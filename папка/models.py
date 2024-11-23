from flask_sqlalchemy import SQLAlchemy  

db = SQLAlchemy()  

class User(db.Model):  
    id = db.Column(db.Integer, primary_key=True)  
    email = db.Column(db.String(120), unique=True, nullable=False)  
    subscriptions = db.relationship('Subscription', backref='subscriber', lazy=True)  

class Article(db.Model):  
    id = db.Column(db.Integer, primary_key=True)  
    title = db.Column(db.String(200), nullable=False)  
    content = db.Column(db.Text, nullable=False)  
    category = db.Column(db.String(50), nullable=False)  
    timestamp = db.Column(db.DateTime, index=True, default=db.func.current_timestamp)  

class Subscription(db.Model):  
    id = db.Column(db.Integer, primary_key=True)  
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  
    category = db.Column(db.String(50), nullable=False)