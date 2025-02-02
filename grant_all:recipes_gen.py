import os
import json

recipes_path = os.path.join(os.getcwd(), 'recipe')

def extract_recipes(recipes_path):
    recipes = []

    for root, dirs, files in os.walk(recipes_path):
        for file in files:
            if file.endswith(".json"):
                recipe_id = os.path.splitext(file)[0]
                recipes.append(recipe_id)

    return recipes

def generate_mcfunction_file(recipes, output_path):
    with open(output_path, 'w') as file:
        for recipe in recipes:
            file.write(f"recipe give @a minecraft:{recipe}\n")

if __name__ == "__main__":
    if not os.path.exists(recipes_path):
        print(f"Recipe directory not found: {recipes_path}")
    else:
        recipes = extract_recipes(recipes_path)
        if not recipes:
            print("No recipes found.")
        else:
            output_file_path = os.path.join(os.getcwd(), "grant_all_recipes.mcfunction")
            generate_mcfunction_file(recipes, output_file_path)
            print("mcfunction file generated successfully.")
