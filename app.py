from flask import Flask, request, flash, url_for, redirect, \
     render_template, abort
from flask_sqlalchemy import SQLAlchemy
import requests

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config.from_pyfile('db.cfg')
db = SQLAlchemy(app)

from models import *
from shells import *
from core import *

errors = []

@app.route('/', methods = ['GET'])
def index():
  base = ''
  try:
      base = Base.query.all()
  except:
        errors.append("Error getting index")
  return render_template('index.html', base=base)

@app.route('/shell', methods = ['GET'])
def shells():
    base =''
    base = Base.query.all()

    return render_template('shell.html', id=id, base=base)

@app.route('/shell/<int:id>', methods = ['GET','POST'])
def shell(id):
    base = ''
    output = ''
    cmd = ''
    os = ''

    id = Base.query.filter_by(id=id).first()
    base = Base.query.all()

    if request.method == 'POST':
        cmd = request.form['cmd']
    try:
        shell_url = 'http://localhost:8000/php_shell.php'
        shell_function = '?cmd='
        shell_os = '?OS'
        shell_user = '?ID'
        os_get = requests.get(shell_url+shell_os)
        user_get = requests.get(shell_url+shell_user)
        if cmd != '':
          r = requests.get(shell_url+shell_function+cmd)
    except:
        errors.append("Error getting shell")
        return render_template('shell.html', errors=errors)
    if cmd != '':
      if r:
        output = r.text
    os = os_get.text
    user = user_get.text
    return render_template('shell.html', output=output, cmd=cmd, id=id, base=base, os=os, user=user)

@app.route('/build', methods = ['GET','POST'])
def build():
    filename = ''
    function = ''
    shell_type = ''
    try:
        if request.method == 'POST':
            filename = request.form['filename']
            function = request.form['function']
            shell_type = request.form['shell_type']
            ShellBuild(filename, shell_type, function)
            return redirect('/')
    except:
        errors.append("Error getting shell")
        return render_template('build.html', errors=errors)
    return render_template('build.html', filename=filename, function=function, shell_type=shell_type)

@app.route('/shell/add', methods = ['GET','POST'])
def add_shell():
    shell_type = ''
    shell_url = ''
    if request.method == 'POST':
        base = Base(shell_url = request.form['shell_url'], shell_type = request.form['shell_type'])
        db.session.add(base)
        db.session.commit()
        #return redirect('/')
        return redirect(url_for('index'))
    return render_template('add_shell.html', shell_type=shell_type, shell_url=shell_url)

if __name__ == '__main__':
    app.run()
