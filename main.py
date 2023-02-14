import threading
# import "packages" from flask
from flask import render_template

# import "packages" from "this" project
from __init__ import app  # Definitions initialization
from model.jokes import initJokes
from model.users import initUsers
from model.cars import initCars
from model.generaters import initfact
from model.facts import initFacts

# setup APIs
from api.joke import joke_api # Blueprint import api definition
from api.user import user_api # Blueprint import api definition
from api.car import car_api
from api.generate import generate_api
from api.fact import fact_api

# setup App pages
from projects.projects import app_projects # Blueprint directory import projects definition

# register URIs
app.register_blueprint(joke_api) # register api routes

app.register_blueprint(user_api) # register api routes
app.register_blueprint(app_projects) # register app pages
app.register_blueprint(car_api)
app.register_blueprint(generate_api)
app.register_blueprint(fact_api)

@app.errorhandler(404)  # catch for URL not found
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

@app.route('/')  # connects default URL to index() function
def index():
    return render_template("index.html")

@app.route('/stub/')  # connects /stub/ URL to stub() function
def stub():
    return render_template("stub.html")

@app.before_first_request
def activate_job():
    initJokes()
    initUsers()
    initCars()
    initfact()
    initFacts()

# this runs the application on the development server
if __name__ == "__main__":
    # change name for testing
    from flask_cors import CORS
    cors = CORS(app)
    app.run(debug=True, host="0.0.0.0", port="8086")