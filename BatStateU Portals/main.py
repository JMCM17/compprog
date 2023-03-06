from flask import Flask, render_template, request
import random
import unorganized

app = Flask(__name__)


@app.route('/')
def home():
    background = random.choice(unorganized.backgrounds)
    return render_template('login.html', background_url=background, campuses=unorganized.campuses)


if __name__ == '__main__':
    app.run(debug=True)
