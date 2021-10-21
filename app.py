
from flask import Flask

# create a Flask Application labeled "app"
app = Flask(__name__)

# create a welcome route
@app.route('/')
def Hello_World():
    return 'Hello World!'