from flask import Flask, render_template, request, redirect, url_for  
from flask_mail import Mail, Message  
from models import db, User, Article, Subscription  
from config import Config  
from datetime import datetime, timedelta  

app = Flask(__name__)  
app.config.from_object(Config)  
db.init_app(app)  
mail = Mail(app)  

@app.route('/register', methods=['POST'])  
def register():  
    email = request.form['email']  
    user = User(email=email)  
    db.session.add(user)  
    db.session.commit()  
    send_welcome_email(email)  
    return redirect(url_for('home'))  

def send_welcome_email(email):  
    msg = Message('Welcome to News Portal!', sender='noreply@example.com', recipients=[email])  
    msg.body = 'Thank you for subscribing to our News Portal!'  
    msg.html = render_template('welcome_email.html')  
    mail.send(msg)  

@app.route('/subscribe', methods=['POST'])  
def subscribe():  
    email = request.form['email']  
    category = request.form['category']  
    user = User.query.filter_by(email=email).first()  
    
    if user:  
        subscription = Subscription(user_id=user.id, category=category)  
        db.session.add(subscription)  
        db.session.commit()  
    return redirect(url_for('home'))  

def send_weekly_summary():  
    one_week_ago = datetime.now() - timedelta(days=7)  
    articles = Article.query.filter(Article.timestamp >= one_week_ago).all()  
    
    users = User.query.all()  
    for user in users:  
        user_subscriptions = Subscription.query.filter_by(user_id=user.id).all()  
        user_categories = [sub.category for sub in user_subscriptions]  
        
        new_articles = [article for article in articles if article.category in user_categories]  
        if new_articles:  
            send_summary_email(user.email, new_articles)  

def send_summary_email(email, articles):  
    msg = Message('Weekly Summary of New Articles', sender='noreply@example.com', recipients=[email])  
    msg.html = render_template('weekly_summary.html', articles=articles)  
    mail.send(msg)  

if __name__ == '__main__':  
    with app.app_context():  
        db.create_all()  
    app.run(debug=True)