from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

app = Flask(__name__)

# Construction de l'URI de connexion à la base de données PostgreSQL à partir des variables d'environnement
app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Désactive le suivi des modifications inutiles

# Initialisation de SQLAlchemy
db = SQLAlchemy(app)

# Définir les modèles pour les tables
class Recipe(db.Model):
    __tablename__ = 'recipes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)

    # Relation avec les ingrédients
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

@app.route('/')
def index():
    # Récupérer toutes les recettes depuis la base de données
    recipes = Recipe.query.all()
    return render_template('index.html', recipes=recipes)

@app.route('/<int:recipe_id>')
def recipe_detail(recipe_id):
    # Récupérer la recette par son ID
    recipe = Recipe.query.get(recipe_id)
    if recipe:
        ingredients = recipe.ingredients  # Accès direct aux ingrédients via la relation
        steps = Step.query.filter_by(recipe_id=recipe_id).order_by(Step.step_order).all()
        return render_template('recipe.html', recipe=recipe, ingredients=ingredients, steps=steps)
    else:
        return render_template('index.html', recipes=Recipe.query.all())

if __name__ == '__main__':
    # Utiliser le contexte de l'application pour créer les tables
    with app.app_context():
        db.create_all()  # Crée toutes les tables si elles n'existent pas déjà
    app.run(debug=True)
