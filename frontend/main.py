from flask import Flask, render_template, request      

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/gpt3',methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        return "Response from the Gpt3 Model";

    
if __name__ == "__main__":
    app.run(debug=True)
