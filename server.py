from flask import Flask, render_template, request
from weather import translate_to_inclusive
from waitress import serve

app = Flask(__name__)
@app.route('/')
@app.route('/login')
def startLogin():
    return render_template('login.html')

@app.route('/translate')
def index():
    return render_template('translate.html')

@app.route('/translate')
def get_weather():
    inputt = request.args.get('input')
    tone = request.args.get('tone')
    output = translate_to_inclusive(inputt,tone)
    return render_template(
        "translated.html",
        inputt=inputt,
        title=output,
    )

@app.route('/analytics')
def analytics():
    return render_template('analytics.html')

if __name__ == "__main__" :
    # serve(app, host="0.0.0.0", port=8000)
    app.run()