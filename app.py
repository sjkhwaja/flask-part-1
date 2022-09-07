### import package
from flask import Flask


### define app using flask instance
app = Flask(__name__)


### main index
@app.route('/')
def hello_world():
    return 'Hello world, WWW!'


### repeat for pages 2 & 3
@app.route('/dashboard')
def dashboard():
    return 'This is my dashboard!'

@app.route('/about')
def about():
    return 'This is the about page!'

  
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
