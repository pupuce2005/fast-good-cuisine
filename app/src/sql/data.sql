-- Insérer les recettes
INSERT INTO recipes (name, description,cooking_time,category,ratings,image_url) VALUES
    ('Spaghetti Carbonara', 'Une recette classique de pâtes avec lardons, crème et parmesan.', 20, 'Pâtes', 4, 'patescarbonara.jpg'),
    ('Salade César', 'Salade composée avec poulet, laitue, croutons et sauce César.', 30, 'Salades', 2, 'saladecesar.jpg')
RETURNING id;

-- Insérer les ingrédients avec quantités et unités (ajuster les quantités et unités si nécessaire)
INSERT INTO ingredients (name) VALUES
    ('Spaghetti'),
    ('Lardons'),
    ('Crème'),
    ('Parmesan'),
    ('Laitue'),
    ('Poulet'),
    ('Croutons'),
    ('Sauce César'),
    ('Oeuf')
ON CONFLICT (name) DO NOTHING
RETURNING id, name;

INSERT INTO units (name) VALUES
    ('g'),
    ('ml'),
    ('pcs')
RETURNING id, name;

-- Associer les ingrédients aux recettes avec des SELECT
INSERT INTO recipe_ingredients (recipe_id, ingredient_id, unit_id, quantity)
SELECT r.id, i.id, u.id, 400 FROM recipes r, ingredients i, units u WHERE r.name = 'Spaghetti Carbonara' AND i.name = 'spaghetti' AND u.name = 'g'
UNION ALL
SELECT r.id, i.id, u.id, 150 FROM recipes r, ingredients i, units u WHERE r.name = 'Spaghetti Carbonara' AND i.name = 'lardons' AND u.name = 'g'
UNION ALL
SELECT r.id, i.id, u.id, 200 FROM recipes r, ingredients i, units u WHERE r.name = 'Spaghetti Carbonara' AND i.name = 'crème' AND u.name = 'ml'
UNION ALL
SELECT r.id, i.id, u.id, 50 FROM recipes r, ingredients i, units u WHERE r.name = 'Spaghetti Carbonara' AND i.name = 'parmesan' AND u.name = 'g'
UNION ALL
SELECT r.id, i.id, u.id, 1 FROM recipes r, ingredients i, units u WHERE r.name = 'Salade César' AND i.name = 'laitue' AND u.name = 'pcs'
UNION ALL
SELECT r.id, i.id, u.id, 200 FROM recipes r, ingredients i, units u WHERE r.name = 'Salade César' AND i.name = 'poulet' AND u.name = 'g'
UNION ALL
SELECT r.id, i.id, u.id, 50 FROM recipes r, ingredients i, units u WHERE r.name = 'Salade César' AND i.name = 'croutons' AND u.name = 'g'
UNION ALL
SELECT r.id, i.id, u.id, 30 FROM recipes r, ingredients i, units u WHERE r.name = 'Salade César' AND i.name = 'sauce César' AND u.name = 'ml'
UNION ALL
SELECT r.id, i.id, u.id, 2 FROM recipes r, ingredients i, units u WHERE r.name = 'Spaghetti Carbonara' AND i.name = 'oeuf' AND u.name = 'pcs'
RETURNING recipe_id, ingredient_id;


-- Insérer les étapes
INSERT INTO steps (recipe_id, step_order, description)
SELECT r.id, 1, 'Faire cuire les pâtes' FROM recipes r WHERE r.name = 'Spaghetti Carbonara'
UNION ALL
SELECT r.id, 2, 'Faire revenir les lardons' FROM recipes r WHERE r.name = 'Spaghetti Carbonara'
UNION ALL
SELECT r.id, 3, 'Mélanger avec la crème et le parmesan' FROM recipes r WHERE r.name = 'Spaghetti Carbonara'
UNION ALL
SELECT r.id, 1, 'Cuire le poulet' FROM recipes r WHERE r.name = 'Salade César'
UNION ALL
SELECT r.id, 2, 'Mélanger les ingrédients' FROM recipes r WHERE r.name = 'Salade César'
UNION ALL
SELECT r.id, 3, 'Ajouter la sauce' FROM recipes r WHERE r.name = 'Salade César';
