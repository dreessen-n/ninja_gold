import random
import datetime
from flask import Flask, render_template, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key='Mind your pot of GOLD'

# Creat a list to store plays
# plays = []
message = ""

@app.route('/')
def index():
    """Render the home page"""
    if 'your_gold' not in session:
        session['your_gold'] = 0
        session['gold_play'] = 0
        session['has_gold'] = 0
        session['message'] = ""
    else:
        session['your_gold'] += session['gold_play']
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process():
    """Process the play and calculate wins/loses"""
    if request.form['name'] == 'farm':
        session['gold_play'] = random.randint(10, 20)
        session['has_gold'] = 1
        session['message'] += f"<p class='text-success'>Earned {session['gold_play']} from the farm. ({datetime.datetime.now()})</p>"
    elif request.form['name'] == 'cave':
        session['gold_play'] = random.randint(5, 10)
        session['has_gold'] = 1
        session['message'] += f"<p class='text-success'>Earned {session['gold_play']} from the cave. ({datetime.datetime.now()})</p>"
    elif request.form['name'] == 'house':
        session['gold_play'] = random.randint(2, 5)
        session['has_gold'] = 1
        session['message'] += f"<p class='text-success'>Earned {session['gold_play']} from the house. ({datetime.datetime.now()})</p>"
    else:
        session['gold_play'] = random.randint(-50, 50)
        session['has_gold'] = 1
        if session['gold_play'] > 0:
            session['message'] += f"<p class='text-success'>Earned {session['gold_play']} from the casino. ({datetime.datetime.now()})</p>"
        else:
            session['message'] += f"<p class='text-danger'>Entered a casino and lost {session['gold_play']} golds... ouch. ({datetime.datetime.now()})</p>"
    return redirect('/')

@app.route('/end_session')
def end_session():
    """Clear the session"""
    session.clear()
    return redirect('/')

@app.errorhandler(404)
def page_not_found(e):
    """Handle page not found"""
    return f'Sorry! No response. Try again.'

# Ensure file is run directly and not from different
# module, and run localhost on port 5001 for mac
if __name__=="__main__":
    app.run(host='localhost', port=5001, debug=True)
