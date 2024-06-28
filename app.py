from flask import Flask ,render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route('/jovlin')
def jovlin():
    return render_template('home.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
