import os  

class Config:  
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key'  
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'  
    SQLALCHEMY_TRACK_MODIFICATIONS = False  
    MAIL_SERVER = 'smtp.example.com'  
    MAIL_PORT = 587  
    MAIL_USE_TLS = True  
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')  
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')