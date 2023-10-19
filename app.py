from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
    return '<h1 style="color: blue;">Sucessfully deploy application with the help of Argonaut</h1><p>Version 1</p>'
if __name__ == '__main__':
  app.run()
