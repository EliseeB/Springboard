from flask import Flask, render_template, redirect, url_for
from models import db, connect_db, Pet
from forms import AddPetForm
from flask_debugtoolbar import DebugToolbarExtension

# Initialize Flask app
app = Flask(__name__)

# Set configuration variables
app.config['SECRET_KEY'] = 'SEK'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_adoption'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_ECHO'] = True
app.debug = True

# Initialize debug toolbar
toolbar = DebugToolbarExtension(app)

# Connect to the database
connect_db(app)

# Create all tables in the database
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    """
    Home route that displays all pets available for adoption.
    
    Returns:
        Rendered template for the home page.
    """
    pets = Pet.query.all()
    return render_template('index.html', pets=pets)

@app.route('/new', methods=['GET', 'POST'])
def add_pet():
    """
    Route to add a new pet. Displays a form and handles form submission.
    
    Returns:
        Rendered template for the form to add a new pet if the form is not valid or has not been submitted.
        Redirect to the home page if the form is valid and has been submitted.
    """
    form = AddPetForm()

    if form.validate_on_submit():
        # Create a new Pet object with data from the form
        pet = Pet(
            name=form.name.data,
            species=form.species.data,
            photo_url=form.photo_url.data,
            age=form.age.data,
            notes=form.note.data,
            available=form.available.data == 'True'
        )
        
        # Add the new pet to the session and commit the session to the database
        db.session.add(pet)
        db.session.commit()

        # Redirect to the home page
        return redirect(url_for('index'))

    else:
        # Render the form to add a new pet
        return render_template('addPetForm.html', form=form)

@app.route('/<int:id>')
def pet_profile(id):
    """
    Route to display a pet's profile.
    
    Args:
        id (int): The id of the pet.
    
    Returns:
        Rendered template for the pet's profile.
    """
    pet = Pet.query.get_or_404(id)
    return render_template('petDetails.html', pet=pet)

@app.route('/<int:id>/edit', methods=['GET', 'POST'])
def edit_pet(id):
    """
    Route to edit a pet's details. Displays a form and handles form submission.
    
    Args:
        id (int): The id of the pet.
    
    Returns:
        Rendered template for the form to edit the pet's details if the form is not valid or has not been submitted.
        Redirect to the home page if the form is valid and has been submitted.
    """
    form = AddPetForm()
    pet = Pet.query.get_or_404(id)

    if form.validate_on_submit():
        # Update the pet's details with data from the form
        pet.name = form.name.data
        pet.species = form.species.data
        pet.age = form.age.data
        pet.photo_url = form.photo_url.data
        pet.note = form.note.data
        pet.available = form.available.data == 'True'

        # Commit the session to the database to save the changes
        db.session.commit()

        # Redirect to the home page
        return redirect(url_for('index'))

    else:
        # Populate the form with the pet's current details
        form.name.data = pet.name
        form.species.data = pet.species
        form.age.data = pet.age
        form.photo_url.data = pet.photo_url
        form.note.data = pet.notes
        form.available.data = pet.available

        # Render the form to edit the pet's details
        return render_template('editPetForm.html', pet=pet, form=form)
