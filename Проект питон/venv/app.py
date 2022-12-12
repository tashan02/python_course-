import os
import flask
from flask import render_template, redirect, url_for, request
import data_processing as dpr


#from flask import Blueprint


app = flask.Flask('Проект по питону', static_folder= 'data_processing.py')
#app = Blueprint('urlToHash', __name__, template_folder='templates')

#@app.route('/<filename>/', methods =['GET', 'POST'])
#def index(filename:str):
#    q = request.form['q']
    #return render_template('index.html') - - work 

   # return render_template("index.html")
#def show_index_page():
#    return 'Hello'

@app.get('/<filename>/')
def process_word(filename:str):
    #return dpr.finde_all(f'./data/{filename}.txt').to_dict()
    tweets = list(dpr.finde_all(f'./data/{filename}.txt').to_dict().values())
    return flask.render_template("index.html", tweets = tweets)
    
#@app.route('/', methods=["GET"])
#def index():
 
#   return render_template("index.html", messages = messages)
 

 
 



if __name__=='__main__':
    app.run('0.0.0.0', port = 9979, debug = True)