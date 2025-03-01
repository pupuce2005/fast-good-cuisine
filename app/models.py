from app.database import db

class Recipe(db.Model):
    __tablename__ = 'recipes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    cooking_time = db.Column(db.Integer)
    category = db.Column(db.String(255))
    ratings = db.Column(db.Integer)
    image_url = db.Column(db.String(255))
    ingredients = db.relationship('RecipeIngredient', backref='recipe', lazy=True)
    steps = db.relationship('Step', backref='recipe', lazy=True)

class Ingredient(db.Model):
    __tablename__ = 'ingredients'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)

class Unit(db.Model):
    __tablename__ = 'units'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)

class RecipeIngredient(db.Model):
    __tablename__ = 'recipe_ingredients'
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'), primary_key=True)
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredients.id'), primary_key=True)
    unit_id = db.Column(db.Integer, db.ForeignKey('units.id'), nullable=False)
    quantity = db.Column(db.Integer)
    ingredient = db.relationship('Ingredient', backref='RecipeIngredient', lazy=True)
    unit = db.relationship('Unit', backref='RecipeIngredient', lazy=True)

class Step(db.Model):
    __tablename__ = 'steps'
    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'), nullable=False)
    step_order = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)
