from flask import Flask, render_template, redirect, flash, url_for, session
from models import db, connect_db, User, Feedback
from forms import RegistrationForm, LoginForm, FeedbackForm, UpdateFeedback
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)

# App configuration
app.config['SECRET_KEY'] = 'scktK'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///auth_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.debug = True
toolbar = DebugToolbarExtension(app)

# Connect to the database and create tables
with app.app_context():
    connect_db(app)
    db.create_all()

@app.route('/')
def index():
    """Redirect to the registration page."""
    return redirect('/register')

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Handle user registration."""
    if "username" in session:
        return redirect(url_for('secret', username=session['username']))

    form = RegistrationForm()

    if form.validate_on_submit():
        user_data = {
            'first_name': form.first_name.data,
            'last_name': form.last_name.data,
            'username': form.username.data,
            'email': form.email.data,
            'password': form.password.data
        }

        user = User.register(**user_data)

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('secret', username=user.username))

    return render_template('registrationForm.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Handle user login."""
    if 'username' in session:
        return redirect(url_for('secret', username=session['username']))

    form = LoginForm()

    if form.validate_on_submit():
        user_data = {
            'username': form.username.data,
            'password': form.password.data
        }

        user = User.authorize(**user_data)

        if user:
            session['username'] = user.username
            return redirect(url_for("secret", username=user.username))

    return render_template('loginForm.html', form=form)

@app.route('/users/<username>')
def secret(username):
    """Display user information and feedbacks."""
    if 'username' not in session:
        return redirect(url_for('login'))
    else:
        user = User.query.filter_by(username=username).first()
        feedbacks = Feedback.query.filter_by(username=user.username).all()
        return render_template('secret.html', user=user, feedbacks=feedbacks)

@app.route('/logout', methods=['POST'])
def logout():
    """Handle user logout."""
    session.pop('username')
    return redirect(url_for('login'))

@app.route('/users/<username>/feedback/add', methods=['GET', 'POST'])
def create_feedback(username):
    """Handle creation of new feedback."""
    form = FeedbackForm()
    user = User.query.filter_by(username=username).first()

    if 'username' not in session:
        return redirect(url_for('login'))

    if form.validate_on_submit():
        feedback_content = {
            "title": form.title.data,
            "content": form.content.data,
            "username": user.username
        }

        user_feedback = Feedback(**feedback_content)

        db.session.add(user_feedback)
        db.session.commit()

        return redirect(url_for('secret', username=user.username))
    else:
        return render_template('createFeedbackForm.html', form=form, user=user)

@app.route('/feedback/<int:id>/update', methods=['GET', 'POST'])
def update_feedback(id):
    """Handle updating existing feedback."""
    username = session['username']

    if username:
        feedback = Feedback.query.get_or_404(id)

        # Create form and populate it with existing feedback data
        form = UpdateFeedback(obj=feedback)
        user = feedback.user

        if form.validate_on_submit():
            # Update feedback object with data from the form
            form.populate_obj(feedback)
            db.session.commit()

            return redirect(url_for('secret', username=session['username']))

        else:
            return render_template('updateFeedback.html', form=form, feedback=feedback, user=user)

@app.route('/feedback/<id>/delete', methods=['POST'])
def delete_feedback(id):
    """Handle deletion of feedback."""
    username = session['username']

    if username:
        feedback = Feedback.query.get_or_404(id)
        db.session.delete(feedback)
        db.session.commit()
        return redirect(url_for('secret', username=session['username']))
    else:
        return redirect(url_for('login'))

@app.route('/users/<username>/delete', methods=['POST'])
def delete_user(username):
    """Handle deletion of a user and associated feedbacks."""
    user = User.query.filter_by(username=username).first()

    if user:
        # Clear the session data for the username
        session.pop('username', None)

        # Delete user's feedbacks before deleting the user
        feedbacks = Feedback.query.filter_by(username=user.username).all()
        for feedback in feedbacks:
            db.session.delete(feedback)

        # Now, delete the user
        db.session.delete(user)
        db.session.commit()

    return redirect(url_for('index'))
