from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def weather():
    city = request.form['city']
    return render_template('weather.html', city = city)

if __name__ == "__main__":
    app.run(debug = True)
