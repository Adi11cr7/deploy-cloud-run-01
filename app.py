from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World, deploying service using githup action! Trigered by commit 2"

if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
