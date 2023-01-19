from flask import Flask, render_template, request
from urllib.parse import unquote_plus, unquote, quote
import urllib
import requests
from requests.utils import requote_uri


app = Flask(__name__)

def parse_query(query):
    query = str(query, 'UTF-8')
    query = unquote_plus(query)
    data = query.split('=')[-1]
    return data

def gpt3_api(query_str):
    query_str = requote_uri(query_str)
    ENDPOINT_PREFIX="http://amaiti-mn1.linkedin.biz:5001/chat?prompt="
    query_url = f"{ENDPOINT_PREFIX}{query_str}"
    print (query_url)
    response = requests.get(query_url)

    if response.status_code == 200:
        print("Successfully connected to GPT3!")
        print('-------------------------------')
        data = response.json()
        return data

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/gpt3',methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        query_str = parse_query(request.get_data())
        data_json = gpt3_api(query_str)
        print (data_json)
        return data_json['resp']

if __name__ == "__main__":
    app.run(debug=True)
