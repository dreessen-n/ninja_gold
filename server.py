import random
import datetime
from flask import Flask, render_template, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key='Mind your pot of GOLD'

@app.route('/')
def index():
    """Render the home page"""
    if 'your_gold' not in session:
        session['your_gold'] = 0
        session['gold_play'] = 0
        session['num_farm'] = 3
        session['num_cave'] = 3
        session['num_house'] = 3
        session['num_casino'] = 3 
        # plays = []
    else:
        session['your_gold'] += session['gold_play']
        session['num_farm'] = random.randint(1, 4)
        session['num_cave'] = random.randint(1, 4)
        session['num_house'] = random.randint(1, 4)
        session['num_casino'] = random.randint(1, 8)
        # x = datetime.datetime.now()
        # plays.append(x.strftime("c"))
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(e):
    """Handle page not found"""
    return f'Sorry! No response. Try again.'

# Ensure file is run directly and not from different
# module, and run localhost on port 5001 for mac
if __name__=="__main__":
    app.run(host='localhost', port=5001, debug=True)
