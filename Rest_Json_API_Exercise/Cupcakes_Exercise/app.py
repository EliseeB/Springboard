
from flask import Flask, request, jsonify, render_template
from models import db, connect_db, Cupcake

# Initialize Flask app
app = Flask(__name__)

# Configure app settings
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "oh-so-secret"

# Connect to the database
connect_db(app)

# Route for the homepage
@app.route("/")
def root():
    """Render homepage."""
    return render_template("index.html")

# Route to list all cupcakes
@app.route("/api/cupcakes")
def list_cupcakes():
    """Return all cupcakes in system as JSON."""
    cupcakes = [cupcake.to_dict() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes=cupcakes)

# Route to create a new cupcake
@app.route("/api/cupcakes", methods=["POST"])
def create_cupcake():
    """Add cupcake and return data about the new cupcake as JSON."""
    data = request.json
    cupcake = Cupcake(
        flavor=data.get('flavor'),
        rating=data.get('rating'),
        size=data.get('size'),
        image=data.get('image', None) 
    )
    db.session.add(cupcake)
    db.session.commit()
    return jsonify(cupcake=cupcake.to_dict()), 201  # Return HTTP status code 201 for CREATED

# Route to get a specific cupcake by ID
@app.route("/api/cupcakes/<int:cupcake_id>")
def get_cupcake(cupcake_id):
    """Return data on a specific cupcake as JSON."""
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    return jsonify(cupcake=cupcake.to_dict())

# Route to update an existing cupcake by ID
@app.route("/api/cupcakes/<int:cupcake_id>", methods=["PATCH"])
def update_cupcake(cupcake_id):
    """Update cupcake from request data and return updated data as JSON."""
    data = request.json
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    # Update cupcake attributes if provided in the request
    cupcake.flavor = data.get('flavor', cupcake.flavor)
    cupcake.rating = data.get('rating', cupcake.rating)
    cupcake.size = data.get('size', cupcake.size)
    cupcake.image = data.get('image', cupcake.image)
    db.session.commit()
    return jsonify(cupcake=cupcake.to_dict())

# Route to delete a cupcake by ID
@app.route("/api/cupcakes/<int:cupcake_id>", methods=["DELETE"])
def remove_cupcake(cupcake_id):
    """Delete cupcake and return a confirmation message as JSON."""
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message="Deleted")

# Check if the script is executed directly and run the app
if __name__ == "__main__":
    app.run()
