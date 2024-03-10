from flask import render_template, redirect, url_for, request
from werkzeug.security import generate_password_hash
from app import app, db
from app.models import User
from app.forms import LoginForm
from transformers import pipeline

def summarize_text(text):
    summarizer = pipeline("summarization", model="Falconsai/text_summarization")
    output = summarizer(text, max_length=1000, min_length=30, do_sample=False)
    return output

@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == 'admin' and form.password.data == 'password':
            hashed_password = generate_password_hash(form.password.data)  # Hash the password
            user = User(username=form.username.data, password=hashed_password)  # Create user with hashed password
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('text_summarization'))
    return render_template('login.html', title='Login', form=form)

@app.route('/text_summarization', methods=['GET', 'POST'])
def text_summarization():
    form = request.form
    summarized_text = None
    if form and request.method == 'POST':
        input_text = form.get('inputText')
        if input_text:
            summarized_text = summarize_text(input_text)
    return render_template('home.html', form=form, summarized_text=summarized_text)
