from flask import Flask, session, request, render_template, redirect
app = Flask(__name__)
app.secret_key = 'aSecret' 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/counter', methods=['POST'])
def counter():
    session['counter'] += 2
    return redirect('/')

@app.route('/reset', methods=['POST'])
def resetCounter():
    session['counter'] = 1
    return redirect('/')

app.run(debug=True)