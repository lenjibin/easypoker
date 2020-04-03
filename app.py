import os

from flask import Flask


# create and configure the app
app = Flask(__name__)

# a simple page that says hello
@app.route('/hello')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
