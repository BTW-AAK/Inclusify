from flask import Flask, render_template, request
from weather import translate_to_inclusive
from waitress import serve

app = Flask(__name__)
@app.route('/')
def onboarding():
    return render_template('onboarding.html')

@app.route('/studentLogin')
def StudentLogin():
    return render_template('studentlogin.html')

@app.route('/teacherLogin')
def TeacherLogin():
    return render_template('teacherlogin.html')


@app.route('/scheduling')
def index():
    return render_template('translate.html')
@app.route('/translate')
def get_weather():
    inputt = request.args.get('input')
    output = translate_to_inclusive(inputt)
    Qualification = request.args.get('Qualifications')
    name = request.args.get('name')
    email = request.args.get('email')
    tips = request.args.get('tips')
    category = request.args.get('category')

    return render_template(
        "translated.html",
        inputt=inputt,
        title=output,
        Qualification = Qualification,
        name = name,
        email = email, 
        tips = tips, 
         category = category, 
    )

@app.route('/Teacherend')
def submittedSchedule():
    return render_template('Teacherend.html')


@app.route('/Calendar')
def calendar():
    return render_template('calendar.html')

if __name__ == "__main__" :
    # serve(app, host="0.0.0.0", port=8000)
    app.run(debug=True, port=8001)