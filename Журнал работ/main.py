from flask import Flask, render_template
from data import db_session
from data.jobs import Jobs
from data.users import User
import datetime


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def main():
    session = db_session.create_session()
    print(0)
    print(session.query(Jobs).all())
    return render_template('jobs.html', data=session.query(Jobs), session=session, User=User)


if __name__ == '__main__':
    db_session.global_init("db/mars.sqlite")
    app.run(port=8080, host='127.0.0.1')