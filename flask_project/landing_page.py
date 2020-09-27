
from flask import Flask, render_template, redirect

from get_json_module import server_response
#this one is my own module, uploaded as get_json_module.py


def hui():
    return str(server_response('http://validate.jsontest.com/?json={"key":"value"}'))


app = Flask(__name__)

@app.route('/')
def start_page() -> '302':
    return redirect('/entry')


@app.route('/entry')
def entry_page() -> 'html':
    my_string = 'hui pizda'
    return render_template('entry.html', the_title='Welcome to JSON tool', returned_json = my_string)
 

@app.route('/request')
def response_method() -> str:
    return str(server_response('http://validate.jsontest.com/?json={"key":"value"}'))


app.run()
