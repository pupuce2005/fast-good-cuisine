CREATE DATABASE fastgoodcuisine
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LOCALE_PROVIDER = 'libc'
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;
    
CREATE TABLE recipes (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    cooking_time INT,
    category VARCHAR(255),
    ratings INT DEFAULT 0,
    image_url VARCHAR(255)
);

CREATE TABLE ingredients (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE units (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE recipe_ingredients (
    recipe_id INT REFERENCES recipes(id) ON DELETE CASCADE,
    ingredient_id INT REFERENCES ingredients(id) ON DELETE CASCADE,
    unit_id INT REFERENCES units(id),
    quantity INT NOT NULL,
    PRIMARY KEY (recipe_id, ingredient_id)
);

CREATE TABLE steps (
    id SERIAL PRIMARY KEY,
    recipe_id INT REFERENCES recipes(id) ON DELETE CASCADE,
    step_order INT NOT NULL,
    description TEXT NOT NULL
);
