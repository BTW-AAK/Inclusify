from flask import Flask, render_template, request
from weather import translate_to_inclusive, analysis
from flask_sqlalchemy import SQLAlchemy
import plotly
import plotly.express as px
import json
from collections import Counter
from sqlalchemy import DateTime
from datetime import datetime
from flask_migrate import Migrate
from sqlalchemy import func



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///analysis.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

#createmodel
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    typeofnonI = db.Column(db.String(200), nullable=True)
    mostUsedN = db.Column(db.String(200), nullable=True)
    mostUsedI = db.Column(db.String(200), nullable=True)
    timestamp = db.Column(DateTime, default=datetime.utcnow)


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

    timestamp = datetime.utcnow()

    json_analysis = analysis(inputt)
    user = Users(typeofnonI=json_analysis['TypeNL'], mostUsedN=json_analysis['UsedN'], mostUsedI=json_analysis['UsedI'], timestamp=timestamp)
    db.session.add(user)
    db.session.commit()


    return render_template(
        "translated.html",
        inputt=inputt,
        title=output,
    )


@app.route('/analytics')
def analytics():
    data = db.session.query(Users.typeofnonI, db.func.count().label('count')).group_by(Users.typeofnonI).all()

    types, counts = zip(*data)

    fig = px.pie(names=types, values=counts, title='Distribution of Type of Non Inclusive Language Used',
                 custom_data=[types, counts], labels={'names': 'Type'}, )
    fig.update_layout({
        'plot_bgcolor': 'rgba(0,0,0,0)',
        'paper_bgcolor': 'rgba(0,0,0,0)'
    })

    plot_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)


    #!THE 5 WORTD THING WORKED
    data = db.session.query(Users.mostUsedN).all()

    # Unpack the list of tuples into a single list of words
    words = [word for (word,) in data if word]

    # Use Counter to count the occurrences of each word
    word_counts = Counter(words)

    # Get the 5 most common words
    most_common_words = word_counts.most_common(10)
    most5_common_words = word_counts.most_common(5)

    pie_chart = {
        "data": [{
            "labels": [word for word, _ in most5_common_words],
            "values": [count for _, count in most5_common_words],
            "type": "pie"
        }],
        "layout": {
            "title": "Top 5 Most Used Non Inclusive Words",
            "paper_bgcolor": "rgba(0, 0, 0, 0)",
            "plot_bgcolor": "rgba(0, 0, 0, 0)",
        }
    }

    # Convert the pie chart data to JSON
    pie_chart_json = json.dumps(pie_chart, cls=plotly.utils.PlotlyJSONEncoder)

    #!NUMBER OF USES
    max_id = db.session.query(db.func.max(Users.id)).scalar()

    #! BAR CHART WITH TIME
    timestamp_data = db.session.query(func.strftime('%Y-%m-%d', Users.timestamp).label('day'), func.count().label('count')).group_by('day').all()
    timestamps = [timestamp.day for timestamp in timestamp_data]
    counts = [timestamp.count for timestamp in timestamp_data]

    # Create a bar graph for the change in frequency over time
    bar_chart = {
        "data": [{
            "x": timestamps,
            "y": counts,
            "type": "bar",
            "name": "Frequency Over Time",
            "marker": {"color": "#9A52B8"}
        }],
        "layout": {
            "title": "Use of Non-Inclusive Language Over Time",
            "xaxis": {"title": "Date", "tickformat": "%d-%m-%Y"},
            "yaxis": {"title": "Frequency"},
            "paper_bgcolor": "rgba(0, 0, 0, 0)",
            "plot_bgcolor": "rgba(0, 0, 0, 0)",

        }
    }

    # Convert the bar chart data to JSON
    bar_chart_json = json.dumps(bar_chart, cls=plotly.utils.PlotlyJSONEncoder)


    return render_template('analytics.html', plot_json=plot_json, most_common_words=most_common_words, pie_chart_json=pie_chart_json, max_id=max_id, bar_chart_json=bar_chart_json, timestamps=timestamps)

if __name__ == "__main__" :
    # serve(app, host="0.0.0.0", port=8000)
    app.run()