from flask import Blueprint, render_template, request, redirect
from app.models import Recipe, Step,Unit,Ingredient, RecipeIngredient, db
from PIL import Image
import os

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

@main_blueprint.route('/edit/<int:recipe_id>')
def recipe_edit(recipe_id):
    recipe = Recipe.query.get(recipe_id)
    if recipe:
        ingredients = recipe.ingredients
        steps = Step.query.filter_by(recipe_id=recipe_id).order_by(Step.step_order).all()
        return render_template('edit.html', recipe=recipe, ingredients=ingredients, steps=steps)
    return render_template('index.html', recipes=Recipe.query.all())

@main_blueprint.route('/update/<int:recipe_id>', methods=['POST'])
def recipe_update(recipe_id):
    recipe = Recipe.query.get(recipe_id)
    
    if recipe:
        recipe.name = request.form['title']
        recipe.description = request.form['description']
        recipe.cooking_time = request.form['cooking_time']
        recipe.category = request.form['category']
        recipe.ratings = request.form['ratings']
        
        db.session.commit()

        ingredients = recipe.ingredients
        steps = Step.query.filter_by(recipe_id=recipe_id).order_by(Step.step_order).all()

        return redirect(f'/edit/{recipe_id}')

    return redirect('/')


@main_blueprint.route('/update-img/<int:recipe_id>', methods=['POST'])
def recipe_update_img(recipe_id):
    recipe = Recipe.query.get(recipe_id)

    image = request.files.get("image")
    img = Image.open(image)

    size = min(img.size)
    left = (img.size[0] - size) / 2
    top = (img.size[1] - size) / 2
    right = (img.size[0] + size) / 2
    bottom = (img.size[1] + size) / 2

    img = img.crop((left, top, right, bottom))
    img = img.resize((500, 500))
    img.save(os.path.join('app/static/image/', image.filename))

    if recipe:
        recipe.image_url = image.filename        
        db.session.commit()
        return redirect(f'/edit/{recipe_id}')
    return redirect('/')

@main_blueprint.route('/delete-recipe-ingredient/<int:recipe_id>/<int:ingredient_id>', methods=['POST']) 
def delete_ingredient(recipe_id, ingredient_id):
    # Cherche l'ingrédient dans la table `RecipeIngredient` avec la clé primaire composée
    ingredient = RecipeIngredient.query.filter_by(recipe_id=recipe_id, ingredient_id=ingredient_id).first()
    if ingredient:
        db.session.delete(ingredient)
        db.session.commit()
    return redirect('/')

@main_blueprint.route('/edit-recipe-ingredient/<int:recipe_id>/<int:ingredient_id>', methods=['POST', 'GET'])
def edit_ingredient(recipe_id, ingredient_id):
    recipeingredient = RecipeIngredient.query.filter_by(recipe_id=recipe_id, ingredient_id=ingredient_id).first()
    ingredient = recipeingredient.ingredient
    unit = recipeingredient.unit
    if recipeingredient:
        return render_template('edit-recipe-ingredient.html', recipe_id=recipe_id, ingredient_id=ingredient_id, recipeingredient=recipeingredient , ingredient=ingredient, unit=unit, allunits=Unit.query.all(), allingredients=Ingredient.query.all()) # TODO: Ne pas envoyé les ingrédients qui sont déjà dans la recette
    return redirect('/')

@main_blueprint.route('/update-recipe-ingredient/<int:recipe_id>/<int:ingredient_id>', methods=['POST'])
def update_ingredient(recipe_id, ingredient_id):
    recipeingredient = RecipeIngredient.query.filter_by(recipe_id=recipe_id, ingredient_id=ingredient_id).first()
    if recipeingredient:
        ingredient = Ingredient.query.filter_by(name=request.form['ingredient']).first()
        recipeingredient.ingredient_id = ingredient.id
        recipeingredient.quantity = request.form['quantity']
        recipeingredient.unit_id = request.form['unit']
        db.session.commit()
    return redirect(f'/edit/{recipe_id}')

@main_blueprint.route('/update-recipe-ingredient/<int:recipe_id>', methods=['POST'])
def update_for_add_ingredient(recipe_id):
    recipeingredient = RecipeIngredient()
    recipeingredient.recipe_id = recipe_id
    ingredient = Ingredient.query.filter_by(name=request.form['ingredient']).first()
    recipeingredient.ingredient_id = ingredient.id
    recipeingredient.quantity = request.form['quantity']
    recipeingredient.unit_id = request.form['unit']
    db.session.add(recipeingredient)
    db.session.commit()
    return redirect(f'/edit/{recipe_id}')

@main_blueprint.route('/add-ingredient/<int:recipe_id>/<int:ingredient_id>', methods=['POST']) # TODO: le faire en javascript
def add_ingredient(recipe_id, ingredient_id):
    where = request.form['where']
    ingredient_name = request.form['name']
    db.session.add(Ingredient(name=ingredient_name))
    db.session.commit()
    if where == 'edit':
        return redirect(f'/edit-recipe-ingredient/{recipe_id}/{ingredient_id}')
    return redirect(f'/add-recipe-ingredient/{recipe_id}')

@main_blueprint.route('/add-recipe-ingredient/<int:recipe_id>', methods=['POST', 'GET'])
def add_recipe_ingredient(recipe_id):
    return render_template('add-recipe-ingredient.html', recipe_id=recipe_id, allunits=Unit.query.all(), allingredients=Ingredient.query.all())