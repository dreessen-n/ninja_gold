import random
import datetime
from flask import Flask, render_template, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key='Mind your pot of GOLD'

# Creat a list to store plays
# plays = []
message = ""
message_list = []

@app.route('/')
def index():
    """Render the home page"""
    if 'your_gold' not in session:
        session['your_gold'] = 0
        session['gold_play'] = 0
        session['has_gold'] = 0
        session['message'] = ""
        session['message_list'] = []
        message_list = []
        len_message_list = 0
        num1 = 0
        num2 = 0
    else:
        session['your_gold'] += session['gold_play']
        message_list = session['message_list']
        len_message_list = len(message_list)
    return render_template('index.html', message_list=message_list, len_message_list=len_message_list)

@app.route('/process_money/<string:str1>/<int:num2>', methods=['POST'])
def process(str1, num2):
    """Process the play and calculate wins/loses"""
    num1 = int(str1)
    session['gold_play'] = random.randint(num1, num2)
    session['has_gold'] = 1
    if session['gold_play'] > 0:
        session['message_list'].append(f"<p class='text-success'>Earned {session['gold_play']} from the casino. ({datetime.datetime.now()})</p>")
    else:
        session['message_list'].append(f"<p class='text-danger'>Entered a casino and lost {session['gold_play']} golds... ouch. ({datetime.datetime.now()})</p>")
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
