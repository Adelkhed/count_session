from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)

app.secret_key="adelkhedhiri"

@app.route('/')
def index():
    if 'count' in session:
        session['count'] += 1
        
    else:
        session['count'] = 0
    
    return render_template("index.html")

@app.route('/increment')
def increment():
    if 'count' in session:
        session['count'] += 2 
    return render_template('index.html')

@app.route('/increment_x', methods=['POST'])
def custom_increment():
    value = int(request.form.get('value', 0))
    if 'count' in session:
        session['count'] += value
    return render_template('index.html')

@app.route('/destroy_session')
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)