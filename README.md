# Create environment
python - m venv venv
# Install django
pip install django
# Migrate
python manage.py migrate
# Create admin login + password
python manage.py createsuperuser
# Run server for tests
python manage.py runserver
# To test the functionality of adding a product to a recipe
GET -> http://localhost:8000/recipes/add_product_to_recipe/?recipe_id=1&product_id=1&weight=200
# To test the recipe preparation functionality
GET -> http://localhost:8000/recipes/cook_recipe/?recipe_id=1
# To test the functionality of displaying recipes without a specific product
GET -> http://localhost:8000/recipes/show_recipes_without_product/?product_id=1
# Admin
http://localhost:8000/admin/
