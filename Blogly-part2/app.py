"""Blogly application."""

from flask import Flask, render_template, redirect, request, flash
from models import db, connect_db, User, Post

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Super_secret_key_goes_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

with app.app_context():
    connect_db(app)
    db.create_all()


@app.route('/')
def home():
    """Redirects to page that shoes all currents users"""
    return redirect('/users')



@app.route('/users')
def show_all_users():
    """Show a list of all users"""
    users = User.query.order_by(User.first_name, User.last_name, User.image_url).all()
    return render_template('all_users.html', users=users)



@app.route('/users/new', methods=['POST', 'GET'])
def form_for_new_user():
    """Form for a new user"""
    if request.method == 'POST':
        new_user = User(
            first_name = request.form.get('first_name'),
            last_name = request.form.get('last_name'),
            image_url = request.form.get('image_url') or None
        )
        
        db.session.add(new_user)
        db.session.commit()

        return redirect('/users')
    
    return render_template('new_user_form.html')


#ROUTE FOR USER'S DETALS

@app.route('/users/<int:user_id>')
def user_detail(user_id):
    """Show user details"""
    user = User.query.get_or_404(user_id)
    return render_template('user_details.html', user=user)


#ROUTE TO THE EXISTING USER EDIT FORM

@app.route('/users/<int:user_id>/edit')
def users_edit(user_id):
    """Show a form to edit an existing user"""

    user = User.query.get_or_404(user_id)
    return render_template('edit_profile.html', user=user)



#ROUTE TO EDIT THE USER'S PROFILE

@app.route('/users/<int:user_id>/edit', methods=["POST"])
def users_update(user_id):
    """Handle form submission for updating an existing user"""

    user = User.query.get_or_404(user_id)
    user.first_name = request.form['first_name']
    user.last_name = request.form['last_name']
    user.image_url = request.form['image_url']

    db.session.add(user)
    db.session.commit()

    return redirect("/users")


#ROUTE to DELETE USER 

@app.route('/users/<int:user_id>/delete')
def delete_user(user_id):

    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()

    return redirect('/users')


####################  POST ROUTE  #######################



@app.route('/users/<int:user_id>/posts/new')
def posts_new_form(user_id):
    """Show a form to create a new post for a specific user"""

    user = User.query.get_or_404(user_id)
    return render_template('posts/new.html', user=user)


@app.route('/users/<int:user_id>/posts/new', methods=["POST"])
def posts_new(user_id):
    """Handle form submission for creating a new post for a specific user"""

    user = User.query.get_or_404(user_id)
    new_post = Post(title=request.form['title'],
                    content=request.form['content'],
                    user=user)

    db.session.add(new_post)
    db.session.commit()
    flash(f"Post '{new_post.title}' added.")

    return redirect(f"/users/{user_id}")


@app.route('/posts/<int:post_id>')
def posts_show(post_id):
    """Show a page with info on a specific post"""

    post = Post.query.get_or_404(post_id)
    return render_template('posts/show.html', post=post)


@app.route('/posts/<int:post_id>/edit')
def posts_edit(post_id):
    """Show a form to edit an existing post"""

    post = Post.query.get_or_404(post_id)
    return render_template('posts/edit.html', post=post)


@app.route('/posts/<int:post_id>/edit', methods=["POST"])
def posts_update(post_id):
    """Handle form submission for updating an existing post"""

    post = Post.query.get_or_404(post_id)
    post.title = request.form['title']
    post.content = request.form['content']

    db.session.add(post)
    db.session.commit()
    flash(f"Post '{post.title}' edited.")

    return redirect(f"/users/{post.user_id}")


@app.route('/posts/<int:post_id>/delete', methods=["POST"])
def posts_destroy(post_id):
    """Handle form submission for deleting an existing post"""

    post = Post.query.get_or_404(post_id)

    db.session.delete(post)
    db.session.commit()
    flash(f"Post '{post.title} deleted.")

    return redirect(f"/users/{post.user_id}")