from flask import Flask, render_template, render_template, request, redirect, session

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Error message for 404
@app.errorhandler(404)
def page_not_found(e):
    return f'Sorry! No response. Try again.'

# Ensure file is run directly and not from different
# module, and run localhost on port 5001 for mac
if __name__=="__main__":
    app.run(host='localhost', port=5001, debug=True)
