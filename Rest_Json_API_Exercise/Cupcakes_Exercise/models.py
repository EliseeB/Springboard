from flask_sqlalchemy import SQLAlchemy

# Initialize SQLAlchemy
db = SQLAlchemy()

# Default image URL for cupcakes
DEFAULT_IMAGE = "https://thestayathomechef.com/wp-content/uploads/2017/12/Most-Amazing-Chocolate-Cupcakes-1-small.jpg"

class Cupcake(db.Model):
    """Cupcake model for storing cupcake details."""
    
    # Define the table name in the database
    __tablename__ = "cupcakes"
    
    # Define the columns in the cupcakes table
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    flavor = db.Column(db.Text, nullable=False)
    size = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    image = db.Column(db.Text, nullable=False, default=DEFAULT_IMAGE)

    def to_dict(self):
        """Serialize cupcake to a dictionary of cupcake info."""
        return {
            "id": self.id,
            "flavor": self.flavor,
            "rating": self.rating,
            "size": self.size,
            "image": self.image or DEFAULT_IMAGE  # Use default image if none provided
        }

def connect_db(app):
    """Connect this database to provided Flask app."""
    db.app = app
    db.init_app(app)