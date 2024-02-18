from flask import Flask, render_template, request
from weather import translate_to_inclusive, analysis
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///analysis.db'

db = SQLAlchemy(app)

#createmodel
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    typeofnonI = db.Column(db.String(200), nullable=True)
    mostUsedN = db.Column(db.String(200), nullable=True)
    mostUsedI = db.Column(db.String(200), nullable=True)

@app.route('/')
@app.route('/onboarding')
def onboarding():
    return render_template('onboarding.html')

@app.route('/login')
def startLogin():
    return render_template('login.html')

@app.route('/signup')
def startSignup():
    return render_template('signup.html')

@app.route('/translate-home')
def index():
    return render_template('translate.html')

@app.route('/translate')
def get_weather():
    inputt = request.args.get('input')
    tone = request.args.get('tone')
    output = translate_to_inclusive(inputt,tone)


    json_analysis = analysis(inputt)
    user = Users(typeofnonI=json_analysis['TypeNL'], mostUsedN=json_analysis['UsedN'], mostUsedI=json_analysis['UsedI'])
    db.session.add(user)
    db.session.commit()


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