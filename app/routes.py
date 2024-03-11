from flask import render_template, redirect, url_for, request, session
from app import app
from app.models import InteractionHistory
from app.forms import LoginForm
from transformers import pipeline
from datetime import datetime
from app import db

# Hardcoded username and password
HARDCODED_USERNAME = "admin"
HARDCODED_PASSWORD = "password"

def summarize_text(text):
    summarizer = pipeline("summarization", model="Falconsai/text_summarization")
    output = summarizer(text, max_length=1000, min_length=30, do_sample=False)
    return output

@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        if username == HARDCODED_USERNAME and password == HARDCODED_PASSWORD:
            session['user_id'] = 1  # Dummy user ID
            return redirect(url_for('text_summarization'))
        else:
            return render_template('login.html', title='Login', form=form, error="Invalid username or password.")
    return render_template('login.html', title='Login', form=form)

@app.route('/text_summarization', methods=['GET', 'POST'])
def text_summarization():
    form = request.form
    summarized_text = None
    interactions = None

    if form and request.method == 'POST':
        input_text = form.get('inputText')
        if input_text:
            # Summarize the text
            summarized_text_list = summarize_text(input_text)

            # Extract the string value from the list and dictionary
            summarized_text_str = summarized_text_list[0]['summary_text'] if summarized_text_list else None

            # Retrieve user ID from session
            user_id = session.get('user_id')

            # Store interaction history
            if user_id and summarized_text_str:
                interaction = InteractionHistory(user_id=user_id, input_text=input_text, summarized_text=summarized_text_str)
                db.session.add(interaction)
                db.session.commit()

            # Assign the summarized text to the variable to pass to the template
            summarized_text = summarized_text_str

    # Retrieve interaction history for current user
    user_id = session.get('user_id')
    print(user_id)
    if user_id:
        interactions = InteractionHistory.query.filter_by(user_id=user_id).order_by(InteractionHistory.timestamp.desc()).all()

    return render_template('home.html', form=form, summarized_text=summarized_text, interactions=interactions)
