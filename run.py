from flask import Flask, request, jsonify
from flask import Flask, render_template, send_from_directory
from database import *

app = Flask(__name__)

create_tables()

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/add_user', methods=['POST'])
def add_user_route():
    name = request.json.get('name')
    email = request.json.get('email')
    response = add_user(name, email)
    return jsonify(response)

@app.route('/get_users', methods=['GET'])
def get_users_route():
    users = get_users()
    return jsonify([{"id": user[0], "name": user[1], "email": user[2], "created_at": user[3]} for user in users])

@app.route('/delete_user', methods=['DELETE'])
def delete_user_route():
    user_id = request.json.get('user_id')
    response = delete_user(user_id)
    return jsonify(response)

@app.route('/add_flavor', methods=['POST'])
def add_flavor_route():
    name = request.json.get('name')
    description = request.json.get('description')
    seasonal = request.json.get('seasonal')
    add_flavor(name, description, seasonal)
    return jsonify({"message": "Flavor added successfully!"})

@app.route('/get_flavors', methods=['GET'])
def get_flavors_route():
    flavors = get_flavors()
    return jsonify([{"id": flavor[0], "name": flavor[1], "description": flavor[2], "seasonal": flavor[3]} for flavor in flavors])

@app.route('/filter_flavors', methods=['GET'])
def filter_flavors_route():
    seasonal = request.args.get('seasonal', 'true') == 'true'
    flavors = filter_flavors(seasonal)
    return jsonify([{"id": flavor[0], "name": flavor[1], "description": flavor[2], "seasonal": flavor[3]} for flavor in flavors])

@app.route('/search_flavor', methods=['GET'])
def search_flavor_route():
    name = request.args.get('name')
    flavors = search_flavor(name)
    return jsonify([{"id": flavor[0], "name": flavor[1], "description": flavor[2], "seasonal": flavor[3]} for flavor in flavors])

@app.route('/add_ingredient', methods=['POST'])
def add_ingredient_route():
    name = request.json.get('name')
    allergy_concerns = request.json.get('allergy_concerns')
    add_ingredient(name, allergy_concerns)
    return jsonify({"message": "Ingredient added successfully!"})

@app.route('/get_ingredients', methods=['GET'])
def get_ingredients_route():
    ingredients = get_ingredients()
    return jsonify([{"id": ingredient[0], "name": ingredient[1], "allergy_concerns": ingredient[2]} for ingredient in ingredients])

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart_route():
    user_id = request.json.get('user_id')
    flavor_id = request.json.get('flavor_id')
    add_to_cart(user_id, flavor_id)
    return jsonify({"message": "Added to cart successfully!"})

@app.route('/get_cart', methods=['GET'])
def get_cart_route():
    user_id = request.args.get('user_id')
    cart_items = get_cart(user_id)
    return jsonify([item[0] for item in cart_items])

@app.route('/add_suggestion', methods=['POST'])
def add_suggestion_route():
    user_id = request.json.get('user_id')
    suggestion = request.json.get('suggestion')
    add_suggestion(user_id, suggestion)
    return jsonify({"message": "Suggestion added successfully!"})

if __name__ == '__main__':
    app.run(debug=True)
