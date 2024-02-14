from flask import Flask, render_template, request
from weather import translate_to_inclusive
from waitress import serve

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
@app.route('/weather')
def get_weather():
    inputt = request.args.get('input')
    output = translate_to_inclusive(inputt)
    return render_template(
        "weather.html",
        inputt=inputt,
        title=output,
    )

if __name__ == "__main__" :
    serve(app, host="0.0.0.0", port=8000)
