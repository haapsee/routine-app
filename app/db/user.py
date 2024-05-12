from hashlib import sha256
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.db import getEngine
from app.models.user import User


def authenticateUser(email, password):
    user = None
    with Session(getEngine()) as session:
        user = getUserByEmail(email)
        if not user:
            return None
        if not validatePassword(password, user):
            return None
    return user

def createUser(firstname, lastname, email, password):
    passhash=hashPassword(password)
    with Session(getEngine()) as session:
        user = User(firstname=firstname, lastname=lastname, email=email, password=passhash)
        session.add(user)
        session.commit()
        return getUserById(user.id)

def getUserById(id):
    with Session(getEngine()) as session:
        statement = select(User).where(User.id == id)
        return session.scalars(statement).one()

def getUserByEmail(email):
    with Session(getEngine()) as session:
        statement = select(User).where(User.email == email)
        return session.scalars(statement).one()

def validatePassword(password, user):
    return hashPassword(password) == user.password

def hashPassword(password):
    return sha256(password.encode('utf-8')).hexdigest()
