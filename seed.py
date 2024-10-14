from app import db, User

with db.app.app_context():
    db.create_all()

def seed_users():

    user1 = User(username='Evan', message='Hello')
    user2 = User(username='Gwen', message='Hi')

    db.session.add(user1)
    db.session.add(user2)

    db.session.commit()

    print("Users seeded")

if __name__ == '__main__':
    seed_users()