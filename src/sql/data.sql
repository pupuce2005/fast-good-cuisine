-- Insérer les recettes
INSERT INTO recipes (name, description) VALUES
    ('Spaghetti Carbonara', 'Une recette classique de pâtes avec lardons, crème et parmesan.'),
    ('Salade César', 'Salade composée avec poulet, laitue, croutons et sauce César.')
RETURNING id;

-- Insérer les ingrédients avec quantités et unités (ajuster les quantités et unités si nécessaire)
INSERT INTO ingredients (name, quantity, unit) VALUES
    ('spaghetti', 100, 'g'),
    ('lardons', 150, 'g'),
    ('crème', 200, 'ml'),
    ('parmesan', 50, 'g'),
    ('laitue', 1, 'tête'),
    ('poulet', 200, 'g'),
    ('croutons', 50, 'g'),
    ('sauce César', 30, 'ml')
ON CONFLICT (name) DO NOTHING
RETURNING id, name;

-- Associer les ingrédients aux recettes
INSERT INTO recipe_ingredients (recipe_id, ingredient_id)
SELECT r.id, i.id
FROM recipes r
JOIN ingredients i ON i.name IN ('spaghetti', 'lardons', 'crème', 'parmesan')
WHERE r.name = 'Spaghetti Carbonara';

INSERT INTO recipe_ingredients (recipe_id, ingredient_id)
SELECT r.id, i.id
FROM recipes r
JOIN ingredients i ON i.name IN ('laitue', 'poulet', 'croutons', 'parmesan', 'sauce César')
WHERE r.name = 'Salade César';

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
