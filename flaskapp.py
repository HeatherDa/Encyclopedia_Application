from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('webpage.html')

@app.route('/login')
def loginRoute():
    return render_template('login.html')

if __name__ == '__main__':
   app.run(debug = True)