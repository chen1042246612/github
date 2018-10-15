from flask import Flask
from flask_script import Manager

app = Flask(__name__)

manage = Manager(app)

@app.route('/')
def index():
    return '123'

if __name__ == '__main__':
    manage.run()
