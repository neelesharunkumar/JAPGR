from flask import Flask
import pprint
import pandas as pd

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello World</h1>'

@app.route('/table')
def table():
    df = pd.read_csv('Patients.csv')
    return df.to_html()


if __name__ == "__main__":
    app.run(debug=True)