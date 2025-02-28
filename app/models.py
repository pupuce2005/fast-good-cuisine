from app.database import db

class Recipe(db.Model):
    __tablename__ = 'recipes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    ingredients = db.relationship('Ingredient', secondary='recipe_ingredients', backref=db.backref('recipes'))
    steps = db.relationship('Step', backref='recipe', lazy=True)

class Ingredient(db.Model):
    __tablename__ = 'ingredients'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    quantity = db.Column(db.Float)
    unit = db.Column(db.String(255))

class RecipeIngredient(db.Model):
    __tablename__ = 'recipe_ingredients'
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'), primary_key=True)
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredients.id'), primary_key=True)

class Step(db.Model):
    __tablename__ = 'steps'
    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'), nullable=False)
    step_order = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)
