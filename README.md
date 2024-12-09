
# Ice Cream Parlor Application


This is a simple Flask-based application for a Ice Cream Parlor Cafe that uses SQLite to manage:

- Seasonal flavor offerings
- Ingredient inventory
- Customer flavor suggestions and allergy concerns

### Features
- Users can **add to cart** and **view cart** items.
- Users can **suggest new flavors**.
- Users can **add allergens** to flavors.
- Simple **frontend** to interact with the API.

## Prerequisites

Before running the application, make sure you have the following installed:

- Python 3.6+
- SQLite (Python comes with SQLite support by default)

## Installation
1. Clone the repository:
```bash
git clone https://github.com/vishnupriyasri/ice_cream_parlor.git
cd ice-cream-parlor
```
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```
3. Initialize the SQLite database:
```bash
python run.py
```
This will create the necessary tables in the SQLite database

## Project Structure

```
/project-directory
    /static
        /styles.css
        /app.js
    /templates
        index.html
    run.py
    requirements.txt
```
- ```/static:``` Contains static files like CSS, JavaScript, and images.
- ```/templates:``` Contains HTML templates (e.g., index.html).
- ```run.py:``` Main Flask application script that runs the app and handles API endpoints.
- ```requirements.txt:``` Lists all required Python packages.

## Running the Application

To run the application locally, use the following command:

```
python run.py

```
Once the app is running, visit http://127.0.0.1:5000/ in your web browser to access the frontend. You can also interact with the application through the API.

## Frontend

The frontend for the application is a simple HTML page (index.html) that allows users to interact with the API. It uses basic JavaScript to send requests to the Flask backend.

1. Open the application in a browser (http://127.0.0.1:5000/).
2. Use the frontend to add flavors to the cart, view the cart, and add suggestions.

## Postman Collection

The above project has postman collection where it is added to the project in the name of **IceCream.postman_collection.json**.

## Conclusion
This application demonstrates how to use Flask with SQLite to manage an ice cream parlor's offerings, ingredients, and customer interactions. 