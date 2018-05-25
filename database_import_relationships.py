from flask_app import db
db.create_all()
from flask_app import User, Post, Author

db.session.add(Author)
db.session.commit()