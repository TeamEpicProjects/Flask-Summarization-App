Flask Summarization App Documentation


Introduction:

The Flask Summarization App is a web application developed using the Flask web framework. It
allows users to log in, input text, and generate a summary of the input text using a text
summarization model.


Features:

● User authentication: Users can log in with a username and password.
● Text Summarization: Users can input text into a form, and the application generates a
summary of the input text using a text summarization model.
● SQLite Database: User login details and input/output text summaries are stored in an
SQLite database.
Installation
git clone https://github.com/devesh2525/Flask-Summarization-App/settings


AI Model:

● Model: Fine-Tuned T5 Small for Text Summarization (an open source model from
Falconsai) https://huggingface.co/Falconsai/text_summarization
● The Fine-Tuned T5 Small is a variant of the T5 transformer model, designed
for the task of text summarization. It is adapted and fine-tuned to generate
concise and coherent summaries of input text.
● During the fine-tuning process, a batch size of 8 is chosen for efficient
computation and learning. Additionally, a learning rate of 2e-5 is selected to
balance convergence speed and model optimization
● Model size: 60.5M parameters


Running the Application:

1. Navigate to the project directory.
2. Activate the virtual environment (if using).
3. Run the Flask application:
python run.py
Access the application in your web browser at http://127.0.0.1:5050.
Project Structure
The project follows a standard Flask application structure:
● app/
○ __init__.py: Initializes the Flask application and sets up configurations.
○ forms.py: Defines Flask-WTF forms used in the application.
○ models.py: Defines SQLAlchemy models for the database.
○ routes.py: Contains URL routes, view functions and AI components.
○ templates/: Contains HTML templates for rendering views.
● venv/: Virtual environment directory.(if using)
● run.py


Usage:

1. Login:
○ Navigate to the login page (/).
○ Enter the username and password and submit the form.
i. Username: admin
ii. Password: password
○ Upon successful login, the application redirects to the text summarization page.
2. Text Summarization:
○ Enter the input text in the provided textarea.
○ Click the "Summarize" button.
○ The application generates a summary of the input text and displays it below the
form.


Dependencies:

● Flask: Web framework for building web applications.
● Flask-WTF: Provides integration with WTForms for handling web forms.
● SQLAlchemy: Object-Relational Mapping (ORM) library for database interactions.
● transformers: Library for Natural Language Processing (NLP) tasks, used for text
summarization.
● Werkzeug: Utility library for handling WSGI requests.



Contributor(s):
● Devesh Sharm
