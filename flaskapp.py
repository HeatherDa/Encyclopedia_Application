from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('webpage.html')

@app.route('/login', methods=['GET', 'POST'])
def loginRoute():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        inputValues = request.get_data()
        return str(inputValues)

@app.route('/signup')
def signupRoute():
    return render_template('signup.html')

if __name__ == '__main__':
   app.run(debug = True)