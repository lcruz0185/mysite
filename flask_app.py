
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_sslify import SSLify
from flask import flash
from flask_login import LoginManager, UserMixin, current_user, login_user, logout_user
from datetime import datetime

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Email, Length

from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash

from flask import redirect
from flask import request
from flask import url_for
from wtforms.validators import ValidationError

# import constants

app = Flask(__name__)

app.config.from_object('config.BaseConfig')
db = SQLAlchemy(app)
# username code (down) ****************************************
#app.config['SQUALCHEMY_DATABASE_URI'] = 'sqlite:///relationships.db'

login = LoginManager(app)

Bootstrap(app)
SSLify(app)

from flask_nav import Nav
from flask_nav.elements import Navbar, Subgroup, View

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    period = db.Column(db.Integer)
    name = db.Column(db.String(80))
    teacher_name = db.Column(db.String(80))
    resource_name = db.Column(db.String(80))
    resource_url = db.Column(db.String(300))

class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    artist_name = db.Column(db.String(80))
    youtube_url = db.Column(db.String(300))

#NEW PAGE#

class Album_post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(280))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class AlbumForm(FlaskForm):
    message = StringField('Album', validators=[InputRequired(), Length(max=280)])
    submit = SubmitField('Post')

class RegistrationForm(FlaskForm):
    username = StringField(
        'Username', validators=[InputRequired(), Length(min=4, max=15)])
    email = StringField(
        'Email', validators=[InputRequired(), Email()])
    password = PasswordField(
        'Password', validators=[InputRequired(), Length(min=8, max=80)])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please choose a different username.')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Sign in')

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15))
    email = db.Column(db.String(150))
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref="author", order_by= 'desc(Post.timestamp)')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(280))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

'''
class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    user_id = db.column(db.Integer, db.ForeignKey('user.id')
'''

class PostForm(FlaskForm):
    message = StringField('Message', validators=[InputRequired(), Length(max=280)])
    submit = SubmitField('Post')

@login.user_loader
def load_user(user_id):
    return User.query.filter_by(id=int(user_id)).first()

@app.route('/')
def homepage():
    recent_posts = Post.query.order_by(Post.timestamp.desc()).limit(20).all()
    return render_template('index.html', posts=recent_posts)

@app.route('/about_me')
def about_me():
    return render_template('about_me.html')

@app.route('/class_schedule')
def class_schedule():
    courses = Course.query.all()
    return render_template('class_schedule.html',
                           courses=courses)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = User(
            username=form.username.data,
            email=form.email.data)
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for('homepage'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('homepage'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if not user or not user.check_password(form.password.data):
            flash('Username or password is incorrect.', 'danger')
            return render_template('login.html', form=form)
        login_user(user)
        return redirect(url_for('homepage'))
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('homepage'))

@app.route('/top_ten_songs')
def top_ten_songs():
    songs = Song.query.all()
    return render_template('top_ten_songs.html',songs=songs)

@app.route('/posts', methods=['GET', 'POST'])
def posts():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    form = PostForm()
    posts = Post.query.filter_by(user_id=current_user.id).all()
    if form.validate_on_submit():
        new_post = Post(user_id=current_user.id, body=form.message.data)
        db.session.add(new_post)
        db.session.commit()
        posts.append(new_post)
    return render_template('posts.html', form=form, posts=posts)

'''
@app.route('/delete_post')
def delete_post():
    post_id = request.args.get('id')
    if not post_id:
        return redirect(url_for('homepage')) #for the album post, post=?
    post = Post.query.filter.by(id=post_id).first()
    #if not post or post.author.id != current_user.id: return redirect(url_for('homepage'))
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('posts', posts=current_user.posts))
'''

@app.route('/album_post', methods=['GET', 'POST'])
def album_post():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    form = AlbumForm()
    album_posts = Album_post.query.filter_by(user_id=current_user.id).all()
    if form.validate_on_submit():
        new_album_post = Album_post(user_id=current_user.id, body=form.message.data)
        db.session.add(new_album_post)
        db.session.commit()
        album_posts.append(new_album_post)
    return render_template('album_post.html', form=form, album_posts=album_posts)

if __name__ == '__main__':
  db.create_all()

nav = Nav(app)
@nav.navigation('mysite_navbar')
def create_navbar():
    home_view = View('Home', 'homepage')
    login_view = View('Login', 'login')
    logout_view = View('Logout', 'logout')
    posts_view = View('Posts', 'posts')
    album_post_view = View('Album Post', 'album_post')
    register_view = View('Register', 'register')
    about_me_view = View('About Me', 'about_me')
    class_schedule_view = View('Class Schedule', 'class_schedule')
    top_ten_songs_view = View('Top Ten Songs', 'top_ten_songs')
    misc_subgroup = Subgroup('Misc',
                             about_me_view,
                             class_schedule_view,
                             top_ten_songs_view)
    if current_user.is_authenticated:
        return Navbar('MySite', home_view, posts_view, album_post_view, misc_subgroup, logout_view)
    else:
        return Navbar('MySite', home_view, misc_subgroup, login_view, register_view)
