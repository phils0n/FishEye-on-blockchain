from fileinput import filename
import flask
from flask import request, jsonify, redirect
import json
from getSmartCon import *
import ast

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/')
def home():
    return '''<h1>Welcome to fisheye</h1>
<p>A prototype API for Ørn Software.</p>
<form method="POST">
    <input name="text">
    <input type="submit">
</form>
'''


@app.route('/upload')
def uploadDef():
    return '''<html>
   <body>
      <form method = "POST" 
         enctype = "multipart/form-data">
         <input type = "file" name = "file" />
         <input type = "submit"/>
      </form>   
   </body>
</html>
'''

lis = []

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    #
    lis.append(text)
    t = "/fish?id=" + text
    return redirect(t, code=302)

@app.route('/upload', methods=['POST'])
def upload():
    #saves submitted files and reads content of file in string format
   if request.method == 'POST':
      f = request.files['file']
      f.save(f.filename)
      file = open(f.filename, "r")
      contents = file.read()
      dictionary = ast.literal_eval(contents)
      file.close()

      id = dictionary["Fish group"]
      s = str(dictionary)
      store(id, s)
      return dictionary



@app.route('/fish', methods=['GET'])
def api_id():
    #get json data on fish based on ID
    if 'id' in request.args:
        id = request.args['id']
    else:
        return "Error: No id field provided. Please specify an id."

    s = retrieve(id)
    res = ast.literal_eval(s)
    return res

app.run()