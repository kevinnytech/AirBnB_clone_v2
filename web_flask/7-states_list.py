#!/usr/bin/python3
"""
The script that starts a Flask web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)

@app.route('/states_list', strict_slashes=False)
def states_list():
    """displays a HTML page with all states listed in alphabetical order"""
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """close the database on teardown"""
    storage.close()



if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
