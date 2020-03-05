from flask import Flask
from data import db_session
from data.users import User


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    session = db_session.create_session()
    user0 = User()
    user0.name = 'Ridley'
    user0.surname = 'Scott'
    user0.age = 21
    user0.position = 'captain'
    user0.speciality = 'research engineer'
    user0.address = 'module_1'
    user0.email = 'scott_chief@mars.org'
    session.add(user0)
    user1 = User()
    user1.name = 'Neal'
    user1.surname = 'Armstrong'
    user1.age = 82
    user1.position = 'senior engineer'
    user1.speciality = 'biologist'
    user1.address = 'module_1'
    user1.email = 'neal_armstrong@mars.org'
    session.add(user1)
    user2 = User()
    user2.name = 'Ivan'
    user2.surname = 'Sokolov'
    user2.position = 'Junior scientist'
    user2.speciality = 'programmer'
    user2.age = 24
    user2.address = 'module_2'
    user2.email = 'ivan000@mars.org'
    session.add(user2)
    session.commit()
    app.run()


if __name__ == '__main__':
    db_session.global_init("db/mars.sqlite")
    main()