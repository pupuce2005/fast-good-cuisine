from flask import Blueprint, render_template
from app.models import Recipe, Step

main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/')
def index():
    recipes = Recipe.query.all()
    return render_template('index.html', recipes=recipes)

@main_blueprint.route('/<int:recipe_id>')
def recipe_detail(recipe_id):
    recipe = Recipe.query.get(recipe_id)
    if recipe:
        ingredients = recipe.ingredients
        steps = Step.query.filter_by(recipe_id=recipe_id).order_by(Step.step_order).all()
        return render_template('recipe.html', recipe=recipe, ingredients=ingredients, steps=steps)
    return render_template('index.html', recipes=Recipe.query.all())
