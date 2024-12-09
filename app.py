from flask import Flask
from database import create_tables

app = Flask(__name__)

create_tables()

from run import *

if __name__ == '__main__':
    app.run(debug=True)
