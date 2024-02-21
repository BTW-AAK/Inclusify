from flask import Flask, render_template, request
from weather import translate_to_inclusive
from waitress import serve

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('translate.html')
@app.route('/translate')
def get_weather():
    inputt = request.args.get('input')
    output = translate_to_inclusive(inputt)
    Qualification = request.args.get('Qualifications')

    return render_template(
        "translated.html",
        inputt=inputt,
        title=output,
        Qualification = Qualification,

    )

if __name__ == "__main__" :
    # serve(app, host="0.0.0.0", port=8000)
    app.run(debug=True, port=8001)