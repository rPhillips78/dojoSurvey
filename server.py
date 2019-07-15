from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "Standing to be the coldest"

@app.route('/form')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    session['username'] = request.form['username']
    session['location'] = request.form['city']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment-area']
    return redirect('/show')

@app.route('/show')
def show():
    return render_template("process.html", )




app.run(debug=True)
