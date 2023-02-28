from flask import Flask, render_template, request
from bg import backgrounds
import random
import random_lists

app = Flask(__name__)


@app.route('/')
def home():
    background_url = random.choice(backgrounds)
    return render_template('login-base.html', background=background_url, campuses=random_lists.campuses)


@app.route('/handle_form', methods=['POST'])
def handle_form():
    username = request.form.get('username')
    password = request.form.get('password')
    remember_me = request.form.get('remember_me')
    # Do something with the form data
    print(username, password)
    return 'Form submitted successfully!'


if __name__ == '__main__':
    app.run()
