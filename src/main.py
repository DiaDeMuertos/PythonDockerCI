from db import session, User
from sqlalchemy.ext.declarative import declarative_base 

if __name__ == "__main__":
    newUser = User(name='glen', fullname='dino princess', password='pup-pup')

    session.add(newUser)
    session.commit()

    for user in session.query(User).all():
        print(user)
