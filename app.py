from flask import Flask, render_template , app, request
import os
UPLOAD_FOLDER='upload_image'
app=Flask(__name__)
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template('base.html',content=["omkar","vikram","akash"])
@app.route('/chart.html')    
def sing():
    items={"bottle":2,
    "pen":1,
    }
    return render_template('chart.html',content=items) 
if __name__=='__main__':
    app.run('localhost',8080,debug=True)